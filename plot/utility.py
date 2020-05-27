import numpy as np

from plot.tools.tools import add_text


def _line(risk_aversion, class_model, ax, alpha=1.0,
          linewidth=3, color="C0", linestyle="-",
          reward_max=1,
          reward_min=0,
          n_points=1000):

    x = np.linspace(reward_min, reward_max, n_points)
    y = [class_model.u(x=i, risk_aversion=risk_aversion) for i in x]

    ax.plot(x, y, color=color, linewidth=linewidth, alpha=alpha,
            linestyle=linestyle)


def plot(ax, fit, show_average=True, alpha_chunk=0.5,
         axis_label_font_size=20,
         ticks_label_font_size=12):
    """
    Produce the utility function figure
    """

    pr = fit['risk_aversion']
    class_model = fit['class_model']

    for j in range(len(pr)):
        _line(
            class_model=class_model,
            risk_aversion=pr[j],
            ax=ax, linewidth=1, alpha=alpha_chunk,
        )

    if show_average:
        v = np.mean(pr)
        _line(
            risk_aversion=v,
            class_model=class_model,
            ax=ax
        )
        add_text(ax, r'$\omega=' + f'{v:.2f}' + '$')

    ax.spines['left'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_color('none')

    ax.set_ylim(0, 1)
    ax.set_xlim(0, 1)

    ax.plot((0, 1), (0, 1), alpha=0.5, linewidth=1, color='black',
            linestyle='--', zorder=-10)

    ax.set_xlabel("$x$", fontsize=axis_label_font_size)
    ax.set_ylabel("$u(x)$", fontsize=axis_label_font_size)

    ax.tick_params(axis='both', which='major', labelsize=ticks_label_font_size)
    ax.tick_params(axis='both', which='minor', labelsize=ticks_label_font_size)

    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])

    ax.set_aspect(1)
