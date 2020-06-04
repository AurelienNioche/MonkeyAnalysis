import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "MonkeyAnalysis.settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from data_interface.models import Data

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import traceback
import warnings
import pickle

import plot.history_best_param
import plot.history_control
import plot.precision
import plot.probability_distortion
import plot.utility
import plot.control
import plot.freq_risk
import plot.control_sigmoid
import plot.info
import plot.best_param_distrib
import plot.LLS_BIC_distrib

from analysis.model.stats import stats_regression_best_values
from analysis.model.model import AgentSideAdditive
# DMSciReports, AgentSoftmax, AgentSide

from parameters.parameters import CONTROL_CONDITIONS, \
    FIG_FOLDER, BACKUP_FOLDER, GAIN, LOSS
from analysis.data_preprocessing \
    import get_control_data, get_control_sigmoid_data, \
    get_freq_risk_data, get_info_data, get_control_history_data, \
    get_control_stats

from analysis.model.parameter_estimate import get_parameter_estimate
# from analysis.summary import summary

# np.seterr(all='raise')


class Analysis:

    LIMIT_N_TRIAL = 2000

    def __init__(self, class_model, cond, **kwargs):

        self.class_model = class_model
        self.cond = cond

        self.monkeys = None
        self.n_monkey = None

        self.info_data = {}
        self.control_data = {}
        self.control_stats = {}
        self.freq_risk_data = {}
        self.hist_best_param_data = {}
        self.hist_control_data = {}
        self.control_sigmoid_data = {}

        self.cpt_fit = {}
        self.risk_sig_fit = {}
        self.control_sig_fit = {}

        self._pre_process_data(**kwargs)

    @classmethod
    def get_monkeys(cls):

        monkeys = list(np.unique(Data.objects.values_list("monkey")))
        print(monkeys)
        # black_list = []
        selected_monkeys = []
        for m in monkeys:
            keep = True
            entries = Data.objects.filter(monkey=m)
            n_trial = entries.count()
            if n_trial < cls.LIMIT_N_TRIAL:
                print(f"Monkey '{m}' has only {n_trial} trials, "
                      f"it will not be included in the analysis")
                keep = False
                # black_list.append(m)

            n_right = entries.filter(c=1).count()
            prop_right = n_right / n_trial
            if not 0.15 <= prop_right <= 0.85:
                print(
                    f"Monkey '{m}' choose the right option {prop_right * 100:.2f}% of the time, "
                    f"it will not be included in the analysis")
                keep = False
                # black_list.append(m)

            if keep:
                selected_monkeys.append(m)

        return selected_monkeys

    # @classmethod
    # def get_n_trial(cls, monkey):
    #     return Data.objects.filter(monkey=monkey).count()

    def _pre_process_data(self,
                          method,
                          n_trials_per_chunk=None,
                          n_chunk=None,
                          n_trials_per_chunk_control=None,
                          n_chunk_control=None,
                          randomize_chunk_trials=False, force_fit=True,
                          skip_exception=True,
                          monkeys=None):

        if monkeys is None:
            monkeys = self.get_monkeys()
        n_monkey = len(monkeys)

        black_list = []

        for i in range(n_monkey):

            try:

                m = monkeys[i]

                print()
                print("-" * 60 + f" {m} " + "-" * 60 + "\n")

                if self.cond == GAIN:
                    entries = Data.objects.filter(monkey=m, is_gain=True)
                elif self.cond == LOSS:
                    entries = Data.objects.filter(monkey=m, is_loss=True)

                else:
                    raise ValueError

                # Sort the data, run fit, etc.
                self.info_data[m] = get_info_data(entries=entries, monkey=m)

                self.control_data[m] = get_control_data(entries)
                self.control_stats[m] = get_control_stats(self.control_data[m])

                self.control_sigmoid_data[m] = \
                    get_control_sigmoid_data(entries)
                self.control_sig_fit[m] = \
                    {cd: self.control_sigmoid_data[m][cd]['fit']
                     for cd in CONTROL_CONDITIONS}

                self.freq_risk_data[m] = get_freq_risk_data(entries)
                self.risk_sig_fit[m] = self.freq_risk_data[m]['fit']

                self.cpt_fit[m] = get_parameter_estimate(
                    cond=self.cond,
                    entries=entries,
                    force=force_fit,
                    n_trials_per_chunk=n_trials_per_chunk,
                    n_chunk=n_chunk,
                    randomize=randomize_chunk_trials,
                    class_model=self.class_model,
                    method=method)

                # Stats for comparison of best parameter values
                self.hist_best_param_data[m] = {
                    'fit': self.cpt_fit[m],
                    'regression':
                        stats_regression_best_values(
                            fit=self.cpt_fit[m],
                            class_model=self.class_model)
                }

                # history of performance for control trials
                self.hist_control_data[m] = \
                    get_control_history_data(
                        entries=entries,
                        n_trials_per_chunk=n_trials_per_chunk_control,
                        n_chunk=n_chunk_control)
                print()

            except Exception as e:
                if skip_exception:
                    m = monkeys[i]
                    track = traceback.format_exc()
                    msg = \
                        f"\nWhile trying to pre-process the data for " \
                        f"monkey '{m}', " \
                        f"I encountered an error. " \
                        "\nHere is the error:\n\n" \
                        f"{track}\n" \
                        f"I will skip the monkey '{m}' " \
                        f"from the rest of the analysis"
                    warnings.warn(msg)
                    black_list.append(m)
                else:
                    raise e

        for m in black_list:
            monkeys.remove(m)
            self.info_data.pop(m, None)
            self.control_data.pop(m, None)
            self.freq_risk_data.pop(m, None)
            self.hist_best_param_data.pop(m, None)
            self.hist_control_data.pop(m, None)
            self.control_sigmoid_data.pop(m, None)
            self.cpt_fit.pop(m, None)
            self.risk_sig_fit.pop(m, None)
            self.control_sig_fit.pop(m, None)

        self.monkeys = monkeys
        self.n_monkey = len(monkeys)


