"""
Produce the the certainty-risk trade-off figure
"""
import matplotlib.gridspec
from matplotlib import pyplot as plt

import experimental_data.filter
from parameters.parameters import COLOR_GAIN, COLOR_LOSS, FIG_EXEMPLARY_CASE
from utils.utils import log


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


def exemplary_case(d):

    monkeys = sorted(d.keys())

    n_rows, n_cols = 1, 2
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)
    fig = plt.figure(figsize=(12, 5), dpi=200)
    axes = [fig.add_subplot(gs[0, i]) for i in range(len(monkeys))]

    for i, monkey in enumerate(monkeys):

        log(f"Creating figure 'exemplary_case' for {monkey}...",
            name=NAME)

        ex_d = experimental_data.filter.get_exemplary_case(d[monkey])

        _plot(
            results=ex_d,
            color_gain=COLOR_GAIN,
            color_loss=COLOR_LOSS,
            ax=axes[i])

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()
    ax.text(
        s='A', x=0, y=0, horizontalalignment='center',
        verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s='B', x=0.5, y=0, horizontalalignment='center',
        verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    gs.tight_layout(fig)
    fig.savefig(fname=FIG_EXEMPLARY_CASE)
