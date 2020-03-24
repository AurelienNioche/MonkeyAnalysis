"""
Produce the probability distortion figure
"""

import numpy as np
import matplotlib.pyplot as plt

from parameters.parameters import COLOR_LOSS, COLOR_GAIN, \
    FIG_PROBABILITY_DISTORTION
from utils.log import log
from plot.utils import save_fig

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

    ax.set_xticks((0, 0.5, 1))
    ax.set_yticks((0, 0.5, 1))

    ax.tick_params(axis='both', which='major', labelsize=ticks_label_size)


def probability_distortion(fit, monkey, show_average=True, pdf=None):

    alpha_chunk = 0.5 if show_average else 1

    fig, ax = plt.subplots(figsize=(6, 5), dpi=200)

    # log(f"Creating figure '{FIG_PROBABILITY_DISTORTION}' "
    #     f"for monkey {monkey}...", NAME)

    pdi = fit['pos_distortion']
    ndi = fit['neg_distortion']

    for j in range(len(pdi)):

        _plot(
            neg_distortion=ndi[j],
            pos_distortion=pdi[j],
            alpha=alpha_chunk,
            linewidth=1,
            ax=ax)

    if show_average:
        _plot(
            neg_distortion=np.mean(ndi),
            pos_distortion=np.mean(pdi),
            ax=ax)

    save_fig(fig_type=FIG_PROBABILITY_DISTORTION, fig=fig,
             pdf=pdf, monkey=monkey)
