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
import collections
import pandas as pd

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

from plot.tools.tools import add_letter

from analysis.model.stats import stats_regression_best_values
from analysis.model.model import AgentSideAdditive
# DMSciReports, AgentSoftmax, AgentSide

from parameters.parameters import CONTROL_CONDITIONS, \
    FIG_FOLDER, BACKUP_FOLDER, EXPORT_FOLDER, GAIN, LOSS
from analysis.data_preprocessing \
    import get_control_data, get_control_sigmoid_data, \
    get_freq_risk_data, get_info_data, get_control_history_data, \
    get_control_stats

from analysis.model.parameter_estimate import get_parameter_estimate
# from analysis.summary import summary

# np.seterr(all='raise')

def nested_dict():
    return collections.defaultdict(nested_dict)


class Analysis:

    LIMIT_N_TRIAL = 2000

    def __init__(self, class_model, **kwargs):

        self.class_model = class_model

        self.monkeys = None
        self.n_monkey = None

        self.info_data = nested_dict()
        self.control_data = nested_dict()
        self.control_stats = nested_dict()
        self.freq_risk_data = nested_dict()
        self.hist_best_param_data = nested_dict()
        self.hist_control_data = nested_dict()
        self.control_sigmoid_data = nested_dict()

        self.cpt_fit = nested_dict()
        self.risk_sig_fit = nested_dict()
        self.control_sig_fit = nested_dict()

        self._pre_process_data(**kwargs)

    @classmethod
    def get_monkeys(cls):

        selected_monkeys = []

        monkeys = list(np.unique(Data.objects.values_list("monkey")))
        print("All monkeys:", monkeys)

        for m in monkeys:
            keep = True
            entries_m = Data.objects.filter(monkey=m)

            for cond in GAIN, LOSS:

                if cond == GAIN:
                    entries = entries_m.filter(is_gain=True)
                elif cond == LOSS:
                    entries = entries_m.filter(is_loss=True)
                else:
                    raise ValueError

                n_trial = entries.count()
                if n_trial < cls.LIMIT_N_TRIAL:
                    print(f"Monkey '{m}' has only {n_trial} trials in condition '{cond}', "
                          f"it will not be included in the analysis")
                    keep = False

                n_right = entries.filter(c=1).count()
                prop_right = n_right / n_trial
                if not 0.20 <= prop_right <= 0.80:
                    print(
                        f"Monkey '{m}' choose the right option {prop_right * 100:.2f}% of the time in condition '{cond}', "
                        f"it will not be included in the analysis")
                    keep = False

            if keep:
                selected_monkeys.append(m)

        print("Selected monkeys:", selected_monkeys)
        return selected_monkeys

    def _pre_process_data(self,
                          skip_exception=True,
                          monkeys=None, **kwargs):

        if monkeys is None:
            monkeys = self.get_monkeys()

        black_list = []

        for m in monkeys:

            try:
                for cond in (GAIN, LOSS):

                    self._analyse_monkey(m=m, cond=cond, **kwargs)
                    print()

            except Exception as e:
                if skip_exception:
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
            for cond in GAIN, LOSS:
                self.info_data[cond].pop(m, None)
                self.control_data[cond].pop(m, None)
                self.freq_risk_data[cond].pop(m, None)
                self.hist_best_param_data[cond].pop(m, None)
                self.hist_control_data[cond].pop(m, None)
                self.control_sigmoid_data[cond].pop(m, None)
                self.cpt_fit[cond].pop(m, None)
                self.risk_sig_fit[cond].pop(m, None)
                self.control_sig_fit[cond].pop(m, None)

        self.monkeys = monkeys
        self.n_monkey = len(monkeys)

    def _analyse_monkey(self, m, cond, method,
                        n_trials_per_chunk=None,
                        n_chunk=None,
                        n_trials_per_chunk_control=None,
                        n_chunk_control=None,
                        randomize_chunk_trials=False, force_fit=True,):

        print()
        print("-" * 60 + f" {m} " + "-" * 60 + "\n")

        if cond == GAIN:
            entries = Data.objects.filter(monkey=m, is_gain=True)
        elif cond == LOSS:
            entries = Data.objects.filter(monkey=m, is_loss=True)

        else:
            raise ValueError

        # Sort the data, run fit, etc.
        self.info_data[cond][m] = get_info_data(entries=entries, monkey=m)

        self.control_data[cond][m] = get_control_data(entries)
        self.control_stats[cond][m] = \
            get_control_stats(self.control_data[cond][m])

        self.control_sigmoid_data[cond][m] = \
            get_control_sigmoid_data(entries)
        self.control_sig_fit[cond][m] = \
            {cd: self.control_sigmoid_data[cond][m][cd]['fit']
             for cd in CONTROL_CONDITIONS}

        self.freq_risk_data[cond][m] = get_freq_risk_data(entries)
        self.risk_sig_fit[cond][m] = self.freq_risk_data[cond][m]['fit']

        self.cpt_fit[cond][m] = get_parameter_estimate(
            cond=cond,
            entries=entries,
            force=force_fit,
            n_trials_per_chunk=n_trials_per_chunk,
            n_chunk=n_chunk,
            randomize=randomize_chunk_trials,
            class_model=self.class_model,
            method=method)

        # Stats for comparison of best parameter values
        self.hist_best_param_data[cond][m] = {
            'fit': self.cpt_fit[cond][m],
            'regression':
                stats_regression_best_values(
                    fit=self.cpt_fit[cond][m],
                    class_model=self.class_model)}

        # history of performance for control trials
        self.hist_control_data[cond][m] = \
            get_control_history_data(
                entries=entries,
                n_trials_per_chunk=n_trials_per_chunk_control,
                n_chunk=n_chunk_control)


