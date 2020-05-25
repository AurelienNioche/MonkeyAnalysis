import numpy as np

from parameters.parameters import CONTROL_CONDITIONS, LABELS_CONTROL

NAME = "plot.history"


def _plot_history_best_param(
        param, ax, y_lim, param_name, mid_line=None,
        axis_label_font_size=20,
        ticks_label_font_size=14,
        color='C0',
        point_size=100):

    x_data = np.arange(len(param)) + 1
    y_data = param

    ax.scatter(x_data, y_data, color=color, alpha=0.5, s=point_size)

    if mid_line is not None:
        ax.axhline(mid_line, alpha=0.5, linewidth=1, color='black',
                   linestyle='--',
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


def _plot_history_control(results, color, ax, last=False,
                          ylabel="Success rate", title="Title", fontsize=10):
    """
    Called by 'control history'
    """

    # exemplary_d is a list (n=number of boxplot) of list (n=number of datapoints)
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
            x_scatter.append(i + np.random.uniform(-0.025*n, 0.025*n))

    assert len(x_scatter) == len(y_scatter)
    ax.scatter(x_scatter, y_scatter, c=color, s=50, alpha=0.5,
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


def history_control(axes, hist_control_d):

    n_cond = len(CONTROL_CONDITIONS)

    for i, cond in enumerate(CONTROL_CONDITIONS):

        title = LABELS_CONTROL[cond]

        last = i == n_cond-1

        _plot_history_control(
            results=hist_control_d[cond],
            ax=axes[i],
            last=last,
            title=title,
        )


def history_best_param(axes, data):

    fit = data['fit']

    args = (
        ('risk_aversion', (-1, 1), 0.0, r"$\omega$"),
        ('distortion', (0, 2), 1.0, r"$\alpha$"),
        ('precision', (0, 5), False, r"$\lambda$")
    )

    for i, arg in enumerate(args):

        pr, y_lim, mid_line, param_name = arg

        _plot_history_best_param(
            ax=axes[i],
            param=fit[pr],
            y_lim=y_lim,
            mid_line=mid_line,
            param_name=param_name
        )

        if 'regression' in data.keys():
            regression_param = data['regression']

            alpha, beta, relevant = regression_param[pr]

            n = len(fit[pr])
            x = np.arange(1, n+1)
            y = alpha + beta * x

            # print(alpha, beta, relevant)
            if relevant:
                line_style = "-"
                alpha = 1
            else:
                line_style = ":"
                alpha = 0.4
            axes[i].plot(x, y, linestyle=line_style,
                         alpha=alpha)
