import numpy as np

from plot.tools.tools import add_text


def plot(ax, data, axis_label_font_size=20, ticks_label_size=14):
    """
    Produce the precision figure
    """

    n_points = 1000

    v_mean = np.mean(data['precision'])
    v_std = np.std(data['precision'])

    n_chunk = len(data['precision'])

    class_model = data['class_model']
    if class_model.__name__ == "DMSciReports":

        p0 = 0.5
        p1, x1 = 1., 0.25

        x0_equal_ev = x1 * (1 / p0)

        x0_list = np.linspace(x1 + 0.01, 1.00, n_points)

        x = x0_list / x1

        pairs = []

        for i, x0 in enumerate(x0_list):
            pairs.append({"p0": p0, "x0": x0, "p1": p1, "x1": x1})

        y = np.zeros((n_chunk, len(x)))

        for i_c in range(n_chunk):

            dm = class_model([data[k][i_c] for k in class_model.param_labels])

            for i_p, p in enumerate(pairs):
                y[i_c, i_p] = dm.p_choice(c=0, **p)

        dm = class_model([np.mean(data[k]) for k in class_model.param_labels])
        y_mean = np.zeros(len(x))
        for i_p, p in enumerate(pairs):
            y_mean[i_p] = dm.p_choice(c=0, **p)

        ax.axvline(x0_equal_ev / x1, alpha=0.5, linewidth=1, color='black',
                   linestyle='--', zorder=-10)

        x_label = r"$\frac{x_{risky}}{x_{safe}}$"
        y_label = "P(Choose risky option)"

    elif class_model.__name__ in ("AgentSoftmax", "AgentSide",
                                  "AgentSideAdditive"):

        fit_precision = data['precision']

        x = np.linspace(-1, 1, n_points)
        y = np.zeros((n_chunk, len(x)))
        for i_c in range(n_chunk):
            v = fit_precision[i_c]
            y[i_c] = class_model.softmax(x, v)

        y_mean = np.zeros(len(x))
        y_mean[:] = class_model.softmax(x, v_mean)

        ax.axvline(0, alpha=0.5, linewidth=1, color='black',
                   linestyle='--', zorder=-10)

        x_label = r"$SEU(L_{1}) - SEU(L_{2})$"
        y_label = "$P(Choose L_{1})$"

    else:
        raise ValueError

    for i_c in range(n_chunk):
        ax.plot(x, y[i_c], color='C0', linewidth=1, alpha=0.5)

    # show_average
    ax.plot(x, y_mean, color='C0', linewidth=3, alpha=1)

    add_text(ax, r'$\lambda=' + f'{v_mean:.2f}\pm{v_std:.2f}' + '$')

    # ax.set_xticks([0, 1, 2])
    ax.set_yticks([0, 0.5, 1])

    # ax.set_xlim(0.0, 2.01)
    ax.set_ylim(-0.01, 1.01)

    ax.tick_params(axis='both', labelsize=ticks_label_size)

    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['top'].set_color('none')

    ax.axhline(0.5, alpha=0.5, linewidth=1, color='black',
               linestyle='--', zorder=-10)

    ax.set_xlabel(x_label, fontsize=axis_label_font_size)
    ax.set_ylabel(y_label, fontsize=axis_label_font_size)
