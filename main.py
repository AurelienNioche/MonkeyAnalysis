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

import plot.history
import plot.precision
import plot.probability_distortion
import plot.utility
import plot.control
import plot.freq_risk
import plot.control_sigmoid
import plot.info
import plot.best_param_distrib

import analysis.model.parameter_estimate
from analysis.model.stats import stats_regression_best_values
from analysis.model.model import DMSciReports
# DMEpsilon, DMNicolas, DMSoftmax, DMSoftmaxSideBias
# from model.stats import stats_comparison_best_values

from analysis.parameters.parameters import CONTROL_CONDITIONS
from analysis.data_preprocessing \
    import get_control_data, get_control_sigmoid_data, \
    get_freq_risk_data, get_info_data

from analysis.model.parameter_estimate import get_parameter_estimate

import analysis.summary
import analysis.data_preprocessing.info

from analysis.parameters.parameters import FIG_FOLDER

# np.seterr(all='raise')

NAME = "main"


LIMIT_N_TRIAL = 2000


def get_monkeys():
    monkeys = list(np.unique(Data.objects.values_list("monkey")))
    for m in monkeys:
        n_trial = Data.objects.filter(monkey=m).count()
        if n_trial < LIMIT_N_TRIAL:
            print(f"Monkey '{m}' has only {n_trial} trials, "
                  f"it will not be included in the analysis")
            monkeys.remove(m)
    return monkeys


def get_n_trial(monkey):
    return Data.objects.filter(monkey=monkey).count()


