"""
Produce the precision figure
"""

import numpy as np

from plot.freq_risk import add_text

NAME = "plot.precision"


def _line(class_model,
          ax, color='C0', alpha=1, linewidth=3, **kwargs):

    n_points = 1000

    p0 = 0.5
    p1, x1 = 1., 0.5

    x0_list = np.linspace(0.501, 1.00, n_points)
    y = np.zeros(len(x0_list))

    dm = class_model([kwargs[k] for k in class_model.param_labels])

    for i, x0 in enumerate(x0_list):

        # print("p0", p0, "p1", p1, "x0", x0, "x1", x1)
        # print("Precision", kwargs["precision"])
        y[i] = dm.p_c0(p0=p0, x0=x0, p1=p1, x1=x1)

    ax.plot(x0_list, y, color=color, linewidth=linewidth, alpha=alpha)


def plot(ax, fit, show_average=True,
         axis_label_font_size=20,
         ticks_label_size=14):

    alpha_chunk = 0.5 if show_average else 1

    for j in range(len(fit['risk_aversion'])):

        _line(
            risk_aversion=fit['risk_aversion'][j],
            distortion=fit['distortion'][j],
            precision=fit['precision'][j],
            ax=ax,
            linewidth=1,
            alpha=alpha_chunk,
            class_model=fit['class_model']
        )

    if show_average:
        v = np.mean(fit['precision'])
        _line(
            risk_aversion=np.mean(fit['risk_aversion']),
            distortion=np.mean(fit['distortion']),
            precision=v,
            class_model=fit['class_model'],
            ax=ax
        )

        add_text(ax, r'$\lambda=' + f'{v:.2f}' + '$')

    # ax.set_xticks([0, 1, 2])
    ax.set_yticks([0, 0.5, 1])

    # ax.set_xlim(0.0, 2.01)
    ax.set_ylim(-0.01, 1.01)

    ax.tick_params(axis='both', labelsize=ticks_label_size)

    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['top'].set_color('none')

    ax.set_xlabel("$x_{risky}$", fontsize=axis_label_font_size)
    ax.set_ylabel("P(Choose risky option)", fontsize=axis_label_font_size)
