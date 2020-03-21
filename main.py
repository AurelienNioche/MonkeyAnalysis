import os

import experimental_data.filter.control

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "MonkeyAnalysis.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import matplotlib.backends.backend_pdf

from parameters.parameters import FIG_FOLDER, MODEL_PARAMETERS, \
    CONTROL_CONDITIONS
# from utils.log import log

from experimental_data.get import get_data, get_monkeys
from experimental_data.filter.control import control_history_sort_data

from plot.history import history_best_param, history_control
from plot.precision import precision
from plot.probability_distortion import probability_distortion
from plot.utility import utility
from plot.control import control
from plot.freq_risk_against_exp_value import freq_risk_against_exp_value
from plot.exemplary_case import exemplary_case

import model.parameter_estimate
from model.stats import stats_comparison_best_values, \
    stats_regression_best_values

from plot import info

import numpy as np

import warnings

np.seterr(all='raise')

NAME = "main"


def main(n_chunk=5, starting_point="2020-02-18",
         randomize_chunk_trials=False, force_fit=True,
         skip_exception=False):

    monkeys = get_monkeys()

    results = {
        "choose_right": [],
    }
    for cd in CONTROL_CONDITIONS:
        results[cd] = []

    for pr in MODEL_PARAMETERS:
        results[pr] = []

    for monkey in monkeys:

        try:
            print()
            print("-"*60 + f" {monkey} " + "-"*60 + "\n")

            # A single pdf file for every figure
            pdf = matplotlib.backends.backend_pdf.PdfPages(
                os.path.join(FIG_FOLDER, f"{monkey}_fig.pdf"))

            # Data
            d = get_data(monkey, starting_point=starting_point)
            # # For reproduction:
            # d = get_data(monkey,
            #              starting_point="2017-03-01",
            #              end_point="2019-09-30")

            # Print info
            info.write_pdf(d=d, monkey=monkey, pdf=pdf)

            # Get fit
            fit = model.parameter_estimate.run(
                d,
                monkey=monkey,
                force=force_fit,
                n_chunk=n_chunk,
                randomize=randomize_chunk_trials)

            # Include in summary table
            for pr in MODEL_PARAMETERS:
                results[pr].append(np.mean(fit[pr]))

            # Stats for comparison of best parameter values
            stats_comparison_best_values(fit, monkey=monkey)

            # Stats for comparison of best parameter values
            rgr_param = stats_regression_best_values(fit, monkey=monkey)

            alternatives, control_types, hits = \
                experimental_data.filter.control.get_control(d)

            control_d = \
                experimental_data.filter.control.cluster_hit_by_control_cond(
                    alternatives, control_types, hits)

            for cd in control_types:
                results[cd].append(np.median(list(control_d[cd].values())))

            # Fig: Control
            control(control_d=control_d, monkey=monkey, pdf=pdf)

            # Fig: Exemplary case
            exemplary_case(d, monkey=monkey, pdf=pdf)

            # Freq risky choice against expected value
            freq_risk_against_exp_value(d, monkey=monkey, pdf=pdf)

            # Fig: Utility function
            utility(fit, monkey=monkey, pdf=pdf)

            # Fig: Probability distortion
            probability_distortion(fit, monkey=monkey, pdf=pdf)

            # Fig: Precision
            precision(fit, monkey=monkey, pdf=pdf)

            # Format data
            hist_control_d = \
                control_history_sort_data(alternatives=alternatives,
                                          control_types=control_types,
                                          hits=hits, n_chunk=n_chunk)

            # Fig: Control history
            history_control(hist_control_d=hist_control_d,
                            monkey=monkey, pdf=pdf)

            # Fig: Best param history
            history_best_param(fit, monkey=monkey,
                               regression_param=rgr_param,
                               pdf=pdf)

            pdf.close()

        except Exception as e:
            if skip_exception:
                msg = \
                    f"I encountered exeception '{e}' " \
                    f"while trying to execute for monkey '{monkey}'." \
                    "I will skip this monkey..."
                warnings.warn(msg, name=NAME)
            else:
                raise e

        break


if __name__ == '__main__':
    main(force_fit=True)