class Plot:

    def __init__(self, analysis):

        self.monkeys = analysis.monkeys
        self.class_model = analysis.class_model

        self.a = analysis

        self.pdf = None
        self.target_monkey = None

        self.fig_suffix = f"_{self.class_model.__name__}.pdf"

    # def create_figure(self, plot_function, data, n_subplot=1):
    #
    #     n_rows = n_subplot
    #     n_cols = self.a.n_monkey if self.target_monkey is None else 1
    #     fig, axes = plt.subplots(nrows=n_rows,
    #                              ncols=n_cols,
    #                              figsize=(6*n_cols, 6*n_rows))
    #
    #     if self.target_monkey is None and self.a.n_monkey > 1:
    #         if len(axes.shape) > 1:
    #             axes = axes.T
    #         for i, m in enumerate(self.a.monkeys):
    #             plot_function(axes[i], data[m])
    #
    #     else:
    #         plot_function(axes, data[self.target_monkey])
    #
    #     plt.tight_layout()
    #     self.pdf.savefig(fig)
    #     plt.close(fig)
    #
    # def create_pdf(self, monkey=None):
    #
    #     self.target_monkey = monkey
    #
    #     # Define the path
    #     pdf_path = os.path.join(
    #         FIG_FOLDER,
    #         f"results{monkey if monkey is not None else ''}"
    #         f"{self.fig_suffix}")
    #
    #     print(f"Creating the figure '{pdf_path}'...")
    #
    #     # Create the pdf
    #     self.pdf = PdfPages(pdf_path)
    #
    #     # Fig: Info
    #     self.create_figure(
    #         plot_function=plot.info.fig_info,
    #         data=self.a.info_data)
    #
    #     # Fig: Control
    #     self.create_figure(
    #         plot_function=plot.control.plot,
    #         data=self.a.control_data)
    #
    #     # Fig: Control sigmoid
    #     self.create_figure(
    #         plot_function=plot.control_sigmoid.plot,
    #         data=self.a.control_sigmoid_data,
    #         n_subplot=len(CONTROL_CONDITIONS))
    #
    #     # Fig: Freq risky choice against expected value
    #     self.create_figure(
    #         plot_function=plot.freq_risk.plot,
    #         data=self.a.freq_risk_data)
    #
    #     # Fig: Utility function
    #     self.create_figure(
    #         plot_function=plot.utility.plot,
    #         data=self.a.cpt_fit)
    #
    #     # Fig: Probability distortion
    #     self.create_figure(
    #         plot_function=plot.probability_distortion.plot,
    #         data=self.a.cpt_fit)
    #
    #     # Fig: Precision
    #     self.create_figure(
    #         plot_function=plot.precision.plot,
    #         data=self.a.cpt_fit)
    #
    #     # Fig: Best param history
    #     self.create_figure(
    #         plot_function=plot.history_best_param.plot,
    #         data=self.a.hist_best_param_data,
    #         n_subplot=len(self.a.class_model.param_labels))
    #
    #     # Fig: Control history
    #     self.create_figure(
    #         plot_function=plot.history_control.plot,
    #         data=self.a.hist_control_data,
    #         n_subplot=len(CONTROL_CONDITIONS))
    #
    #     self.pdf.close()
    #     self.target_monkey = None
    #
    #     print(f"Figure '{pdf_path}' created.\n")

    # def create_best_param_distrib_and_lls_distrib(self):
    #
    #     # Define the path
    #     fig_path = os.path.join(
    #         FIG_FOLDER,
    #         f"best_param_distrib{self.fig_suffix}")
    #
    #     print(f"Creating the figure '{fig_path}'...")
    #
    #     plot.best_param_distrib.plot(
    #         self.a.cpt_fit, fig_path=fig_path,
    #         param_labels=self.a.class_model.param_labels)
    #
    #     fig_path_lls = os.path.join(
    #         FIG_FOLDER,
    #         f"LLS_distrib{self.fig_suffix}")
    #
    #     fig_path_bic = os.path.join(
    #         FIG_FOLDER,
    #         f"BIC_distrib{self.fig_suffix}.pdf")
    #
    #     print(f"Creating the figure '{fig_path_lls}'...")
    #     print(f"Creating the figure '{fig_path_bic}'...")
    #     plot.LLS_BIC_distrib.plot(self.a.cpt_fit, fig_path_lls=fig_path_lls,
    #                               fig_path_bic=fig_path_bic)

    def create_main_figure(self):

        nrows, ncols = 2, 3
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols,
                                 figsize=(6*ncols, 6*nrows))

        colors = ['C0', 'C1']

        linestyles = ['--' if i in ('Havane', 'Gladys') else ':' for i in self.monkeys]

        for i, cond in enumerate((GAIN, LOSS)):
            # Fig: Utility function
            data = {'class_model': self.a.class_model,
                    'cond': cond}
            for param in ("risk_aversion", "distortion",
                          "precision", "side_bias"):
                data[param] = [np.mean(self.a.cpt_fit[cond][m][param])
                               for m in self.a.monkeys]

            plot.utility.plot(ax=axes[i, 0], data=data, color=colors[i],
                              linestyles=linestyles)
            add_letter(axes[i, 0], i=i*3)
            plot.probability_distortion.plot(ax=axes[i, 1], data=data,
                                             color=colors[i],
                                             linestyles=linestyles)
            add_letter(axes[i, 1], i=i*3+1)
            plot.precision.plot(ax=axes[i, 2], data=data, color=colors[i],
                                linestyles=linestyles)
            add_letter(axes[i, 2], i=i * 3 + 2)

        fig_path = os.path.join(
            FIG_FOLDER,
            f"main{self.fig_suffix}")
        plt.tight_layout()
        plt.savefig(fig_path)
        print(f"Figure {fig_path} created!")

    def export_csv(self):

        data = dict()
        data["monkey"] = [m for m in self.monkeys]
        for cond in GAIN, LOSS:
            for param in "distortion", "risk_aversion", "precision", "side_bias":
                xs = [self.a.cpt_fit[cond][m][param] for m in self.monkeys]
                x = [np.mean(i) for i in xs]
                data[f"{cond}-{param}"] = x

            if cond == GAIN:
                entries = Data.objects.filter(is_gain=True)
            elif cond == LOSS:
                entries = Data.objects.filter(is_loss=True)
            else:
                raise ValueError
            data[f"{cond}-n_trial"] = [
                entries.filter(monkey=m).count() for m in self.monkeys
            ]

        df = pd.DataFrame(data=data)
        df.to_csv(os.path.join(EXPORT_FOLDER, f"param.csv"))


