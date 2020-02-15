import matplotlib.gridspec
import numpy as np
from matplotlib import pyplot as plt
import string

import experimental_data.filter

from experimental_data.filter import control_history_sort_data
from utils.utils import log

from parameters.parameters import FIG_HISTORY_CONTROL,\
    FIG_HISTORY_BEST_PARAM, \
    COLOR_LOSS, COLOR_GAIN

NAME = "plot.history"


def _plot_history_best_param(
        pos_param, neg_param, ax, y_lim, param_name, show_mid_line=False,
        axis_label_font_size=20,
        ticks_label_font_size=14,
        point_size=100):

    x_data = np.arange(len(pos_param)) + 1
    y_data_gain = pos_param
    y_data_loss = neg_param

    ax.scatter(x_data, y_data_gain, color=COLOR_GAIN, alpha=0.5, s=point_size)
    ax.scatter(x_data, y_data_loss, color=COLOR_LOSS, alpha=0.5, s=point_size)

    if show_mid_line:
        ax.axhline(0, alpha=0.5, linewidth=1, color='black', linestyle='--',
                   zorder=-10)

    ax.set_xlim((0.5, len(x_data)+0.5))
    ax.set_ylim(y_lim)

    if len(x_data) >= 10:
        ax.set_xticks((1, len(x_data)//2, len(x_data)))

    # Axis labels
    ax.set_xlabel(
        "time",
        fontsize=axis_label_font_size)
    ax.set_ylabel(
        param_name,
        fontsize=axis_label_font_size)

    # Remove top and right borders
    # ax.spines['right'].set_color('none')
    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')
    # ax.spines['bottom'].set_position(('data', 0))
    # ax.spines['top'].set_color('none')

    ax.tick_params(axis='both', which='major', labelsize=ticks_label_font_size)
    ax.tick_params(axis='both', which='minor', labelsize=ticks_label_font_size)


def _plot_history_control(results, color, ax, last=False, letter=None,
                          ylabel="Success rate", title="Title", fontsize=5):
    """
    Called by 'control history'
    """

    # results is a list (n=number of boxplot) of list (n=number of datapoints)
    n = len(results)

    tick_labels = [f"{i + 1}" for i in range(n)]

    # colors = ["black", color_gain, color_loss, color_gain, color_loss]
    positions = list(range(n))

    x_scatter = []
    y_scatter = []

    values_box_plot = []

    for i, res in enumerate(results):
        values_box_plot.append([])

        for v in results[i].values():

            # For box plot
            values_box_plot[-1].append(v)

            # For scatter
            y_scatter.append(v)
            x_scatter.append(i)

    assert len(x_scatter) == len(y_scatter)
    ax.scatter(x_scatter, y_scatter, c=color, s=10, alpha=0.5,
               linewidth=0.0, zorder=1)

    ax.axhline(0.5, linestyle='--', color='0.3', zorder=-10, linewidth=0.5)
    ax.set_yticks(np.arange(0.0, 1.1, 0.5))
    ax.tick_params(axis='both', labelsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_ylim(-0.02, 1.02)

    # Boxplot
    bp = ax.boxplot(values_box_plot, positions=positions,
                    labels=tick_labels, showfliers=False, zorder=2)

    # Warning: only one box, but several whiskers by plot
    for e in ['boxes', 'caps', 'whiskers', 'medians']:
        for b in bp[e]:
            b.set(color='black')
            # b.set_alpha(1)

    if not last:
        ax.tick_params(
            axis='x',  # changes apply to the x-axis
            which='both',  # both major and minor ticks are affected
            bottom=False,  # ticks along the bottom edge are off
            top=False,  # ticks along the top edge are off
            labelbottom=False)  # labels along the bottom edge are off

    else:
        ax.set_xlabel('Chunk', fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize+1)

    if letter is not None:
        pass
        # ax.text(
        #     s=letter, x=-0.3, y=-0.4, horizontalalignment='center',
        #     verticalalignment='center', transform=ax.transAxes,
        #     fontsize=20)


def history_control(d, n_chunk,
                    labels=("Loss vs gains", "Diff. $x +$, same $p$",
                            "Diff. $x -$, same $p$",
                            "Diff. $p$, same $x +$", "Diff. $p$, same $x -$"),
                    colors=("black", COLOR_GAIN, COLOR_LOSS, COLOR_GAIN,
                            COLOR_LOSS)):

    monkeys = sorted(d.keys())

    n_monkey = len(monkeys)
    n_cond = len(experimental_data.filter.control_conditions)
    n = n_monkey * n_cond

    n_rows, n_cols = n, 1
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(3, 5*n_monkey), dpi=200)
    axes = [fig.add_subplot(gs[i, 0]) for i in range(n)]

    i = 0
    for j, monkey in enumerate(monkeys):

        log(f"Stats for success to control trials over time "
            f"(fig: '{FIG_HISTORY_CONTROL}') - {monkey}",
            NAME)

        alternatives, control_types, hits = \
            experimental_data.filter.get_control(d[monkey])

        control_d = control_history_sort_data(alternatives, control_types,
                                              hits, n_chunk=n_chunk)

        for cond, color, title in \
                zip(experimental_data.filter.control_conditions,
                    colors, labels):

            last = i == n-1

            last_for_monkey = (i+1) % n_cond == 0
            if last_for_monkey:
                letter = string.ascii_uppercase[j]

            else:
                letter = None

            _plot_history_control(
                results=control_d[cond],
                color=color,
                ax=axes[i],
                last=last,
                title=title,
                letter=letter
            )

            i += 1

    log(f"Creating '{FIG_HISTORY_CONTROL}'...", NAME)
    # plt.tight_layout()

    gs.tight_layout(fig)

    j = 0
    for i, ax in enumerate(fig.get_axes()):
        last_for_monkey = (i + 1) % n_cond == 0
        if last_for_monkey:
            ax.text(
                s=string.ascii_uppercase[j],
                x=-0.12, y=-0.2, horizontalalignment='center',
                verticalalignment='center', transform=ax.transAxes,
                fontsize=20)
            j += 1

    fig.savefig(fname=FIG_HISTORY_CONTROL)
    log(f"Done!\n", NAME)


def history_best_param(fit, regression_param=None):

    monkeys = sorted(fit.keys())

    n_monkey = len(monkeys)

    n_rows, n_cols = n_monkey, 3
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(15, 5*n_rows), dpi=200)

    axes = [[] for _ in range(n_cols)]
    for i in range(len(monkeys)):
        for j in range(3):
            axes[i].append(fig.add_subplot(gs[i, j]))

    args = (
        ('pos_risk_aversion', 'neg_risk_aversion', (-1, 1), True, r"$\omega$"),
        ('pos_distortion', 'neg_distortion', (0, 1), False, r"$\alpha$"),
        ('pos_precision', 'neg_precision', (0, 5), False, r"$\lambda$")
    )

    for i, monkey in enumerate(monkeys):

        ax = axes[i][0]
        letter = string.ascii_uppercase[i]
        ax.text(
            s=letter, x=-0.2, y=-0.1, horizontalalignment='center',
            verticalalignment='center', transform=ax.transAxes,
            fontsize=30)

        for j, arg in enumerate(args):

            pos_param, neg_param, y_lim, show_mid_line, param_name = arg

            _plot_history_best_param(
                ax=axes[i][j],
                pos_param=fit[monkey][pos_param],
                neg_param=fit[monkey][neg_param],
                y_lim=y_lim,
                show_mid_line=show_mid_line,
                param_name=param_name
            )

            if regression_param:

                for param, color in zip((pos_param, neg_param),
                                        (COLOR_GAIN, COLOR_LOSS)):

                    alpha, beta, relevant = regression_param[monkey][param]

                    n = len(fit[monkey][param])
                    x = np.arange(1, n+1)
                    y = alpha + beta * x

                    # print(alpha, beta, relevant)
                    if relevant:
                        line_style = "-"
                        alpha = 1
                    else:
                        line_style = ":"
                        alpha = 0.4
                    axes[i][j].plot(x, y, color=color, linestyle=line_style,
                                    alpha=alpha)

    log(f"Creating '{FIG_HISTORY_BEST_PARAM}'...", NAME)

    gs.tight_layout(fig)
    fig.savefig(fname=FIG_HISTORY_BEST_PARAM)

    log(f"Done!\n", NAME)
