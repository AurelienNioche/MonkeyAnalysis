from pylab import np, plt


"""
Produce the probability distortion figure
"""


def pi(p, distortion):
    """Probability distortion"""

    return np.exp(-(-np.log(p)) ** distortion)


def plot(neg_distortion, pos_distortion, fig_name=None):

    label_font_size = 20
    ticks_label_size = 14
    line_width = 3

    n_points = 1000

    x = np.linspace(0.001, 1, n_points)

    plt.plot(x, pi(x), color="black", linewidth=line_width)

    plt.xlabel('$p$', fontsize=label_font_size)
    plt.ylabel('$w(p)$', fontsize=label_font_size)

    plt.ylim(0, 1)
    plt.figaspect(1)

    ax = plt.gca()

    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['top'].set_color('none')

    plt.xticks([0, 0.25, 0.5, 0.75, 1], fontsize=ticks_label_size)
    plt.yticks([0, 0.25, 0.5, 0.75, 1], fontsize=ticks_label_size)

    plt.figaspect(1)

    if fig_name:
        plt.savefig(fig_name)
        plt.close()

    else:
        plt.show()