def main():

    # for class_model in (AgentSideAdditive, AgentSide,
    #                     AgentSoftmax, DMSciReports):
    force = False
    class_model = AgentSideAdditive

    print("*" * 150)
    print(f"Using model '{class_model.__name__}'")
    print("*" * 150)
    print()

    bkp_file = os.path.join(BACKUP_FOLDER,
                            f"analysis_{class_model.__name__}")

    if not os.path.exists(bkp_file) or force:
        a = Analysis(
            monkeys=None, # ('Havane', ),""#'Gladys'),
            class_model=class_model,
            n_trials_per_chunk=200,
            n_trials_per_chunk_control=500,
            method='SLSQP',
            force_fit=force,
            skip_exception=False)
        pickle.dump(a, open(bkp_file, "wb"))
    else:
        a = pickle.load(open(bkp_file, "rb"))

    # # summary.create(
    # #     info_data=a.info_data,
    # #     control_data=a.control_data,
    # #     cpt_fit=a.cpt_fit,
    # #     control_sig_fit=a.control_sig_fit,
    # #     risk_sig_fit=a.risk_sig_fit,
    # #     class_model=a.class_model
    # # )
    p = Plot(analysis=a)
    p.export_csv()
    p.create_main_figure()
    # p.create_pdf()
    # # for m in a.monkeys:
    # #     p.create_pdf(monkey=m)
    # # p.create_best_param_distrib_and_lls_distrib()
    # p.create_main_figure()


if __name__ == '__main__':
    main()
