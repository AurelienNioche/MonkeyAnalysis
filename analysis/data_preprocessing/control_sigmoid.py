import numpy as np

from analysis.sigmoid_fit.sigmoid_fit import sigmoid_fit
from analysis.parameters.parameters import CONTROL_CONDITIONS, SAME_P, SAME_X
from data_interface.models import Data


def get_control_sigmoid_data(monkey):

    print("Getting the control sigmoid data...", end=' ', flush=True)

    d_monkey = Data.objects.filter(monkey=monkey)

    data = {}

    for i, cd in enumerate(CONTROL_CONDITIONS):

        x = []
        y = []

        if cd == SAME_P:
            d_cond = d_monkey.filter(is_same_p=True)
        elif cd == SAME_X:
            d_cond = d_monkey.filter(is_same_x=True)
        else:
            raise ValueError(f"Control type not recognized: '{cd}'")

        unq_pairs = np.unique(d_cond.values_list('pair_id'))

        for p_id in unq_pairs:
            for side in (0, 1):

                d_pair_sided = d_cond.filter(pair_id=p_id, is_reversed=side)

                n_choose_right = d_pair_sided.filter(c=1).count()
                n = d_pair_sided.count()
                prop = n_choose_right/n

                first_pair = d_pair_sided[0]
                ev_right_minus_ev_left = \
                    (first_pair.x1 * first_pair.p1) \
                    - (first_pair.x0 * first_pair.p0)

                x.append(ev_right_minus_ev_left)
                y.append(prop)

        try:
            fit = sigmoid_fit(x=x, y=y)
        except RuntimeError as e:
            print(e)
            fit = None

        data[cd] = {'x': x, 'y': y, 'fit': fit}

    print("Done!")

    return data
