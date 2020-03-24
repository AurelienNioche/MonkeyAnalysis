"""
Produce the figure which presents at which extent
the risky option was chosen according to the difference
between expected values,
i.e. the certainty-risk trade-off figure
"""

import matplotlib.pyplot as plt

from experimental_data.filter.risk import get_choose_risky_loss_or_gain_only
from sigmoid_fit.sigmoid_fit import sigmoid_fit

from utils.log import log
from plot.utils import save_fig

from parameters.parameters import \
    COLOR_LOSS, COLOR_GAIN, FIG_FREQ_RISK_AGAINST_EXP_VALUE


NAME = "plot.freq_risk_against_exp_value"


def _plot(expected_values_differences, risky_choice_means, color, ax,
          label=None):

    line_width = 3
    axis_label_font_size = 20
    ticks_label_font_size = 14
    point_size = 100

    x_data = expected_values_differences
    y_data = risky_choice_means

    if label is not None:
        label = label.capitalize()

    stats_r = None
    try:

        x, y, stats_r = sigmoid_fit(x_data=x_data, y_data=y_data)

        ax.plot(x, y, color=color, linewidth=line_width, label=label)
        ax.legend()

    except RuntimeError as e:
        log(e, NAME)

    ax.scatter(x_data, y_data, color=color, alpha=0.5, s=point_size)

    ax.axhline(0.5, alpha=0.5, linewidth=1, color='black',
               linestyle='--', zorder=-10)
    ax.axvline(0, alpha=0.5, linewidth=1, color='black',
               linestyle='--', zorder=-10)

    ax.set_ylim(-0.01, 1.01)
    ax.set_yticks((0, 0.5, 1))

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

    return stats_r


def freq_risk_against_exp_value(d, monkey, pdf=None):

    print()

    fig, ax = plt.subplots(figsize=(6, 5), dpi=200)

    stats_slope = {}

    for i, gain_only in enumerate((1, 0)):

        cond = 'gain' if gain_only else 'loss'

        log(f"{monkey} "
            f"- Stats for risk against exp value "
            f"- {cond}:", name=NAME)

        expected_values_differences, risky_choice_means = \
            get_choose_risky_loss_or_gain_only(
                d, gain_only=gain_only)

        color = (COLOR_LOSS, COLOR_GAIN)[gain_only]

        stats_r = _plot(
            expected_values_differences=expected_values_differences,
            risky_choice_means=risky_choice_means,
            color=color,
            ax=ax,
            label=cond
        )

        stats_slope[cond] = stats_r[-1]

    txt = r"$F(x) = \dfrac{1}{1 + \exp(-k (x - x_0))}$" + "\n\n"
    for cond in ('gain', 'loss'):
        txt += r"$k_{" + f"{cond}" + "}=" + \
               f"{stats_slope[cond]['val']:.2f}\," \
               f"[{stats_slope[cond]['ic-']:.2f}, " \
               f"{stats_slope[cond]['ic+']:.2f}]" + "$\n"

    ax.text(0.05, 0.9, txt,
            horizontalalignment='left',
            verticalalignment='center',
            transform=ax.transAxes)

    save_fig(fig_type=FIG_FREQ_RISK_AGAINST_EXP_VALUE,
             fig=fig, pdf=pdf, monkey=monkey)
