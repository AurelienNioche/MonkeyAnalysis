import numpy as np

from model import model


def plot(neg_precision, pos_precision, neg_risk_aversion, pos_risk_aversion, neg_distortion, pos_distortion,
         color_gain, color_loss, ax, alpha=1, linewidth=3):

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
            neg_risk_aversion=neg_risk_aversion, pos_risk_aversion=pos_risk_aversion,
            neg_precision=neg_precision, pos_precision=pos_precision
        )

    p0, m0 = 0.25, -3
    p1, m1 = 1., -0.1

    for i, delta in enumerate(x):

        new_m1 = m1 - delta

        y_loss[i] = model.get_p_multi(
            p0=p0, m0=m0, p1=p1, m1=new_m1,
            neg_distortion=neg_distortion, pos_distortion=pos_distortion,
            neg_risk_aversion=neg_risk_aversion, pos_risk_aversion=pos_risk_aversion,
            neg_precision=neg_precision, pos_precision=pos_precision
        )

    ax.set_xticks([0, 1, 2])
    ax.set_yticks([0, 0.5, 1])

    ax.set_xlim(-0.01, 2.01)
    ax.set_ylim(-0.01, 1.01)

    ax.plot(x, y_gain, color=color_gain, linewidth=linewidth, alpha=alpha)
    ax.plot(x, y_loss, color=color_loss, linewidth=linewidth, alpha=alpha)

    ax.tick_params(axis='both', labelsize=ticks_label_size)

    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['top'].set_color('none')

    ax.set_xlabel("$|x_{Risky} - x_{Safe}|$", fontsize=axis_label_font_size)
    ax.set_ylabel("P(Choose risky option)", fontsize=axis_label_font_size)
