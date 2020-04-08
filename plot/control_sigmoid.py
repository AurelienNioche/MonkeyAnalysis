"""
Produce the control sigmoid figures
"""

from parameters.parameters import \
    COLOR_GAIN, COLOR_LOSS, CONTROL_CONDITIONS, \
    SAME_P_GAIN_VS_LOSS, \
    SAME_P_GAIN, \
    SAME_P_LOSS, \
    SAME_X0_GAIN, \
    SAME_X0_LOSS, \
    SIG_STEEP, \
    SIG_MID

from plot.freq_risk import scatter_and_sigmoid, add_text

NAME = "plot.control"


def control_sigmoid(axes, data,
                    axis_label_font_size=20,
                    ticks_label_font_size=14):

    colors = ["black", COLOR_GAIN, COLOR_LOSS, COLOR_GAIN, COLOR_LOSS]

    _axes = [axes[0], axes[1], axes[1], axes[2], axes[2]]
    labels = [None, "Gain", "Loss", "Gain", "Loss"]

    for i, cd in enumerate(CONTROL_CONDITIONS):
        color = colors[i]
        ax = _axes[i]
        d = data[cd]

        scatter_and_sigmoid(
            x=d['x'],
            y=d['y'],
            x_fit=d['fit']['x'],
            y_fit=d['fit']['y'],
            color=color,
            label=labels[i],
            ax=ax)

    x_label = "$EV_{right} - EV_{left}$"
    y_label = "F(Choose right)"

    titles = ["Gain vs loss", "Same $p$ - Diff $x$", "Same $x$ - Diff $p$", ]

    for i, ax in enumerate(axes):
        title = titles[i]
        ax.set_title(title, fontsize=axis_label_font_size*1.2)

        ax.axhline(0.5, alpha=0.5, linewidth=1, color='black',
                   linestyle='--', zorder=-10)
        ax.axvline(0.5, alpha=0.0, linewidth=1, color='black',
                   linestyle='--', zorder=-10)

        ax.set_ylim(-0.01, 1.01)
        ax.set_yticks((0, 0.5, 1))

        # Axis labels
        ax.set_xlabel(x_label, fontsize=axis_label_font_size)
        ax.set_ylabel(y_label, fontsize=axis_label_font_size)

        # Remove top and right borders
        ax.spines['right'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['top'].set_color('none')

        ax.tick_params(axis='both', which='major',
                       labelsize=ticks_label_font_size)
        ax.tick_params(axis='both', which='minor',
                       labelsize=ticks_label_font_size)

    txt = \
        r"$F(x) = \dfrac{1}{1 + \exp(-k (x - x_0))}$" + "\n\n" \
        + "$k=" + f"{data[SAME_P_GAIN_VS_LOSS]['fit'][SIG_STEEP]:.2f}" + "$" + "\n" \
        + "$x_0=" + f"{data[SAME_P_GAIN_VS_LOSS]['fit'][SIG_MID]:.2f}" + "$" + "\n"
    add_text(axes[0], txt)

    txt = \
        r"$F(x) = \dfrac{1}{1 + \exp(-k (x - x_0))}$" + "\n\n" \
        + "$k^{gain}=" + f"{data[SAME_P_GAIN]['fit'][SIG_STEEP]:.2f}" + "$" + "\n" \
        + "$x_0^{gain}=" + f"{data[SAME_P_GAIN]['fit'][SIG_MID]:.2f}" + "$" + "\n" \
        + "$k^{loss}=" + f"{data[SAME_P_LOSS]['fit'][SIG_MID]:.2f}" + "$" + "\n" \
        + "$x_0^{loss}=" + f"{data[SAME_P_LOSS]['fit'][SIG_STEEP]:.2f}" + "$" + "\n"
    add_text(axes[1], txt)

    txt = \
        r"$F(x) = \dfrac{1}{1 + \exp(-k (x - x_0))}$" + "\n\n" \
        + "$k^{gain}=" + f"{data[SAME_X0_GAIN]['fit'][SIG_STEEP]:.2f}" + "$" + "\n" \
        + "$x_0^{gain}=" + f"{data[SAME_X0_GAIN]['fit'][SIG_MID]:.2f}" + "$" + "\n" \
        + "$k^{loss}=" + f"{data[SAME_X0_LOSS]['fit'][SIG_MID]:.2f}" + "$" + "\n" \
        + "$x_0^{loss}=" + f"{data[SAME_X0_LOSS]['fit'][SIG_STEEP]:.2f}" + "$" + "\n"
    add_text(axes[2], txt)

        # for cond in ('gain', 'loss'):
    #     txt += r"$k_{" + f"{cond}" + "}=" + \
    #            f"{stats_slope[cond]['val']:.2f}\," \
    #            f"[{stats_slope[cond]['ic-']:.2f}, " \
    #            f"{stats_slope[cond]['ic+']:.2f}]" + "$\n"


    # save_fig(fig_type=FIG_CONTROL_SIGMOID, fig=fig, pdf=pdf, monkey=monkey)
