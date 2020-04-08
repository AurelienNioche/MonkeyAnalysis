"""
Produce the control figures
"""

import numpy as np

from parameters.parameters import COLOR_GAIN, COLOR_LOSS

NAME = "plot.control"


def plot(ax, control_d):

    n = len(control_d.keys())

    tick_labels = [
        "Loss\nvs\ngains", "Diff. $x +$\nSame $p$", "Diff. $x -$\nSame $p$",
        "Diff. $p$\nSame $x +$", "Diff. $p$\nSame $x -$"]

    colors = ["black", COLOR_GAIN, COLOR_LOSS, COLOR_GAIN, COLOR_LOSS]
    positions = list(range(n))

    x_scatter = []
    y_scatter = []
    colors_scatter = []

    values_box_plot = []

    for i, cond in enumerate(control_d.keys()):

        values_box_plot.append([])

        for v in control_d[cond].values():
            # For box plot
            values_box_plot[-1].append(v)

            # For scatter
            y_scatter.append(v)
            x_scatter.append(i + np.random.uniform(-0.025*n, 0.025*n))
            colors_scatter.append(colors[i])

    fontsize = 10

    ax.scatter(x_scatter, y_scatter, c=colors_scatter, s=50, alpha=0.5,
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


# def control(control_d, monkey, pdf=None):
#
#     log(f"Stats for control trials - {monkey}:", NAME)
#
#     fig, ax = plt.subplots(figsize=(12, 6), dpi=200)
#
#     _plot(control_d=control_d, ax=ax)
#
#     save_fig(fig_type=FIG_CONTROL, fig=fig, pdf=pdf, monkey=monkey)