class Analysis:

    def __init__(self, class_model, **kwargs):

        self.class_model = class_model

        self.monkeys = None
        self.n_monkey = None

        self.data = {}

        self.info_data = {}
        self.control_data = {}
        self.exemplary_data = {}
        self.freq_risk_data = {}
        self.hist_best_param_data = {}
        self.hist_control_data = {}
        self.control_sigmoid_data = {}

        self.cpt_fit = {}
        self.risk_sig_fit = {}
        self.control_sig_fit = {}

        self.pdf = None
        self.target_monkey = None

        self._pre_process_data(**kwargs)

    def _pre_process_data(self,
                          method,
                          n_trials_per_chunk=None,
                          n_chunk=None,
                          randomize_chunk_trials=False, force_fit=True,
                          skip_exception=True,
                          monkeys=None):

        if monkeys is None:
            monkeys = get_monkeys()
        n_monkey = len(monkeys)

        black_list = []

        for i in range(n_monkey):

            try:

                m = monkeys[i]

                print()
                print("-" * 60 + f" {m} " + "-" * 60 + "\n")

                # Sort the data, run fit, etc.
                self.info_data[m] = get_info_data(monkey=m)

                self.control_data[m] = get_control_data(monkey=m)

                self.control_sigmoid_data[m] = \
                    get_control_sigmoid_data(monkey=m)
                self.control_sig_fit[m] = \
                    {cd: self.control_sigmoid_data[m][cd]['fit']
                     for cd in CONTROL_CONDITIONS}

                self.freq_risk_data[m] = get_freq_risk_data(monkey=m)
                self.risk_sig_fit[m] = self.freq_risk_data[m]['fit']

                self.cpt_fit[m] = get_parameter_estimate(
                    monkey=m,
                    force=force_fit,
                    n_trials_per_chunk=n_trials_per_chunk,
                    n_chunk=n_chunk,
                    randomize=randomize_chunk_trials,
                    class_model=self.class_model,
                    method=method,
                )
                #
                # #     # Stats for comparison of best parameter values
                # #     stats_comparison_best_values(fit, monkey=monkey)
                #
                # Stats for comparison of best parameter values
                self.hist_best_param_data[m] = {
                    'fit': self.cpt_fit[m],
                    'regression':
                        stats_regression_best_values(
                            fit=self.cpt_fit[m],
                            class_model=self.class_model)
                }

                # # history of performance for control trials
                # self.hist_control_data[m] = \
                #     experimental_data.filter.control.control_history_sort_data(
                #         alternatives=alternatives,
                #         control_types=control_types,
                #         hits=hits, n_chunk=n_chunk,
                #         n_trials_per_chunk=n_trials_per_chunk,
                #     )
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
            self.data.pop(m, None)
            self.info_data.pop(m, None)
            self.control_data.pop(m, None)
            self.exemplary_data.pop(m, None)
            self.freq_risk_data.pop(m, None)
            self.hist_best_param_data.pop(m, None)
            self.hist_control_data.pop(m, None)
            self.control_sigmoid_data.pop(m, None)
            self.cpt_fit.pop(m, None)
            self.risk_sig_fit.pop(m, None)
            self.control_sig_fit.pop(m, None)

        self.monkeys = monkeys
        self.n_monkey = len(monkeys)

    def create_figure(self, plot_function, data, n_subplot=1):

        n_rows = n_subplot
        n_cols = self.n_monkey if self.target_monkey is None else 1
        fig, axes = plt.subplots(nrows=n_rows,
                                 ncols=n_cols,
                                 figsize=(6*n_cols, 6*n_rows))

        if self.target_monkey is None and self.n_monkey > 1:
            if len(axes.shape) > 1:
                axes = axes.T
            for i, m in enumerate(self.monkeys):
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
            f"results{monkey if monkey is not None else ''}_"
            f"{self.class_model.__name__}.pdf")

        print(f"Creating the figure '{pdf_path}'...")

        # Create the pdf
        self.pdf = PdfPages(pdf_path)

        # Fig: Info
        self.create_figure(
            plot_function=plot.info.fig_info,
            data=self.info_data)

        # Fig: Control
        self.create_figure(
            plot_function=plot.control.plot,
            data=self.control_data)

        # Fig: Control sigmoid
        self.create_figure(
            plot_function=plot.control_sigmoid.control_sigmoid,
            data=self.control_sigmoid_data,
            n_subplot=len(CONTROL_CONDITIONS))

        # Fig: Freq risky choice against expected value
        self.create_figure(
            plot_function=plot.freq_risk.plot,
            data=self.freq_risk_data)

        # Fig: Utility function
        self.create_figure(
            plot_function=plot.utility.plot,
            data=self.cpt_fit)

        # Fig: Probability distortion
        self.create_figure(
            plot_function=plot.probability_distortion.plot,
            data=self.cpt_fit)

        # Fig: Precision
        self.create_figure(
            plot_function=plot.precision.plot,
            data=self.cpt_fit)

        # Fig: Best param history
        self.create_figure(
            plot_function=plot.history.history_best_param,
            data=self.hist_best_param_data,
            n_subplot=len(self.class_model.param_labels))

        # # Fig: Control history
        # self.create_figure(
        #     plot_function=plot.history.history_control,
        #     data=self.hist_control_data,
        #     n_subplot=len(CONTROL_CONDITIONS))

        self.pdf.close()
        self.target_monkey = None

        print(f"Figure '{pdf_path}' created.\n")

    def create_summary(self):
        pass
        #
        # analysis.summary.create(
        #     info_data=self.info_data,
        #     control_data=self.control_data,
        #     cpt_fit=self.cpt_fit,
        #     control_sig_fit=self.control_sig_fit,
        #     risk_sig_fit=self.risk_sig_fit,
        #     class_model=self.class_model
        # )

    def create_best_param_distrib(self):

        # Define the path
        fig_path = os.path.join(
            FIG_FOLDER,
            f"best_param_distrib_{self.class_model.__name__}.pdf")

        print(f"Creating the figure '{fig_path}'...")

        plot.best_param_distrib.plot(self.cpt_fit, fig_path=fig_path,
                                     param_labels=self.class_model.param_labels)


def main():

    # for class_model in (DMSciReports, DMEpsilon, DMNicolas, DMSoftmax,
    #                     DMSoftmaxSideBias):

    class_model = DMSciReports
    a = Analysis(
        monkeys=None, # ('Havane', 'Gladys'),
        class_model=class_model,
        n_trials_per_chunk=200,
        method='SLSQP',
        force_fit=True,
        skip_exception=True)
    a.create_summary()
    a.create_pdf()
    for m in a.monkeys:
        a.create_pdf(monkey=m)

    a.create_best_param_distrib()


if __name__ == '__main__':
    main()
