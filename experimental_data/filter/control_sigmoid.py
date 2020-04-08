import numpy as np

from sigmoid_fit.sigmoid_fit import sigmoid_fit
from utils.log import log

from parameters.parameters import CONTROL_CONDITIONS


NAME = "experimental_data.filter.control_sigmoid"


def diff_ev_right_left(alternative):
    return \
        alternative[1][0] * alternative[1][1] \
        - alternative[0][0] * alternative[0][1]


def get(alternatives_sided, control_types, choose_right):

    uniq_alternatives = []
    cont_type_for_uniq_alt = []
    x_values = []
    y_values = []
    for i in range(len(alternatives_sided)):
        alt = alternatives_sided[i]
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

    data = {}

    for i, cd in enumerate(CONTROL_CONDITIONS):

        relevant = cont_type_for_uniq_alt == cd
        x = x_values[relevant]
        y = y_values[relevant]

        try:
            fit = sigmoid_fit(x=x, y=y)
        except RuntimeError as e:
            log(e, NAME)
            fit = None

        data[cd] = {'x': x.copy(), 'y': y.copy(), 'fit': fit}

    return data
