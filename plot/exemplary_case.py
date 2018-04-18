
"""
Produce the the certainty-risk trade-off figure
"""


def plot(results, color_gain, color_loss, ax):

    axis_label_font_size = 14
    ticks_font_size = 14

    names = "Gain", "Loss"

    ax.scatter(names, (results["gains"], results["losses"]), color=(color_gain, color_loss), s=80, zorder=2)

    ax.plot(names, (results["gains"], results["losses"]), color="black", zorder=1, alpha=0.5, linestyle='--')
    ax.set_xlabel("\nLotteries potential outputs",  # \nMonkey {}.".format(monkey),
                  fontsize=axis_label_font_size)

    ax.tick_params(axis='both', labelsize=ticks_font_size)

    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_ylabel(
        "F(Choose riskiest option)",
        fontsize=axis_label_font_size)

    ax.set_aspect(2)
