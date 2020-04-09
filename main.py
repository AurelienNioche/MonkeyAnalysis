import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "MonkeyAnalysis.settings")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.axes._axes
from parameters.parameters import FIG_FOLDER, CONTROL_CONDITIONS, GAIN, LOSS

from experimental_data.get import get_data, get_monkeys
import experimental_data.filter.control
import experimental_data.filter.exemplary
import experimental_data.filter.freq_risk
import experimental_data.filter.control_sigmoid

import plot.history
import plot.precision
import plot.probability_distortion
import plot.utility
import plot.control
import plot.freq_risk
import plot.exemplary_case
import plot.control_sigmoid
import plot.info

import model.parameter_estimate
from model.stats import stats_regression_best_values
# from model.stats import stats_comparison_best_values

import analysis.summary
import analysis.info

import numpy as np

import warnings

np.seterr(all='raise')

NAME = "main"


class Analysis:

    def __init__(self, **kwargs):
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
                          n_chunk=5, starting_point="2020-02-18",
                          randomize_chunk_trials=False, force_fit=False,
                          skip_exception=False):

        monkeys = get_monkeys()[:2]
        n_monkey = len(monkeys)

        black_list = []

        for i in range(n_monkey):

            try:

                m = monkeys[i]

                print()
                print("-" * 60 + f" {m} " + "-" * 60 + "\n")

                # Pre-process data --------------------------------

                # Get the data
                d = get_data(m, starting_point=starting_point)
                self.data[m] = d

                # Sort the data, run fit, etc.
                self.info_data[m] = analysis.info.get(d=d, m=m)

                alternatives, alternatives_sided, \
                    control_types, \
                    hits, choose_right = \
                    experimental_data.filter.control.get_control(d)

                self.control_data[m] = \
                    experimental_data.filter.control.sort_by_cond(
                        alternatives=alternatives,
                        control_types=control_types, hits=hits)

                self.control_sigmoid_data[m] = \
                    experimental_data.filter.control_sigmoid.get(
                        alternatives_sided=alternatives_sided,
                        control_types=control_types, choose_right=choose_right
                    )
                self.control_sig_fit[m] = \
                    {cd: self.control_sigmoid_data[m][cd]['fit']
                     for cd in CONTROL_CONDITIONS}

                self.exemplary_data[m] = \
                    experimental_data.filter.exemplary.get(d)

                self.freq_risk_data[m] = \
                    experimental_data.filter.freq_risk.get(d)
                self.risk_sig_fit[m] = \
                    {cd: self.freq_risk_data[m][cd]['fit']
                     for cd in (GAIN, LOSS)}

                self.cpt_fit[m] = model.parameter_estimate.run(
                    d,
                    monkey=m,
                    force=force_fit,
                    n_chunk=n_chunk,
                    randomize=randomize_chunk_trials)

                #     # Stats for comparison of best parameter values
                #     stats_comparison_best_values(fit, monkey=monkey)

                # Stats for comparison of best parameter values
                self.hist_best_param_data[m] = {
                    'fit': self.cpt_fit[m],
                    'regression':
                        stats_regression_best_values(fit=self.cpt_fit[m])
                }

                # history of performance for control trials
                self.hist_control_data[m] = \
                    experimental_data.filter.control.control_history_sort_data(
                        alternatives=alternatives,
                        control_types=control_types,
                        hits=hits, n_chunk=n_chunk)

            except Exception as e:
                if skip_exception:
                    m = monkeys[i]
                    msg = \
                        f"I encountered exeception '{e}' " \
                        f"while trying to execute for monkey '{m}'." \
                        "I will skip this monkey..."
                    warnings.warn(msg)
                    black_list.append(m)
                else:
                    raise e

        for m in black_list:
            monkeys.remove(m)

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

        # Create the pdf
        self.pdf = PdfPages(os.path.join(
            FIG_FOLDER,
            f"results{monkey if monkey is not None else''}.pdf"))

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
            n_subplot=3)

        # Fig: Exemplary case
        self.create_figure(
            plot_function=plot.exemplary_case.plot,
            data=self.exemplary_data)

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

        # Fig: Control history
        self.create_figure(
            plot_function=plot.history.history_control,
            data=self.hist_control_data,
            n_subplot=len(CONTROL_CONDITIONS))

        # Fig: Best param history
        self.create_figure(
            plot_function=plot.history.history_best_param,
            data=self.hist_best_param_data,
            n_subplot=3)

        self.pdf.close()
        self.target_monkey = None

    def create_summary(self):

        analysis.summary.create(
            info_data=self.info_data,
            control_data=self.control_data,
            cpt_fit=self.cpt_fit,
            control_sig_fit=self.control_sig_fit,
            risk_sig_fit=self.risk_sig_fit)


def main():

    a = Analysis()
    a.create_pdf()
    a.create_summary()
    for m in a.monkeys:
        a.create_pdf(monkey=m)


if __name__ == '__main__':
    main()
