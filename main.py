import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "MonkeyAnalysis.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

from parameters.parameters import FIG_FOLDER, MODEL_PARAMETERS, \
    CONTROL_CONDITIONS, CHOOSE_RIGHT, MONKEY_NAME, N_TRIALS, \
    CONTROL_SIG_PARAM, RISK_SIG_PARAM
# from utils.log import log

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

import model.parameter_estimate
from model.stats import stats_regression_best_values
# from model.stats import stats_comparison_best_values

import analysis.summary
import analysis.info

from plot import info

import numpy as np

import warnings

np.seterr(all='raise')

NAME = "main"


def main(n_chunk=5, starting_point="2020-02-18",
         randomize_chunk_trials=False, force_fit=True,
         skip_exception=True):

    monkeys = get_monkeys()
    n_monkey = len(monkeys)

    data = {}

    info_data = {}
    control_data = {}
    exemplary_data = {}
    freq_risk_data = {}
    hist_best_param_data = {}
    hist_control_data = {}
    control_sigmoid_data = {}

    cpt_fit = {}
    risk_sig_fit = {}
    control_sig_fit = {}

    black_list = []

    for i in range(n_monkey):

        try:

            m = monkeys[i]

            print()
            print("-"*60 + f" {m} " + "-"*60 + "\n")

            # Pre-process data --------------------------------

            # Get the data
            d = get_data(m, starting_point=starting_point)
            data[m] = d

            # Sort the data, run fit, etc.
            info_data[m] = analysis.info.get(d=d)

            alternatives, alternatives_sided, \
                control_types, \
                hits, choose_right = \
                experimental_data.filter.control.get_control(d)

            control_data[m] = \
                experimental_data.filter.control.cluster_hit_by_control_cond(
                    alternatives, control_types, hits)

            control_sigmoid_data[m] = \
                experimental_data.filter.control_sigmoid.get(
                    alternatives=alternatives,
                    control_types=control_types, choose_right=choose_right
                )
            control_sig_fit[m] = control_sigmoid_data[m]['fit']

            exemplary_data[m] = experimental_data.filter.exemplary.get(d)

            freq_risk_data[m] = experimental_data.filter.freq_risk.get(d)
            risk_sig_fit[m] = freq_risk_data[m]['fit']

            cpt_fit[m] = model.parameter_estimate.run(
                d,
                monkey=m,
                force=force_fit,
                n_chunk=n_chunk,
                randomize=randomize_chunk_trials)

            #     # Stats for comparison of best parameter values
            #     stats_comparison_best_values(fit, monkey=monkey)

            # Stats for comparison of best parameter values
            hist_best_param_data[m] = \
                stats_regression_best_values(fit=cpt_fit[m])

            # history of performance for control trials
            hist_control_data[m] = \
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

    n_monkey = len(monkeys)

    # A single pdf file for everything
    with PdfPages(os.path.join(FIG_FOLDER, "exemplary_d.pdf")) as pdf:

        # Fig: Info
        fig, axes = plt.subplots(ncols=n_monkey, figsize=(6*n_monkey, 6))

        for i in range(n_monkey):
            m = monkeys[i]
            ax = axes[i]
            info.fig_info(ax=ax, info=info_data[m], monkey=m)
        plt.tight_layout()
        pdf.savefig(fig)
        # plt.close(fig)

        # Fig: Control
        fig, axes = plt.subplots(ncols=n_monkey, figsize=(6*n_monkey, 6))

        for i in range(n_monkey):
            # Fig: Control
            m = monkeys[i]
            ax = axes[i]
            control_d = control_data[m]

            plot.control.plot(ax=ax, control_d=control_d)

        plt.tight_layout()
        pdf.savefig(fig)

        # Fig: Control sigmoid
        n_rows = 3
        fig, axes = plt.subplots(ncols=n_monkey, nrows=n_rows,
                                 figsize=(6*n_monkey, 6*n_rows))

        for i in range(n_monkey):
            m = monkeys[i]
            _axes = axes[:, i]
            plot.control_sigmoid.control_sigmoid(
                axes=_axes, **control_sigmoid_data[m])

        plt.tight_layout()
        pdf.savefig(fig)

        # Fig: Exemplary case
        fig, axes = plt.subplots(ncols=n_monkey,
                                 figsize=(6*n_monkey, 6))

        for i in range(n_monkey):
            m = monkeys[i]
            ax = axes[i]

            plot.exemplary_case.plot(ax=ax, exemplary_d=exemplary_data[m])

        plt.tight_layout()
        pdf.savefig(fig)

        # Fig: Freq risky choice against expected value
        fig, axes = plt.subplots(ncols=n_monkey,
                                 figsize=(6*n_monkey, 6))

        for i in range(n_monkey):
            m = monkeys[i]
            ax = axes[i]
            plot.freq_risk.plot(ax=ax, **freq_risk_data[m])

        plt.tight_layout()
        pdf.savefig(fig)

        # Fig: Utility function
        fig, axes = plt.subplots(ncols=n_monkey,
                                 figsize=(6*n_monkey, 6))

        for i in range(n_monkey):
            m = monkeys[i]
            ax = axes[i]
            plot.utility.plot(ax=ax, fit=cpt_fit[m])

        plt.tight_layout()
        pdf.savefig(fig)

        # Fig: Probability distortion
        fig, axes = plt.subplots(ncols=n_monkey,
                                 figsize=(6*n_monkey, 6))

        for i in range(n_monkey):
            m = monkeys[i]
            ax = axes[i]
            plot.probability_distortion.plot(ax=ax, fit=cpt_fit[m])

        plt.tight_layout()
        pdf.savefig(fig)

        # Fig: Precision
        fig, axes = plt.subplots(ncols=n_monkey,
                                 figsize=(6*n_monkey, 6))

        for i in range(n_monkey):
            m = monkeys[i]
            ax = axes[i]
            plot.precision.plot(ax=ax, fit=cpt_fit[m])

        plt.tight_layout()
        pdf.savefig(fig)

        # Fig: Control history
        n_rows = len(CONTROL_CONDITIONS)
        fig, axes = plt.subplots(ncols=n_monkey, nrows=n_rows,
                                 figsize=(6*n_monkey, 6*n_rows))

        for i in range(n_monkey):
            m = monkeys[i]
            _axes = axes[:, i]
            plot.history.history_control(axes=_axes,
                                         hist_control_d=hist_control_data[m])

        plt.tight_layout()
        pdf.savefig(fig)

        # Fig: Best param history
        n_rows = 3
        fig, axes = plt.subplots(ncols=n_monkey, nrows=n_rows,
                                 figsize=(6*n_monkey, 6*n_rows))

        for i in range(n_monkey):
            m = monkeys[i]
            _axes = axes[:, i]
            plot.history.history_best_param(
                axes=_axes, fit=cpt_fit[m],
                regression_param=hist_best_param_data[m])

        plt.tight_layout()
        pdf.savefig(fig)

    # Do summary ------------------------------------------
    summary = analysis.summary.create()

    for m in monkeys:

        # Add monkey name
        summary[MONKEY_NAME].append(m)

        # Add number of trials
        summary[N_TRIALS].append(info_data[m].n_trials)

        # Add side bias
        summary[CHOOSE_RIGHT].append(info_data[m].choose_right)

        # Add median for each type of control
        summary.append_performance_to_control(control_data[m])

        # Include best-fit parameters
        summary.append_cpt_fit(cpt_fit[m])
        summary.append_control_sig_fit(control_sig_fit[m])
        summary.append_risk_sig_fit(risk_sig_fit[m])

        #
        #     # Fig: Utility function
        #     utility(fit, monkey=monkey, pdf=pdf)
        #
        #     # Fig: Probability distortion
        #     probability_distortion(fit, monkey=monkey, pdf=pdf)
        #
        #     # Fig: Precision
        #     precision(fit, monkey=monkey, pdf=pdf)
        #
        #     # Fig: Control history
        #     history_control(hist_control_d=hist_control_d,
        #                     monkey=monkey, pdf=pdf)
        #
        #     # Fig: Best param history
        #     history_best_param(fit, monkey=monkey,
        #                        regression_param=rgr_param,
        #                        pdf=pdf)

            # # For reproduction:
            # d = get_data(monkey,
            #              starting_point="2017-03-01",
            #              end_point="2019-09-30")
            #
            # Get basic info


        #     # Get fit
        #     fit = model.parameter_estimate.run(
        #         d,
        #         monkey=monkey,
        #         force=force_fit,
        #         n_chunk=n_chunk,
        #         randomize=randomize_chunk_trials)
        #
        #     # Stats for comparison of best parameter values
        #     stats_comparison_best_values(fit, monkey=monkey)
        #
        #     # Stats for comparison of best parameter values
        #     rgr_param = stats_regression_best_values(fit, monkey=monkey)
        #
        #     # Preprocess data for control trials
        #     alternatives, alternatives_sided, \
        #         control_types, \
        #         hits, choose_right = \
        #         experimental_data.filter.control.get_control(d)
        #
        #     control_d = \
        #         experimental_data.filter.control.cluster_hit_by_control_cond(
        #             alternatives, control_types, hits)
        #
        #     # Preprocess data for history of performance for control trials
        #     hist_control_d = \
        #         control_history_sort_data(alternatives=alternatives,
        #                                   control_types=control_types,
        #                                   hits=hits, n_chunk=n_chunk)
        #
        #     # Do the figures ----------------------------------------
        #
        #
        #     # Fig: Info
        #     info.write_pdf(info=basic_info, monkey=monkey, pdf=pdf)
        #
        #     # Fig: Control
        #     control(control_d=control_d, monkey=monkey, pdf=pdf)
        #
        #     # Fig: Control sigmoid
        #     control_sig_fit = control_sigmoid(
        #         alternatives=alternatives_sided,
        #         control_types=control_types,
        #         choose_right=choose_right, monkey=monkey,
        #         pdf=pdf)
        #
        #     # Fig: Exemplary case
        #     exemplary_case(d, monkey=monkey, pdf=pdf)
        #
        #     # Fig: Freq risky choice against expected value
        #     risk_sig_fit = \
        #         freq_risk_against_exp_value(d, monkey=monkey, pdf=pdf)
        #
        #     # Fig: Utility function
        #     utility(fit, monkey=monkey, pdf=pdf)
        #
        #     # Fig: Probability distortion
        #     probability_distortion(fit, monkey=monkey, pdf=pdf)
        #
        #     # Fig: Precision
        #     precision(fit, monkey=monkey, pdf=pdf)
        #
        #     # Fig: Control history
        #     history_control(hist_control_d=hist_control_d,
        #                     monkey=monkey, pdf=pdf)
        #
        #     # Fig: Best param history
        #     history_best_param(fit, monkey=monkey,
        #                        regression_param=rgr_param,
        #                        pdf=pdf)
        #
        #     pdf.close()
        #
        #     # Do summary ------------------------------------------
        #
        #     # Add monkey name
        #     summary[MONKEY_NAME].append(monkey)
        #
        #     # Add number of trials
        #     summary[N_TRIALS].append(basic_info.n_trials)
        #
        #     # Add side bias
        #     summary[CHOOSE_RIGHT].append(basic_info.choose_right)
        #
        #     # Add median for each type of control
        #     for cd in CONTROL_CONDITIONS:
        #         median = np.median(list(control_d[cd].values()))
        #         summary[cd].append(median)
        #
        #     # Include best-fit parameters
        #     for pr in MODEL_PARAMETERS:
        #         mean = np.mean(fit[pr])
        #         summary[pr].append(mean)
        #
        #     for pr in CONTROL_SIG_PARAM:
        #         summary[pr].append(control_sig_fit[pr])
        #
        #     for pr in RISK_SIG_PARAM:
        #         summary[pr].append(risk_sig_fit[pr])
        #
        # except Exception as e:
        #     if skip_exception:
        #         msg = \
        #             f"I encountered exeception '{e}' " \
        #             f"while trying to execute for monkey '{monkey}'." \
        #             "I will skip this monkey..."
        #         warnings.warn(msg)
        #     else:
        #         raise e

    # summary.export_as_xlsx()


if __name__ == '__main__':
    main()
