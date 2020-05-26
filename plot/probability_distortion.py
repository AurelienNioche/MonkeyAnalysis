"""
Produce the probability distortion figure
"""

import numpy as np

from plot.freq_risk import add_text

NAME = "plot.probability_distortion"


def pi(p, distortion):
    """Probability distortion"""

    return np.exp(-(-np.log(p)) ** distortion) if p > 0 else 0


def _line(param, ax, linewidth=3, alpha=1, color='C0'):

    n_points = 1000

    x = np.linspace(0, 1, n_points)

    ax.plot(x, [pi(i, param) for i in x], color=color,
            linewidth=linewidth, alpha=alpha)
    # ax.plot(x, [pi(i, pos_distortion) for i in x], color=COLOR_GAIN,
    #         linewidth=linewidth, alpha=alpha)


def plot(ax, fit, show_average=True, label_font_size=20, ticks_label_size=14):

    alpha_chunk = 0.5 if show_average else 1

    # fig, ax = plt.subplots(figsize=(6, 5), dpi=200)

    # log(f"Creating figure '{FIG_PROBABILITY_DISTORTION}' "
    #     f"for monkey {monkey}...", NAME)

    for j in range(len(fit["distortion"])):

        _line(
            param=fit["distortion"][j],
            alpha=alpha_chunk,
            linewidth=1,
            ax=ax)

    if show_average:
        v = np.mean(fit["distortion"])
        _line(
            param=v,
            linewidth=3,
            ax=ax)
        add_text(ax, r'$\alpha=' + f'{v:.2f}' + '$')

    ax.set_xlabel('$p$', fontsize=label_font_size)
    ax.set_ylabel('$w(p)$', fontsize=label_font_size)

    ax.set_ylim(0, 1)
    ax.set_xlim(-0.01, 1.01)
    ax.set_aspect('equal')

    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['top'].set_color('none')

    ax.plot((0, 1), (0, 1), alpha=0.5, linewidth=1, color='black',
            linestyle='--', zorder=-10)

    ax.set_xticks((0, 0.5, 1))
    ax.set_yticks((0, 0.5, 1))

    ax.tick_params(axis='both', which='major', labelsize=ticks_label_size)


# def plot(ax, fit, show_average=True,
#          label_font_size=20,
#          ticks_label_size=14):
#
#     alpha_chunk = 0.5 if show_average else 1
#
#     # fig, ax = plt.subplots(figsize=(6, 5), dpi=200)
#
#     # log(f"Creating figure '{FIG_PROBABILITY_DISTORTION}' "
#     #     f"for monkey {monkey}...", NAME)
#
#     pdi = fit['pos_distortion']
#     ndi = fit['neg_distortion']
#
#     for j in range(len(pdi)):
#
#         _line(
#             neg_distortion=ndi[j],
#             pos_distortion=pdi[j],
#             alpha=alpha_chunk,
#             linewidth=1,
#             ax=ax)
#
#     if show_average:
#         _line(
#             neg_distortion=np.mean(ndi),
#             pos_distortion=np.mean(pdi),
#             ax=ax)
#
#     ax.set_xlabel('$p$', fontsize=label_font_size)
#     ax.set_ylabel('$w(p)$', fontsize=label_font_size)
#
#     ax.set_ylim(0, 1)
#     ax.set_aspect('equal')
#
#     ax.spines['right'].set_color('none')
#     ax.xaxis.set_ticks_position('bottom')
#     ax.yaxis.set_ticks_position('left')
#     ax.spines['top'].set_color('none')
#
#     ax.set_xticks((0, 0.5, 1))
#     ax.set_yticks((0, 0.5, 1))
#
#     ax.tick_params(axis='both', which='major', labelsize=ticks_label_size)