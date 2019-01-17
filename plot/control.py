import numpy as np


def plot(results, color_gain, color_loss, ax):

    n = len(results.keys())

    tick_labels = [
        "Loss\nvs\ngains", "Diff. $x +$\nSame $p$", "Diff. $x -$\nSame $p$",
        "Diff. $p$\nSame $x +$", "Diff. $p$\nSame $x -$"]

    colors = ["black", color_gain, color_loss, color_gain, color_loss]
    positions = list(range(n))

    x_scatter = []
    y_scatter = []
    colors_scatter = []

    values_box_plot = []

    for i, cond in enumerate(results.keys()):

        values_box_plot.append([])

        for v in results[cond].values():
            # For box plot
            values_box_plot[-1].append(v)

            # For scatter
            y_scatter.append(v)
            x_scatter.append(i)
            colors_scatter.append(colors[i])

    fontsize = 10

    ax.scatter(x_scatter, y_scatter, c=colors_scatter, s=30, alpha=0.5, linewidth=0.0, zorder=1)

    ax.axhline(0.5, linestyle='--', color='0.3', zorder=-10, linewidth=0.5)

    ax.set_yticks(np.arange(0.4, 1.1, 0.2))

    ax.tick_params(axis='both', labelsize=fontsize)

    # ax.set_xlabel("Type of control\nMonkey {}.".format(monkey), fontsize=fontsize)
    # ax.set_xlabel("Control type", fontsize=fontsize)
    ax.set_ylabel("Success rate", fontsize=fontsize)

    ax.set_ylim(0.35, 1.02)

    # Boxplot
    bp = ax.boxplot(values_box_plot, positions=positions, labels=tick_labels, showfliers=False, zorder=2)

    for e in ['boxes', 'caps', 'whiskers', 'medians']:  # Warning: only one box, but several whiskers by plot
        for b in bp[e]:
            b.set(color='black')
            # b.set_alpha(1)

    ax.set_aspect(3)
