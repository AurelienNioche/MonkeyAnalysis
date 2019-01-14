import os
import matplotlib.gridspec
import matplotlib.pyplot as plt
import numpy as np

import model.parameter_estimate

import plot.utility
import plot.precision
import plot.probability_distortion
import plot.control
import plot.exemplary_case
import plot.freq_risk_against_exp_value

import data.get
import data.filter

from utils.utils import today, log

from main import get_data, utility_multi

name = "Supp"

monkeys = 'Havane', 'Gladys'
color_loss, color_gain = 'C1', 'C0'
fig_folder = 'fig'


def main(force_data_import=False, force_fit=False):

    # Create fig folder
    os.makedirs(fig_folder, exist_ok=True)

    # Get data
    d = get_data(force_data_import)

    # Get fit
    fit = model.parameter_estimate.run_cross_validation(d, force_fit, randomize=False)

    # Utility
    utility_multi(fit=fit, fig_name='utility_not_random_order', ordered_chunks=True, show_average=False)


if __name__ == '__main__':
    main(False, False)
