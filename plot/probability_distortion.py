"""
Produce the probability distortion figure
"""

import matplotlib.gridspec
import numpy as np
from matplotlib import pyplot as plt
import string

from parameters.parameters import COLOR_LOSS, COLOR_GAIN, \
    FIG_PROBABILITY_DISTORTION
from utils.utils import log

NAME = "plot.probability_distortion"


def pi(p, distortion):
    """Probability distortion"""

    return np.exp(-(-np.log(p)) ** distortion) if p > 0 else 0


def _plot(neg_distortion, pos_distortion, ax,
          linewidth=3, alpha=1):

    label_font_size = 20
    ticks_label_size = 14

    n_points = 1000

    x = np.linspace(0, 1, n_points)

    ax.plot(x, [pi(i, neg_distortion) for i in x], color=COLOR_LOSS,
            linewidth=linewidth, alpha=alpha)
    ax.plot(x, [pi(i, pos_distortion) for i in x], color=COLOR_GAIN,
            linewidth=linewidth, alpha=alpha)

    ax.set_xlabel('$p$', fontsize=label_font_size)
    ax.set_ylabel('$w(p)$', fontsize=label_font_size)

    ax.set_ylim(0, 1)
    ax.set_aspect('equal')

    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['top'].set_color('none')

    ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])

    ax.tick_params(axis='both', which='major', labelsize=ticks_label_size)


def probability_distortion(fit, show_average=True):

    log(f"Creating figure '{FIG_PROBABILITY_DISTORTION}'...", NAME)

    monkeys = sorted(fit.keys())
    n_monkeys = len(monkeys)

    alpha_chunk = 0.5 if show_average else 1

    n_rows, n_cols = 1, n_monkeys
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(6*n_cols, 5), dpi=200)

    axes = [fig.add_subplot(gs[0, i]) for i in range(len(monkeys))]

    for i, monkey in enumerate(monkeys):

        pdi = fit[monkey]['pos_distortion']
        ndi = fit[monkey]['neg_distortion']

        for j in range(len(pdi)):

            _plot(
                neg_distortion=ndi[j],
                pos_distortion=pdi[j],
                alpha=alpha_chunk,
                linewidth=1,
                ax=axes[i])

        if show_average:
            _plot(
                neg_distortion=np.mean(ndi),
                pos_distortion=np.mean(pdi),
                ax=axes[i])

    gs.tight_layout(fig)

    for i, ax in enumerate(fig.get_axes()):
        ax.text(
            s=string.ascii_uppercase[i],
            x=-0.2, y=-0.1, horizontalalignment='center',
            verticalalignment='center', transform=ax.transAxes,
            fontsize=30)

    fig.savefig(fname=FIG_PROBABILITY_DISTORTION)

    log(f"Done!\n", NAME)
