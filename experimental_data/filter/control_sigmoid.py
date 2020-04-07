import numpy as np

from sigmoid_fit.sigmoid_fit import sigmoid_fit
from utils.log import log

from parameters.parameters import \
    CONTROL_CONDITIONS, \
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
    SAME_X0_LOSS, \
    SIG_STEEP, \
    SIG_MID


NAME = "experimental_data.filter.control_sigmoid"


def diff_ev_right_left(alternative):
    return \
        alternative[1][0] * alternative[1][1] \
        - alternative[0][0] * alternative[0][1]


def get(alternatives, control_types, choose_right):

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

        fit[cd] = {
            SIG_MID: p_opt[SIG_MID],
            SIG_STEEP: p_opt[SIG_STEEP]
        }

    return {
        'x': x_data,
        'y': y_data,
        'x_fit': x_fit,
        'y_fit': y_fit,
        'fit': fit
    }
