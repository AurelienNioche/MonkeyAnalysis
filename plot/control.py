"""
Produce the control figures
"""

import matplotlib.gridspec
import numpy as np
from matplotlib import pyplot as plt
import string

import experimental_data.filter

from utils.utils import log

from parameters.parameters import FIG_CONTROL, COLOR_GAIN, COLOR_LOSS

NAME = "plot.control"


def _plot(results, ax, letter=None):

    n = len(results.keys())

    tick_labels = [
        "Loss\nvs\ngains", "Diff. $x +$\nSame $p$", "Diff. $x -$\nSame $p$",
        "Diff. $p$\nSame $x +$", "Diff. $p$\nSame $x -$"]

    colors = ["black", COLOR_GAIN, COLOR_LOSS, COLOR_GAIN, COLOR_LOSS]
    positions = list(range(n))

    x_scatter = []
    y_scatter = []
    colors_scatter = []

    values_box_plot = []

    for i, cond in enumerate(results.keys()):

        values_box_plot.append([])

        for v in results[cond].values():
            # For box plot
            values_box_plot[-1].append(v)

            # For scatter
            y_scatter.append(v)
            x_scatter.append(i)
            colors_scatter.append(colors[i])

    fontsize = 10

    ax.scatter(x_scatter, y_scatter, c=colors_scatter, s=30, alpha=0.5,
               linewidth=0.0, zorder=1)

    ax.axhline(0.5, linestyle='--', color='0.3', zorder=-10, linewidth=0.5)

    ax.set_yticks(np.arange(0.4, 1.1, 0.2))

    ax.tick_params(axis='both', labelsize=fontsize)

    ax.set_ylabel("Success rate", fontsize=fontsize)

    ax.set_ylim(0.35, 1.02)

    # Boxplot
    bp = ax.boxplot(values_box_plot, positions=positions, labels=tick_labels,
                    showfliers=False, zorder=2)

    # Warning: only one box, but several whiskers by plot
    for e in ['boxes', 'caps', 'whiskers', 'medians']:
        for b in bp[e]:
            b.set(color='black')
            # b.set_alpha(1)

    ax.set_aspect(3)

    ax.text(
        s=letter, x=-0.1, y=-0.1, horizontalalignment='center',
        verticalalignment='center', transform=ax.transAxes,
        fontsize=25)


def control(d):

    monkeys = sorted(d.keys())
    n_monkey = len(monkeys)

    n_rows, n_cols = n_monkey, 1
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(4.7, 5.4), dpi=200)
    axes = [fig.add_subplot(gs[i, 0]) for i in range(len(monkeys))]

    for i, monkey in enumerate(monkeys):

        log(f"Stats for control trials - {monkey}:", NAME)

        alternatives, control_types, hits = experimental_data.filter.get_control(d[monkey])
        control_d = experimental_data.filter.cluster_hit_by_control_cond(
            alternatives, control_types, hits)

        _plot(results=control_d, ax=axes[i],
              letter=string.ascii_uppercase[i])

    log(f"Creating figure '{FIG_CONTROL}'...",
        name=NAME)

    gs.tight_layout(fig)

    fig.savefig(fname=FIG_CONTROL)
    log(f"Done!\n", NAME)
