"""
Produce the figure which presents at which extent
the risky option was chosen according to the difference
between expected values,
i.e. the certainty-risk trade-off figure
"""

from parameters.parameters import \
    COLOR_LOSS, COLOR_GAIN, GAIN, LOSS, \
    SIG_STEEP, SIG_MID

NAME = "plot.freq_risk"


def scatter_and_sigmoid(ax, x, y, x_fit, y_fit, color, label=None,
                        line_width=3, point_size=100, alpha_scatter=0.5):

    if label is not None:
        label = label.capitalize()

    if x_fit is not None and y_fit is not None:

        ax.plot(x_fit, y_fit, color=color, linewidth=line_width, label=label)

    ax.scatter(x, y, color=color, alpha=alpha_scatter, s=point_size)


def add_text(ax, txt, fontsize=10):
    ax.text(0.05, 0.9, txt,
            horizontalalignment='left',
            verticalalignment='top',
            transform=ax.transAxes)


def plot(ax, data,
         axis_label_font_size=20,
         ticks_label_font_size=14):

    conditions = (GAIN, LOSS)
    color = {GAIN: COLOR_GAIN, LOSS: COLOR_LOSS}

    for i, cd in enumerate(conditions):

        d = data[cd]

        scatter_and_sigmoid(
            x=d['x'], y=d['y'],
            x_fit=d['fit']['x'], y_fit=d['fit']['y'],
            color=color[cd],
            ax=ax,
            label=cd
        )

    ax.axhline(0.5, alpha=0.5, linewidth=1, color='black',
               linestyle='--', zorder=-10)
    ax.axvline(0, alpha=0.5, linewidth=1, color='black',
               linestyle='--', zorder=-10)

    ax.set_ylim(-0.01, 1.01)
    ax.set_yticks((0, 0.5, 1))

    # Axis labels
    ax.set_xlabel(
        r"$EV_{\mathrm{Riskiest\,option}} - EV_{\mathrm{Safest\,option}}$",
        fontsize=axis_label_font_size)
    ax.set_ylabel(
        "F(Choose riskiest option)",
        fontsize=axis_label_font_size)

    # Remove top and right borders
    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_color('none')

    ax.tick_params(axis='both', which='major', labelsize=ticks_label_font_size)
    ax.tick_params(axis='both', which='minor', labelsize=ticks_label_font_size)

    txt = \
        r"$F(x) = \dfrac{1}{1 + \exp(-k (x - x_0))}$" + "\n\n" \
        + "$k^{gain}=" + f"{data[GAIN]['fit'][SIG_STEEP]:.2f}" + "$" + "\n"\
        + "$x_0^{gain}=" + f"{data[GAIN]['fit'][SIG_MID]:.2f}" + "$" + "\n" \
        + "$k^{loss}=" + f"{data[LOSS]['fit'][SIG_STEEP]:.2f}" + "$" + "\n" \
        + "$x_0^{loss}=" + f"{data[LOSS]['fit'][SIG_MID]:.2f}" + "$" + "\n" \
        # for cond in ('gain', 'loss'):
    #     txt += r"$k_{" + f"{cond}" + "}=" + \
    #            f"{stats_slope[cond]['val']:.2f}\," \
    #            f"[{stats_slope[cond]['ic-']:.2f}, " \
    #            f"{stats_slope[cond]['ic+']:.2f}]" + "$\n"

    add_text(ax, txt)

    ax.legend(loc='lower right')