class Plot:

    def __init__(self, analysis):

        self.a = analysis

        self.pdf = None
        self.target_monkey = None

        self.fig_suffix = f"_{self.a.class_model.__name__}_{self.a.cond}.pdf"

    def create_figure(self, plot_function, data, n_subplot=1):

        n_rows = n_subplot
        n_cols = self.a.n_monkey if self.target_monkey is None else 1
        fig, axes = plt.subplots(nrows=n_rows,
                                 ncols=n_cols,
                                 figsize=(6*n_cols, 6*n_rows))

        if self.target_monkey is None and self.a.n_monkey > 1:
            if len(axes.shape) > 1:
                axes = axes.T
            for i, m in enumerate(self.a.monkeys):
                plot_function(axes[i], data[m])

        else:
            plot_function(axes, data[self.target_monkey])

        plt.tight_layout()
        self.pdf.savefig(fig)
        plt.close(fig)

    def create_pdf(self, monkey=None):

        self.target_monkey = monkey

        # Define the path
        pdf_path = os.path.join(
            FIG_FOLDER,
            f"results{monkey if monkey is not None else ''}"
            f"{self.fig_suffix}")

        print(f"Creating the figure '{pdf_path}'...")

        # Create the pdf
        self.pdf = PdfPages(pdf_path)

        # Fig: Info
        self.create_figure(
            plot_function=plot.info.fig_info,
            data=self.a.info_data)

        # Fig: Control
        self.create_figure(
            plot_function=plot.control.plot,
            data=self.a.control_data)

        # Fig: Control sigmoid
        self.create_figure(
            plot_function=plot.control_sigmoid.plot,
            data=self.a.control_sigmoid_data,
            n_subplot=len(CONTROL_CONDITIONS))

        # Fig: Freq risky choice against expected value
        self.create_figure(
            plot_function=plot.freq_risk.plot,
            data=self.a.freq_risk_data)

        # Fig: Utility function
        self.create_figure(
            plot_function=plot.utility.plot,
            data=self.a.cpt_fit)

        # Fig: Probability distortion
        self.create_figure(
            plot_function=plot.probability_distortion.plot,
            data=self.a.cpt_fit)

        # Fig: Precision
        self.create_figure(
            plot_function=plot.precision.plot,
            data=self.a.cpt_fit)

        # Fig: Best param history
        self.create_figure(
            plot_function=plot.history_best_param.plot,
            data=self.a.hist_best_param_data,
            n_subplot=len(self.a.class_model.param_labels))

        # Fig: Control history
        self.create_figure(
            plot_function=plot.history_control.plot,
            data=self.a.hist_control_data,
            n_subplot=len(CONTROL_CONDITIONS))

        self.pdf.close()
        self.target_monkey = None

        print(f"Figure '{pdf_path}' created.\n")

    def create_best_param_distrib_and_lls_distrib(self):

        # Define the path
        fig_path = os.path.join(
            FIG_FOLDER,
            f"best_param_distrib{self.fig_suffix}")

        print(f"Creating the figure '{fig_path}'...")

        plot.best_param_distrib.plot(
            self.a.cpt_fit, fig_path=fig_path,
            param_labels=self.a.class_model.param_labels)

        fig_path_lls = os.path.join(
            FIG_FOLDER,
            f"LLS_distrib{self.fig_suffix}")

        fig_path_bic = os.path.join(
            FIG_FOLDER,
            f"BIC_distrib{self.fig_suffix}.pdf")

        print(f"Creating the figure '{fig_path_lls}'...")
        print(f"Creating the figure '{fig_path_bic}'...")
        plot.LLS_BIC_distrib.plot(self.a.cpt_fit, fig_path_lls=fig_path_lls,
                                  fig_path_bic=fig_path_bic)

    def create_main_figure(self):

        nrows, ncols = 1, 3
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols,
                                 figsize=(6*ncols, 6*nrows))

        # Fig: Utility function
        data = {'risk_aversion': [np.mean(self.a.cpt_fit[m]['risk_aversion'])
                for m in self.a.monkeys],
                'class_model': self.a.class_model,
                'cond': self.a.cond}
        plot.utility.plot(ax=axes[0], data=data)

        # Fig: Probability distortion
        data = {'distortion': [np.mean(self.a.cpt_fit[m]['distortion']) for m in self.a.monkeys],
                'class_model': self.a.class_model,
                'cond': self.a.cond}
        plot.probability_distortion.plot(ax=axes[1], data=data)

        # Fig: Precision
        data = {'precision': [np.mean(self.a.cpt_fit[m]['precision'])
                              for m in self.a.monkeys],
                'side_bias': [np.mean(self.a.cpt_fit[m]['side_bias'])
                              for m in self.a.monkeys],
                'class_model': self.a.class_model,
                'cond': self.a.cond}
        plot.precision.plot(ax=axes[2], data=data)

        fig_path = os.path.join(
            FIG_FOLDER,
            f"main{self.fig_suffix}")
        plt.tight_layout()
        plt.savefig(fig_path)
        print(f"Figure {fig_path} created!")


