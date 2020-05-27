def scatter_and_sigmoid(ax, x, y, x_fit, y_fit, color='C0', label=None,
                        line_width=3, point_size=100, alpha_scatter=0.5):

    if label is not None:
        label = label.capitalize()

    if x_fit is not None and y_fit is not None:

        ax.plot(x_fit, y_fit, color=color, linewidth=line_width, label=label)

    ax.scatter(x, y, color=color, alpha=alpha_scatter, s=point_size)


def add_text(ax, txt,):
    ax.text(0.05, 0.9, txt,
            horizontalalignment='left',
            verticalalignment='top',
            transform=ax.transAxes)