import numpy as np

from analysis.parameters.parameters import CONTROL_CONDITIONS, SAME_P, SAME_X
from data_interface.models import Data


def get_control_data(monkey):

    print("Getting the control data...", end=' ', flush=True)

    d_monkey = Data.objects.filter(monkey=monkey)

    data = {}
    for cd in CONTROL_CONDITIONS:

        data[cd] = []

        if cd == SAME_P:
            d_cd = d_monkey.filter(is_same_p=True)
        elif cd == SAME_X:
            d_cd = d_monkey.filter(is_same_x=True)
        else:
            raise ValueError(f"Control type not recognized: '{cd}'")

        unq_pairs = np.unique(d_cd.values_list('pair_id'))

        for p_id in unq_pairs:
            d_pair = d_cd.filter(pair_id=p_id)
            n_success = d_pair.filter(choose_best=True).count()
            n = d_pair.count()
            success_rate = n_success/n

            data[cd].append(success_rate)

    print("Done!")

    return data
