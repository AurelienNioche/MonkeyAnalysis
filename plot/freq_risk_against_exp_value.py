import numpy as np
from scipy.optimize import curve_fit

from utils.utils import log

from scipy.stats.distributions import t

""" 
Produce the figure which presents at which extent 
the risky option was chosen according to the difference between expected values
"""

name = "freq_risk_against_exp_value"


def sigmoid(x, x0, k):
    y = 1 / (1 + np.exp(-k * (x - x0)))
    return y


def sigmoid_one_param(x, theta):
    # Activation function used to map any real value between 0 and 1
    return 1 / (1 + np.exp(-theta * x))


def stats(y, p_opt, p_cov, alpha=0.05):  # 95% confidence interval = 100*(1-alpha)

    n = len(y)  # number of data points
    p = len(p_opt)  # number of parameters

    # print(n, p)

    dof = max(0, n - p)  # number of degrees of freedom

    # student-t value for the dof and confidence level
    tval = t.ppf(1.0 - alpha / 2., dof)

    log(f"student-t value: {tval:.2f}", name=name)

    p_err = np.sqrt(np.diag(p_cov))

    for i, p, std in zip(range(n), p_opt, p_err):

        me = std * tval
        log(f'p{i}: {p:.2f} [{p - me:.2f}  {p + me:.2f}]', name=name)


def plot(expected_values_differences, risky_choice_means, color, ax, f=sigmoid):

    line_width = 3
    axis_label_font_size = 20
    ticks_label_font_size = 14
    point_size = 100

    x_data = expected_values_differences
    y_data = risky_choice_means

    # ####### TO REMOVE AFTERWARDS ######## #
    # import scipy.stats
    # slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x_data, y_data)
    # print(r_value, p_value)
    # ##################################### #

    try:

        # Fit sigmoid
        p_opt, p_cov = curve_fit(f, x_data, y_data)

        # Do stats about fit
        stats(y=y_data, p_cov=p_cov, p_opt=p_opt)

        # Plot
        n_points = 50  # Arbitrary neither too small, or too large
        x = np.linspace(min(x_data), max(x_data), n_points)
        y = f(x, *p_opt)

        ax.plot(x, y, color=color, linewidth=line_width)

    except RuntimeError as e:
        log(e)

    ax.scatter(x_data, y_data, color=color, alpha=0.5, s=point_size)

    ax.axhline(0.5, alpha=0.5, linewidth=1, color='black', linestyle='--', zorder=-10)
    ax.axvline(0, alpha=0.5, linewidth=1, color='black', linestyle='--', zorder=-10)

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
