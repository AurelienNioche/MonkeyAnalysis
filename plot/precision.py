"""
Produce the precision figure
"""

import numpy as np

from parameters.parameters import COLOR_GAIN, COLOR_LOSS
from model import model

NAME = "plot.precision"


def _line(neg_precision, pos_precision, neg_risk_aversion, pos_risk_aversion,
          neg_distortion, pos_distortion,
          ax, alpha=1, linewidth=3):

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

    ax.plot(x, y_gain, color=COLOR_GAIN, linewidth=linewidth, alpha=alpha)
    ax.plot(x, y_loss, color=COLOR_LOSS, linewidth=linewidth, alpha=alpha)


def plot(ax, fit, show_average=True,
         axis_label_font_size=20,
         ticks_label_size=14):

    alpha_chunk = 0.5 if show_average else 1

    # log(f"Creating figure '{FIG_PRECISION}' for monkey {monkey}...", NAME)

    # fig, ax = plt.subplots(figsize=(6, 5), dpi=200)

    pra, nra, pdi, ndi, ppr, npr = \
        fit['pos_risk_aversion'], \
        fit['neg_risk_aversion'], \
        fit['pos_distortion'], \
        fit['neg_distortion'], \
        fit['pos_precision'], \
        fit['neg_precision']

    for j in range(len(pra)):

        _line(
            neg_risk_aversion=nra[j],
            pos_risk_aversion=pra[j],
            neg_distortion=ndi[j],
            pos_distortion=pdi[j],
            neg_precision=npr[j],
            pos_precision=ppr[j],
            ax=ax,
            linewidth=1,
            alpha=alpha_chunk
        )

    if show_average:
        _line(
            neg_risk_aversion=np.mean(nra),
            pos_risk_aversion=np.mean(pra),
            neg_distortion=np.mean(ndi),
            pos_distortion=np.mean(pdi),
            neg_precision=np.mean(npr),
            pos_precision=np.mean(ppr),
            ax=ax
        )

    ax.set_xticks([0, 1, 2])
    ax.set_yticks([0, 0.5, 1])

    ax.set_xlim(-0.01, 2.01)
    ax.set_ylim(-0.01, 1.01)

    ax.tick_params(axis='both', labelsize=ticks_label_size)

    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['top'].set_color('none')

    ax.set_xlabel("$|x_{Risky} - x_{Safe}|$", fontsize=axis_label_font_size)
    ax.set_ylabel("P(Choose risky option)", fontsize=axis_label_font_size)
    #
    # save_fig(fig_type=FIG_PRECISION, fig=fig,
    #          pdf=pdf, monkey=monkey)
