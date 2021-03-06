import numpy as np

"""
Produce the utility function figure
"""


def u(m, pos_risk_aversion, neg_risk_aversion):

    assert -1 < pos_risk_aversion < 1
    assert -1 < neg_risk_aversion < 1

    if m > 0:
        return m ** (1 - pos_risk_aversion)  # / (1 - positive_risk_aversion)

    elif m < 0:
        return - np.abs(m) ** (1 + neg_risk_aversion)

    else:
        return 0


def plot(pos_risk_aversion, neg_risk_aversion, ax, alpha=1, linewidth=3, color="black", linestyle="-"):

    reward_max = 1
    reward_min = - 1
    n_points = 1000
    axis_label_font_size = 20
    ticks_label_font_size = 12

    x = np.linspace(reward_min, reward_max, n_points)
    y = [u(i, pos_risk_aversion, neg_risk_aversion) for i in x]

    ax.plot(x, y, color=color, linewidth=linewidth, alpha=alpha, linestyle=linestyle)

    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_color('none')

    ax.set_ylim(-1, 1)
    ax.set_xlim(-1, 1)

    ax.set_xlabel("$x$", rotation=0, position=(0.9, None), fontsize=axis_label_font_size)
    ax.set_ylabel("$u(x)$", rotation=0, position=(None, 0.9), fontsize=axis_label_font_size)

    ax.tick_params(axis='both', which='major', labelsize=ticks_label_font_size)
    ax.tick_params(axis='both', which='minor', labelsize=ticks_label_font_size)

    ax.set_xticks([-1, 1])
    ax.set_yticks([-1, 1])

    ax.set_aspect(1)
