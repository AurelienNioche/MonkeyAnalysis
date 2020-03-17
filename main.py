import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "MonkeyAnalysis.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from parameters.parameters import FIG_FOLDER
from utils.log import log

from experimental_data.get import get_data, get_monkeys

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

import matplotlib.backends.backend_pdf

from plot import info

import numpy as np

import warnings

np.seterr(all='raise')

NAME = "main"


def main(n_chunk=5, randomize_chunk_trials=False, force_fit=True,
         skip_exception=False):

    monkeys = get_monkeys()

    for monkey in monkeys:

        try:
            print()
            print("-"*60 + f" {monkey} " + "-"*60 + "\n")

            # A single pdf file for every figure
            pdf = matplotlib.backends.backend_pdf.PdfPages(
                os.path.join(FIG_FOLDER, f"{monkey}_fig.pdf"))

            # Data
            d = get_data(monkey)
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

            # Stats for comparison of best parameter values
            stats_comparison_best_values(fit, monkey=monkey)

            # Stats for comparison of best parameter values
            rgr_param = stats_regression_best_values(fit, monkey=monkey)

            # Fig: Control
            control(d, monkey=monkey, pdf=pdf)

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

            # Fig: Control history
            history_control(d, monkey=monkey, n_chunk=n_chunk, pdf=pdf)

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


if __name__ == '__main__':
    main(force_fit=True)
