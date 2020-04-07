"""
Produce the the certainty-risk trade-off figure
"""

from parameters.parameters import COLOR_GAIN, COLOR_LOSS, GAIN, LOSS


NAME = "plot.exemplary_case"


def plot(exemplary_d, ax):

    axis_label_font_size = 14
    ticks_font_size = 14

    names = "Gain", "Loss"

    ax.scatter(names, (exemplary_d[GAIN], exemplary_d[LOSS]),
               color=(COLOR_GAIN, COLOR_LOSS), s=80, zorder=2)

    ax.plot(names, (exemplary_d[GAIN], exemplary_d[LOSS]), color="black",
            zorder=1, alpha=0.5, linestyle='--')
    ax.set_xlabel("\nLotteries potential outputs",
                  fontsize=axis_label_font_size)

    ax.tick_params(axis='both', labelsize=ticks_font_size)

    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_ylabel(
        "F(Choose riskiest option)",
        fontsize=axis_label_font_size)

    p = exemplary_d['stats']['p']
    str_p = f"{p:.3f}" if p >= 0.001 else " < 0.001"

    txt = \
        r"$\chi^2=" + f"{exemplary_d['stats']['val']:.2f}$\n" + \
        f"$p={str_p}$"

    ax.text(0.1, 0.9, txt,
            horizontalalignment='left',
            verticalalignment='center',
            transform=ax.transAxes)

    ax.set_aspect(2)


# def exemplary_case(d, monkey, pdf=None):
#
#     fig, ax = plt.subplots(figsize=(6, 5), dpi=200)
#
#     log(f"Stats for exemplary case - {monkey}...",
#         name=NAME)
#
#     ex_d = experimental_data.filter.exemplary.get_exemplary_case(d)
#     if ex_d is None:
#         log(f"[{NAME}] "
#             f"No data available I can not plot '{FIG_EXEMPLARY_CASE}'.",
#             name="WARNING")
#         return
#
#     _plot(
#         exemplary_d=ex_d,
#         color_gain=COLOR_GAIN,
#         color_loss=COLOR_LOSS,
#         ax=ax
#     )
#
#     save_fig(fig_type=FIG_EXEMPLARY_CASE, fig=fig, pdf=pdf, monkey=monkey)
