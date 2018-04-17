import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from utils.utils import log

""" 
Produce the figure which presents at which extent 
the risky option was chosen according to the difference between expected values
"""


def sigmoid(x, x0, k):
    y = 1 / (1 + np.exp(-k * (x - x0)))
    return y


def plot(expected_values_differences, risky_choice_means, color,
         fig_name=None, subplot_spec=None, fig=None):

    if None in (subplot_spec, fig):
        fig = plt.figure()
        ax = fig.add_subplot()

    else:
        ax = fig.add_subplot(subplot_spec)

    line_width = 3
    axis_label_font_size = 20
    ticks_label_font_size = 14
    point_size = 100

    x_data = expected_values_differences
    y_data = risky_choice_means

    try:

        p_opt, p_cov = curve_fit(sigmoid, x_data, y_data)

        n_points = 50  # Arbitrary neither too small, or too large
        x = np.linspace(min(x_data), max(x_data), n_points)
        y = sigmoid(x, *p_opt)
        ax.plot(x, y, color=color, label='fit', linewidth=line_width)

    except RuntimeError as e:
        log(e)

    ax.scatter(x_data, y_data, color=color, label='data', s=point_size)

    ax.set_ylim(-0.01, 1.01)

    # Axis labels
    ax.set_xlabel(
        "$EV_{\mathrm{Riskiest\,option}} - EV_{\mathrm{Safest\,option}}$",
        fontsize=axis_label_font_size)
    ax.set_ylabel(
        "F(Choose riskiest option)",
        fontsize=axis_label_font_size)

    # Remove top and right borders
    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_color('none')

    ax.tick_params(axis='both', which='major', labelsize=ticks_label_font_size)
    ax.tick_params(axis='both', which='minor', labelsize=ticks_label_font_size)

    if fig_name:
        plt.tight_layout()
        plt.savefig(fname=fig_name)
        plt.close()
