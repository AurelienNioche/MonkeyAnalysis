"""
Produce the figure which presents at which extent
the risky option was chosen according to the difference
between expected values,
i.e. the certainty-risk trade-off figure
"""

import matplotlib.gridspec
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

import data.filter

from utils.utils import log

from scipy.stats.distributions import t

from parameters.parameters import \
    COLOR_LOSS, COLOR_GAIN, FIG_FREQ_RISK_AGAINST_EXP_VALUE


NAME = "plot.freq_risk_against_exp_value"


def sigmoid(x, x0, k):
    y = 1 / (1 + np.exp(-k * (x - x0)))
    return y


def sigmoid_one_param(x, theta):
    # Activation function used to map any real value between 0 and 1
    return 1 / (1 + np.exp(-theta * x))


def stats(y, p_opt, p_cov, alpha=0.01):
    # 95% confidence interval = 100*(1-alpha)

    n = len(y)  # number of data points
    p = len(p_opt)  # number of parameters

    # print(n, p)

    dof = max(0, n - p)  # number of degrees of freedom

    # student-t value for the dof and confidence level
    tval = t.ppf(1.0 - alpha / 2., dof)

    log(f"student-t value: {tval:.2f}", name=NAME)

    p_err = np.sqrt(np.diag(p_cov))

    for i, p, std in zip(range(n), p_opt, p_err):

        me = std * tval
        log(f'p{i}: {p:.2f} [{p - me:.2f}  {p + me:.2f}]', name=NAME)


def _plot(expected_values_differences, risky_choice_means, color, ax,
          f=sigmoid):

    line_width = 3
    axis_label_font_size = 20
    ticks_label_font_size = 14
    point_size = 100

    x_data = expected_values_differences
    y_data = risky_choice_means

    # ####### TO REMOVE AFTERWARDS ######## #
    # import scipy.stats
    # slope, intercept, r_value, p_value, std_err =
    # scipy.stats.linregress(x_data, y_data)
    # print(r_value, p_value)
    # ##################################### #

    try:

        # Fit sigmoid
        p_opt, p_cov = curve_fit(f, x_data, y_data,
                                 maxfev=10000)

        # Do stats about fit
        stats(y=y_data, p_cov=p_cov, p_opt=p_opt)

        # Plot
        n_points = 50  # Arbitrary neither too small, or too large
        x = np.linspace(min(x_data), max(x_data), n_points)
        y = f(x, *p_opt)

        ax.plot(x, y, color=color, linewidth=line_width)

    except RuntimeError as e:
        log(e, NAME)

    ax.scatter(x_data, y_data, color=color, alpha=0.5, s=point_size)

    ax.axhline(0.5, alpha=0.5, linewidth=1, color='black',
               linestyle='--', zorder=-10)
    ax.axvline(0, alpha=0.5, linewidth=1, color='black',
               linestyle='--', zorder=-10)

    ax.set_ylim(-0.01, 1.01)

    # Axis labels
    ax.set_xlabel(
        r"$EV_{\mathrm{Riskiest\,option}} - EV_{\mathrm{Safest\,option}}$",
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


def freq_risk_against_exp_value(d, f=sigmoid):

    monkeys = sorted(d.keys())

    n_rows, n_cols = 2, 2
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)
    fig = plt.figure(figsize=(12, 10), dpi=200)
    axes = [[] for _ in range(n_cols)]
    for i in range(len(monkeys)):
        for j in range(2):
            axes[i].append(fig.add_subplot(gs[i, j]))

    for i, monkey in enumerate(monkeys):

        log(f"Creating figure 'freq_risk_against_exp_value' for {monkey}...",
            name=NAME)

        for j, gain_only in enumerate((1, 0)):

            expected_values_differences, risky_choice_means = \
                data.filter.get_choose_risky_loss_or_gain_only(
                    d[monkey], gain_only=gain_only)

            color = (COLOR_LOSS, COLOR_GAIN)[gain_only]

            _plot(
                expected_values_differences=expected_values_differences,
                risky_choice_means=risky_choice_means,
                color=color,
                ax=axes[i][j],
                f=f
            )

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()
    ax.text(
        s='A', x=-0.05, y=0.5, horizontalalignment='center',
        verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s='B', x=-0.05, y=-0.1, horizontalalignment='center',
        verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    gs.tight_layout(fig)
    fig.savefig(fname=FIG_FREQ_RISK_AGAINST_EXP_VALUE)
