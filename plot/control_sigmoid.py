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


NAME = "plot.control"


def diff_ev_right_left(alternative):
    return \
        alternative[1][0] * alternative[1][1] \
        - alternative[0][0] * alternative[0][1]


def _plot(x, y, ax, color='C0',
          x_fit=None, y_fit=None,
          x_label=None, y_label=None,
          label=None, title=None,
          line_width=3,
          axis_label_font_size=20,
          ticks_label_font_size=14,
          point_size=100):

    if x_fit is not None and y_fit is not None:
        ax.plot(x_fit, y_fit, color=color, linewidth=line_width, label=label)
        if label is not None:
            ax.legend()

    ax.scatter(x, y, color=color, alpha=0.5, s=point_size)

    ax.axhline(0.5, alpha=0.5, linewidth=1, color='black',
               linestyle='--', zorder=-10)
    # ax.axvline(0, alpha=0.5, linewidth=1, color='black',
    #            linestyle='--', zorder=-10)

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

    ax.tick_params(axis='both', which='major', labelsize=ticks_label_font_size)
    ax.tick_params(axis='both', which='minor', labelsize=ticks_label_font_size)

    ax.set_title(title, fontsize=axis_label_font_size*1.5)


def add_text(ax, txt):
    ax.text(0.05, 0.9, txt,
            horizontalalignment='left',
            verticalalignment='top',
            transform=ax.transAxes)


def control_sigmoid(axes, x, y, x_fit, y_fit, fit):

    colors = ["black", COLOR_GAIN, COLOR_LOSS, COLOR_GAIN, COLOR_LOSS]
    # n_rows = 3
    # fig, _axes = plt.subplots(figsize=(6, 5*n_rows), nrows=n_rows, dpi=200)
    #
    _axes = [axes[0], axes[1], axes[1], axes[2], axes[2]]
    labels = [None, "Gain", "Loss", "Gain", "Loss"]
    titles = ["Gain vs loss", ] \
        + ["Same $p$ - Diff $x$", ] * 2 \
        + ["Same $x$ - Diff $p$", ] * 2

    for i, cd in enumerate(CONTROL_CONDITIONS):
        color = colors[i]
        ax = _axes[i]
        _plot(x=x[cd],
              y=y[cd],
              x_fit=x_fit[cd],
              y_fit=y_fit[cd],
              color=color,
              title=titles[i],
              label=labels[i],
              ax=ax,
              x_label="$EV_{right} - EV_{left}$",
              y_label="F(Choose right)")

    txt = \
        r"$F(x) = \dfrac{1}{1 + \exp(-k (x - x_0))}$" + "\n\n" \
        + "$k=" + f"{fit[SAME_P_GAIN_VS_LOSS][SIG_STEEP]:.2f}" + "$" + "\n" \
        + "$x_0=" + f"{fit[SAME_P_GAIN_VS_LOSS][SIG_MID]:.2f}" + "$" + "\n"
    add_text(axes[0], txt)

    txt = \
        r"$F(x) = \dfrac{1}{1 + \exp(-k (x - x_0))}$" + "\n\n" \
        + "$k^{gain}=" + f"{fit[SAME_P_GAIN][SIG_STEEP]:.2f}" + "$" + "\n" \
        + "$x_0^{gain}=" + f"{fit[SAME_P_GAIN][SIG_MID]:.2f}" + "$" + "\n" \
        + "$k^{loss}=" + f"{fit[SAME_P_LOSS][SIG_MID]:.2f}" + "$" + "\n" \
        + "$x_0^{loss}=" + f"{fit[SAME_P_LOSS][SIG_STEEP]:.2f}" + "$" + "\n"
    add_text(axes[1], txt)

    txt = \
        r"$F(x) = \dfrac{1}{1 + \exp(-k (x - x_0))}$" + "\n\n" \
        + "$k^{gain}=" + f"{fit[SAME_X0_GAIN][SIG_STEEP]:.2f}" + "$" + "\n" \
        + "$x_0^{gain}=" + f"{fit[SAME_X0_GAIN][SIG_MID]:.2f}" + "$" + "\n" \
        + "$k^{loss}=" + f"{fit[SAME_X0_LOSS][SIG_MID]:.2f}" + "$" + "\n" \
        + "$x_0^{loss}=" + f"{fit[SAME_X0_LOSS][SIG_STEEP]:.2f}" + "$" + "\n"
    add_text(axes[2], txt)

        # for cond in ('gain', 'loss'):
    #     txt += r"$k_{" + f"{cond}" + "}=" + \
    #            f"{stats_slope[cond]['val']:.2f}\," \
    #            f"[{stats_slope[cond]['ic-']:.2f}, " \
    #            f"{stats_slope[cond]['ic+']:.2f}]" + "$\n"


    # save_fig(fig_type=FIG_CONTROL_SIGMOID, fig=fig, pdf=pdf, monkey=monkey)
