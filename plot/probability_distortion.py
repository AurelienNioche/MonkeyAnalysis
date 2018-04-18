import numpy as np


"""
Produce the probability distortion figure
"""


def pi(p, distortion):
    """Probability distortion"""

    return np.exp(-(-np.log(p)) ** distortion) if p > 0 else 0


def plot(neg_distortion, pos_distortion, color_gain, color_loss, ax, linewidth=3, alpha=1):

    label_font_size = 20
    ticks_label_size = 14

    n_points = 1000

    x = np.linspace(0, 1, n_points)

    ax.plot(x, [pi(i, neg_distortion) for i in x], color=color_loss, linewidth=linewidth, alpha=alpha)
    ax.plot(x, [pi(i, pos_distortion) for i in x], color=color_gain, linewidth=linewidth, alpha=alpha)

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
