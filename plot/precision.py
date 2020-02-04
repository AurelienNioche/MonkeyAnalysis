"""
Produce the precision figure
"""

import matplotlib.gridspec
import numpy as np
from matplotlib import pyplot as plt

from parameters.parameters import COLOR_GAIN, COLOR_LOSS, FIG_PRECISION
from model import model
from utils.utils import log

NAME = "plot.precision"


def _plot(neg_precision, pos_precision, neg_risk_aversion, pos_risk_aversion,
          neg_distortion, pos_distortion,
          ax, alpha=1, linewidth=3):

    axis_label_font_size = 20
    ticks_label_size = 14

    n_points = 1000

    p0, m0 = 0.25, 3
    p1, m1 = 1., 2

    x = np.linspace(0.1, 1.99, n_points)

    y_loss = np.zeros(len(x))
    y_gain = np.zeros(len(x))

    for i, delta in enumerate(x):

        new_m1 = m1 - delta

        y_gain[i] = model.get_p_multi(
            p0=p0, m0=m0, p1=p1, m1=new_m1,
            neg_distortion=neg_distortion, pos_distortion=pos_distortion,
            neg_risk_aversion=neg_risk_aversion,
            pos_risk_aversion=pos_risk_aversion,
            neg_precision=neg_precision, pos_precision=pos_precision
        )

    p0, m0 = 0.25, -3
    p1, m1 = 1., -0.1

    for i, delta in enumerate(x):

        new_m1 = m1 - delta

        y_loss[i] = model.get_p_multi(
            p0=p0, m0=m0, p1=p1, m1=new_m1,
            neg_distortion=neg_distortion, pos_distortion=pos_distortion,
            neg_risk_aversion=neg_risk_aversion,
            pos_risk_aversion=pos_risk_aversion,
            neg_precision=neg_precision, pos_precision=pos_precision
        )

    ax.set_xticks([0, 1, 2])
    ax.set_yticks([0, 0.5, 1])

    ax.set_xlim(-0.01, 2.01)
    ax.set_ylim(-0.01, 1.01)

    ax.plot(x, y_gain, color=COLOR_GAIN, linewidth=linewidth, alpha=alpha)
    ax.plot(x, y_loss, color=COLOR_LOSS, linewidth=linewidth, alpha=alpha)

    ax.tick_params(axis='both', labelsize=ticks_label_size)

    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['top'].set_color('none')

    ax.set_xlabel("$|x_{Risky} - x_{Safe}|$", fontsize=axis_label_font_size)
    ax.set_ylabel("P(Choose risky option)", fontsize=axis_label_font_size)


def precision(fit, show_average=True):

    log(f"Creating figure '{FIG_PRECISION}'...", NAME)

    monkeys = sorted(fit.keys())

    alpha_chunk = 0.5 if show_average else 1

    n_rows, n_cols = 1, 2
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(12, 5), dpi=200)

    axes = [fig.add_subplot(gs[0, i]) for i in range(len(monkeys))]

    for i, monkey in enumerate(monkeys):

        pra = fit[monkey]['pos_risk_aversion']
        nra = fit[monkey]['neg_risk_aversion']
        pdi = fit[monkey]['pos_distortion']
        ndi = fit[monkey]['neg_distortion']
        ppr = fit[monkey]['pos_precision']
        npr = fit[monkey]['neg_precision']

        for j in range(len(pra)):

            _plot(
                neg_risk_aversion=nra[j],
                pos_risk_aversion=pra[j],
                neg_distortion=ndi[j],
                pos_distortion=pdi[j],
                neg_precision=npr[j],
                pos_precision=ppr[j],
                ax=axes[i],
                linewidth=1,
                alpha=alpha_chunk
            )

        if show_average:
            _plot(
                neg_risk_aversion=np.mean(nra),
                pos_risk_aversion=np.mean(pra),
                neg_distortion=np.mean(ndi),
                pos_distortion=np.mean(pdi),
                neg_precision=np.mean(npr),
                pos_precision=np.mean(ppr),
                ax=axes[i])

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()

    ax.text(
        s='A', x=-0.05, y=-0.1, horizontalalignment='center',
        verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s='B', x=0.49, y=-0.1, horizontalalignment='center',
        verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    gs.tight_layout(fig)
    fig.savefig(fname=FIG_PRECISION)

    log(f"Done!\n", NAME)
