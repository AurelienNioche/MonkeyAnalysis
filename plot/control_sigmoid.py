"""
Produce the control sigmoid figures
"""

import numpy as np
import matplotlib.pyplot as plt

from utils.log import log
from plot.utils import save_fig

from parameters.parameters import FIG_CONTROL_SIGMOID, \
    COLOR_GAIN, COLOR_LOSS, CONTROL_CONDITIONS

from sigmoid_fit.sigmoid_fit import sigmoid_fit

NAME = "plot.control"


def diff_ev(alternative):
    return \
        np.abs(alternative[0][0] * alternative[0][1]
               - alternative[1][0] * alternative[1][1])


def _plot(x_data, y_data, ax, color='C0',
          x_label=None, y_label=None,
          label=None, title=None,
          line_width=3,
          axis_label_font_size=20,
          ticks_label_font_size=14,
          point_size=100):

    stats_r = None
    try:

        x, y, stats_r = sigmoid_fit(x_data=x_data, y_data=y_data)

        ax.plot(x, y, color=color, linewidth=line_width, label=label)
        if label is not None:
            ax.legend()

    except RuntimeError as e:
        log(e, NAME)

    ax.scatter(x_data, y_data, color=color, alpha=0.5, s=point_size)

    ax.axhline(0.5, alpha=0.5, linewidth=1, color='black',
               linestyle='--', zorder=-10)
    # ax.axvline(0, alpha=0.5, linewidth=1, color='black',
    #            linestyle='--', zorder=-10)

    ax.set_ylim(-0.01, 1.01)
    ax.set_yticks((0, 0.5, 1))

    # Axis labels
    ax.set_xlabel(x_label, fontsize=axis_label_font_size)
    ax.set_ylabel(y_label, fontsize=axis_label_font_size)

    # Remove top and right borders
    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_color('none')

    ax.tick_params(axis='both', which='major', labelsize=ticks_label_font_size)
    ax.tick_params(axis='both', which='minor', labelsize=ticks_label_font_size)

    ax.set_title(title, fontsize=axis_label_font_size*1.5)

    return stats_r


def control_sigmoid(alternatives, control_types, hits, monkey, pdf=None):

    uniq_alternatives = []
    cont_type_for_uniq_alt = []
    y_data = []
    x_data = []
    for i in range(len(alternatives)):
        alt = alternatives[i]
        if alt not in uniq_alternatives:
            uniq_alternatives.append(alt)

            ct = control_types[i]
            cont_type_for_uniq_alt.append(ct)
            y_data.append([])

            x = diff_ev(alt)
            x_data.append(x)

        y_data[uniq_alternatives.index(alt)].append(hits[i])

    x_data = np.array(x_data)
    y_data = np.array([np.mean(i) for i in y_data])
    cont_type_for_uniq_alt = np.array(cont_type_for_uniq_alt)

    colors = ["black", COLOR_GAIN, COLOR_LOSS, COLOR_GAIN, COLOR_LOSS]
    n_rows = 3
    fig, _axes = plt.subplots(figsize=(6, 5*n_rows), nrows=n_rows, dpi=200)

    axes = [_axes[0], _axes[1], _axes[1], _axes[2], _axes[2]]
    labels = [None, "Gain", "Loss", "Gain", "Loss"]
    titles = ["Gain vs loss", ] \
        + ["Same $p$ - Diff $x$", ] * 2 \
        + ["Same $x$ - Diff $p$", ] * 2

    for i, cd in enumerate(CONTROL_CONDITIONS):
        relevant = cont_type_for_uniq_alt == cd
        color = colors[i]
        _plot(x_data=x_data[relevant],
              y_data=y_data[relevant],
              color=color,
              title=titles[i],
              label=labels[i],
              ax=axes[i],
              x_label="$EV_{best} - EV_{worse}$",
              y_label="F(Choose best)")

    save_fig(fig_type=FIG_CONTROL_SIGMOID, fig=fig, pdf=pdf, monkey=monkey)
