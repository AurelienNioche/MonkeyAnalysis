from pylab import np, plt
import os
import json





"""
Produce the utility function figure
"""


def u(m, positive_risk_aversion, negative_risk_aversion):

    assert -1 < positive_risk_aversion < 1
    assert -1 < negative_risk_aversion < 1

    if m > 0:
        return m ** (1 - positive_risk_aversion)  # / (1 - positive_risk_aversion)

    elif m < 0:
        return - np.abs(m) ** (1 + negative_risk_aversion)

    else:
        return 0


def plot(positive_risk_aversion, negative_risk_aversion, fig_name=None):

    reward_max = 1
    reward_min = - 1
    n_points = 1000
    axis_label_font_size = 20
    ticks_label_font_size = 14
    line_width = 3

    x = np.linspace(reward_min, reward_max, n_points)
    y = [u(i, positive_risk_aversion, negative_risk_aversion) for i in x]

    # x= x-2

    # x[:] = np.divide(x, reward_max)

    ax = plt.gca()
    ax.plot(x, y, color="black", linewidth=line_width)

    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_color('none')

    ax.set_ylim([-1, 1])
    ax.set_xlim([-1, 1])

    ax.set_xlabel("$x$", rotation=0, position=(0.9, None), fontsize=axis_label_font_size)
    ax.set_ylabel("$u(x)$", rotation=0, position=(None, 0.9), fontsize=axis_label_font_size)

    plt.tick_params(axis='both', which='major', labelsize=ticks_label_font_size)
    plt.tick_params(axis='both', which='minor', labelsize=ticks_label_font_size)

    plt.xticks([-1, -0.5, 0.5, 1])
    plt.yticks([-1, -0.5, 0.5, 1])

    ax.set_aspect(1)

    plt.tight_layout()

    if fig_name:
        plt.savefig(fname=fig_name)
        plt.close()

    else:
        plt.show()


def main():

    plot(0.9, 0.5)

main()