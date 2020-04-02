"""
Produce the control sigmoid figures
"""

import numpy as np
import matplotlib.pyplot as plt

from utils.log import log
from plot.utils import save_fig

from parameters.parameters import FIG_CONTROL_SIGMOID, \
    COLOR_GAIN, COLOR_LOSS, CONTROL_CONDITIONS, \
    SIG_STEEP_SAME_P_GAIN_VS_LOSS,  \
    SIG_STEEP_SAME_P_GAIN, \
    SIG_STEEP_SAME_P_LOSS, \
    SIG_STEEP_SAME_X0_GAIN, \
    SIG_STEEP_SAME_X0_LOSS, \
    SIG_MID_SAME_P_GAIN_VS_LOSS, \
    SIG_MID_SAME_P_GAIN, \
    SIG_MID_SAME_P_LOSS, \
    SIG_MID_SAME_X0_GAIN, \
    SIG_MID_SAME_X0_LOSS, \
    SAME_P_GAIN_VS_LOSS, \
    SAME_P_GAIN, \
    SAME_P_LOSS, \
    SAME_X0_GAIN, \
    SAME_X0_LOSS

from sigmoid_fit.sigmoid_fit import sigmoid_fit

NAME = "plot.control"


def diff_ev_right_left(alternative):
    return \
        alternative[1][0] * alternative[1][1] \
        - alternative[0][0] * alternative[0][1]


def _plot(x_data, y_data, ax, color='C0',
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

    ax.scatter(x_data, y_data, color=color, alpha=0.5, s=point_size)

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


def control_sigmoid(alternatives, control_types, choose_right, monkey, pdf=None):

    uniq_alternatives = []
    cont_type_for_uniq_alt = []
    x_values = []
    y_values = []
    for i in range(len(alternatives)):
        alt = alternatives[i]
        if alt not in uniq_alternatives:
            uniq_alternatives.append(alt)

            ct = control_types[i]
            cont_type_for_uniq_alt.append(ct)
            y_values.append([])

            x = diff_ev_right_left(alt)
            x_values.append(x)

        y_values[uniq_alternatives.index(alt)].append(choose_right[i])

    x_values = np.array(x_values)
    y_values = np.array([np.mean(i) for i in y_values])
    cont_type_for_uniq_alt = np.array(cont_type_for_uniq_alt)

    x_data = {}
    y_data = {}
    x_fit = {}
    y_fit = {}

    fit = {}

    for i, cd in enumerate(CONTROL_CONDITIONS):

        relevant = cont_type_for_uniq_alt == cd
        x_data_cd = x_values[relevant]
        y_data_cd = y_values[relevant]
        try:
            x_fit_cd, y_fit_cd, p_opt, stats_cond = \
                sigmoid_fit(x_data=x_data_cd, y_data=y_data_cd,
                            return_p_opt=True)

        except RuntimeError as e:
            log(e, NAME)
            x_fit_cd, y_fit_cd = None, None
            p_opt = None, None

        x_data[cd] = x_data_cd
        y_data[cd] = y_data_cd
        x_fit[cd] = x_fit_cd
        y_fit[cd] = y_fit_cd

        if cd == SAME_P_GAIN_VS_LOSS:
            fit[SIG_MID_SAME_P_GAIN_VS_LOSS], \
            fit[SIG_STEEP_SAME_P_GAIN_VS_LOSS] = p_opt

        elif cd == SAME_P_GAIN:
            fit[SIG_MID_SAME_P_GAIN], \
            fit[SIG_STEEP_SAME_P_GAIN] = p_opt

        elif cd == SAME_P_LOSS:
            fit[SIG_MID_SAME_P_LOSS], \
            fit[SIG_STEEP_SAME_P_LOSS] = p_opt

        elif cd == SAME_X0_GAIN:
            fit[SIG_MID_SAME_X0_GAIN], \
            fit[SIG_STEEP_SAME_X0_GAIN] = p_opt

        elif cd == SAME_X0_LOSS:
            fit[SIG_MID_SAME_X0_LOSS], \
            fit[SIG_STEEP_SAME_X0_LOSS] = p_opt

        else:
            raise ValueError(cd)

    colors = ["black", COLOR_GAIN, COLOR_LOSS, COLOR_GAIN, COLOR_LOSS]
    n_rows = 3
    fig, _axes = plt.subplots(figsize=(6, 5*n_rows), nrows=n_rows, dpi=200)

    axes = [_axes[0], _axes[1], _axes[1], _axes[2], _axes[2]]
    labels = [None, "Gain", "Loss", "Gain", "Loss"]
    titles = ["Gain vs loss", ] \
        + ["Same $p$ - Diff $x$", ] * 2 \
        + ["Same $x$ - Diff $p$", ] * 2

    for i, cd in enumerate(CONTROL_CONDITIONS):
        color = colors[i]
        _plot(x_data=x_data[cd],
              y_data=y_data[cd],
              x_fit=x_fit[cd],
              y_fit=y_fit[cd],
              color=color,
              title=titles[i],
              label=labels[i],
              ax=axes[i],
              x_label="$EV_{right} - EV_{left}$",
              y_label="F(Choose right)")

    save_fig(fig_type=FIG_CONTROL_SIGMOID, fig=fig, pdf=pdf, monkey=monkey)

    return fit
