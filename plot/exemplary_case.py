"""
Produce the the certainty-risk trade-off figure
"""

import matplotlib.pyplot as plt

import experimental_data.filter
from parameters.parameters import COLOR_GAIN, COLOR_LOSS, FIG_EXEMPLARY_CASE

from utils.log import log
from plot.utils import save_fig


NAME = "plot.exemplary_case"


def _plot(results, color_gain, color_loss, ax):

    axis_label_font_size = 14
    ticks_font_size = 14

    names = "Gain", "Loss"

    ax.scatter(names, (results["gains"], results["losses"]),
               color=(color_gain, color_loss), s=80, zorder=2)

    ax.plot(names, (results["gains"], results["losses"]), color="black",
            zorder=1, alpha=0.5, linestyle='--')
    ax.set_xlabel("\nLotteries potential outputs",
                  fontsize=axis_label_font_size)

    ax.tick_params(axis='both', labelsize=ticks_font_size)

    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_ylabel(
        "F(Choose riskiest option)",
        fontsize=axis_label_font_size)

    ax.set_aspect(2)


def exemplary_case(d, monkey, pdf=None):

    fig, ax = plt.subplots(figsize=(6, 5), dpi=200)

    log(f"Stats for exemplary case - {monkey}...",
        name=NAME)

    ex_d = experimental_data.filter.get_exemplary_case(d)
    if ex_d is None:
        log(f"[{NAME}] "
            f"No data available I can not plot '{FIG_EXEMPLARY_CASE}'.",
            name="WARNING")
        return

    _plot(
        results=ex_d,
        color_gain=COLOR_GAIN,
        color_loss=COLOR_LOSS,
        ax=ax
    )

    save_fig(fig_type=FIG_EXEMPLARY_CASE, fig=fig, pdf=pdf, monkey=monkey)
