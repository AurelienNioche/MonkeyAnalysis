import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "MonkeyAnalysis.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from experimental_data.get import get_data

from plot.history import history_best_param, history_control
from plot.precision import precision
from plot.probability_distortion import probability_distortion
from plot.utility import utility
from plot.control import control
from plot.freq_risk_against_exp_value import freq_risk_against_exp_value
from plot.exemplary_case import exemplary_case

import model.parameter_estimate
from model.stats import stats_comparison_best_values, \
    stats_regression_best_values, display_table_content


def main(n_chunk=5, randomize_chunk_trials=False, force_fit=True,
         print_latex=False):

    # Get data
    d = get_data()

    # Get fit
    fit = model.parameter_estimate.run(d, force=force_fit,
                                       n_chunk=n_chunk,
                                       randomize=randomize_chunk_trials)

    if print_latex:
        # Print line for latex table
        display_table_content(fit)

    # Stats for comparison of best parameter values
    stats_comparison_best_values(fit)

    # Stats for comparison of best parameter values
    rgr_param = stats_regression_best_values(fit, print_latex=print_latex)

    # Control history figure
    history_control(d, n_chunk=n_chunk)

    # Fig: Exemplary case
    exemplary_case(d)

    # Fig: Control
    control(d)

    # Freq risky choice against expected value
    freq_risk_against_exp_value(d)

    # Fig: History
    history_best_param(fit, regression_param=rgr_param)

    # Fig: Utility function
    utility(fit)

    # Fig: Probability distortion
    probability_distortion(fit)

    # Fig: Precision
    precision(fit)


if __name__ == '__main__':
    main(force_fit=True)