def main():

    # for class_model in (AgentSideAdditive, AgentSide,
    #                     AgentSoftmax, DMSciReports):
    force = True
    class_model = AgentSideAdditive

    for cond in GAIN, LOSS:

        print("*" * 150)
        print(f"Using model '{class_model.__name__}' - COND: {cond}")
        print("*" * 150)
        print()

        bkp_file = os.path.join(BACKUP_FOLDER,
                                f"analysis_{class_model.__name__}_{cond}")

        if not os.path.exists(bkp_file) or force:
            a = Analysis(
                cond=cond,
                monkeys=None,  # ('Havane', 'Gladys'),
                class_model=class_model,
                n_trials_per_chunk=200,
                n_trials_per_chunk_control=500,
                method='SLSQP',
                force_fit=force,
                skip_exception=False)
            pickle.dump(a, open(bkp_file, "wb"))
        else:
            a = pickle.load(open(bkp_file, "rb"))

        # summary.create(
        #     info_data=a.info_data,
        #     control_data=a.control_data,
        #     cpt_fit=a.cpt_fit,
        #     control_sig_fit=a.control_sig_fit,
        #     risk_sig_fit=a.risk_sig_fit,
        #     class_model=a.class_model
        # )
        p = Plot(analysis=a)
        # p.create_pdf()
        # for m in a.monkeys:
        #     p.create_pdf(monkey=m)
        # p.create_best_param_distrib_and_lls_distrib()
        p.create_main_figure()


if __name__ == '__main__':
    main()
