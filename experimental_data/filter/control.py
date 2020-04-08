import numpy as np

from . gain_vs_loss import _gains_only, _losses_only
from parameters.parameters import CONTROL_CONDITIONS, SAME_P_GAIN, \
    SAME_P_LOSS, \
    SAME_P_GAIN_VS_LOSS, SAME_X0_GAIN, SAME_X0_LOSS, LEFT, RIGHT
from utils.log import log

NAME = "experimental_data.filter.control"


def _type_of_control(d, t):
    type_of_control = None

    if _fixed_p(d, t):

        if _gains_only(d, t):
            type_of_control = SAME_P_GAIN

        elif _losses_only(d, t):
            type_of_control = SAME_P_LOSS

        else:
            type_of_control = SAME_P_GAIN_VS_LOSS

    elif _fixed_x(d, t):

        if _gains_only(d, t):
            type_of_control = SAME_X0_GAIN

        elif _losses_only(d, t):
            type_of_control = SAME_X0_LOSS
        else:
            raise ValueError('Control type not recognized')

    return type_of_control


def _control_alternative(d, t, best_option):

    alternative_sided = (
        (d.p.left[t], d.x.left[t]),
        (d.p.right[t], d.x.right[t])
    )

    if best_option == LEFT:
        alternative = alternative_sided

    else:
        alternative = (alternative_sided[1],
                       alternative_sided[0])

    return alternative, alternative_sided


def _hit(d, t, best_option):
    return d.choice[t] == (best_option == RIGHT)


def _best_option(d, t, condition):
    best_is_left = _best_option_on_left(d, t, condition)
    return LEFT if best_is_left else RIGHT


def _fixed_p(d, t):
    return d.p.left[t] == d.p.right[t]


def _fixed_x(d, t):
    return d.x.left[t] == d.x.right[t]


def _best_option_on_left(d, t, condition):
    if condition in \
            (SAME_P_GAIN_VS_LOSS,
             SAME_P_LOSS,
             SAME_P_GAIN):
        return d.x.left[t] > d.x.right[t]

    elif condition == SAME_X0_LOSS:
        return d.p.left[t] < d.p.right[t]

    elif condition == SAME_X0_GAIN:
        return d.p.left[t] > d.p.right[t]

    else:
        raise Exception('Condition not understood.')


def sort_by_cond(alternatives, control_types, hits):

    sorted_data = {i: {} for i in CONTROL_CONDITIONS}

    for alt, ct, hit in zip(alternatives, control_types, hits):

        if alt not in sorted_data[ct].keys():
            sorted_data[ct][alt] = []

        sorted_data[ct][alt].append(hit)

    results = {i: {} for i in CONTROL_CONDITIONS}

    for cond in sorted_data.keys():

        log(f'Condition "{cond}"', NAME)

        data = sorted_data[cond]

        alternatives = sorted(list(data.keys()))

        n_trials = []
        means = []

        for i, alt in enumerate(alternatives):
            n = len(data[alt])
            mean = np.mean(data[alt])
            n_trials.append(n)

            results[cond][alt] = mean

            means.append(mean)

            log(f'{i} {alt}: mean {mean:.2f}, n {n}', NAME)

        # ----------------------------------------- #

        perc_75, perc_25 = np.percentile(means, [75, 25])

        log(f'Number of pairs of lotteries: {len(n_trials)}', NAME)

        log(f'The median of frequencies for {cond}: {np.median(means):.02f} '
            f'(IQR = {perc_25:.02f} -- {perc_75:.02f})', NAME)

        log('Number of trials for a specific pair:', NAME)

        log(f'Min: {np.min(n_trials)}', NAME)
        log(f'Max: {np.max(n_trials)}', NAME)
        log(f'Median: {np.median(n_trials):.2f}', NAME)
        log(f'Mean: {np.mean(n_trials):.2f}', NAME)
        log(f'Std: {np.std(n_trials):.2f}', NAME)
        log(f'Sum: {np.sum(n_trials)}\n', NAME)

    return results


def get_control(d):

    alternatives = []
    alternatives_sided = []
    control_types = []
    hits = []
    choose_right = []

    n_trials = len(d.p.left)

    for t in range(n_trials):
        ct = _type_of_control(d, t)

        if ct is None:
            continue

        best_option = _best_option(d, t, ct)
        hit = _hit(d, t, best_option)
        cr = d.choice[t]

        alt, alt_sided = _control_alternative(d, t, best_option)

        alternatives.append(alt)
        alternatives_sided.append(alt_sided)
        control_types.append(ct)
        hits.append(hit)
        choose_right.append(cr)

    return alternatives, alternatives_sided, control_types, hits, choose_right


def control_history_sort_data(alternatives, control_types, hits, n_chunk):

    # Pre-sort data
    sorted_data = {i: {} for i in CONTROL_CONDITIONS}

    for alt, ct, hit in zip(alternatives, control_types, hits):

        if alt not in sorted_data[ct].keys():
            sorted_data[ct][alt] = []

        sorted_data[ct][alt].append(hit)

    # Prepare container for output
    results = {i: [{} for _ in range(n_chunk)] for i in CONTROL_CONDITIONS}

    for cond in sorted_data.keys():

        # log(f'Condition "{cond}"', name=NAME)

        d = sorted_data[cond]
        alternatives = sorted(list(d.keys()))

        for i, alt in enumerate(alternatives):

            n_trials = len(d[alt])

            reminder = n_trials % n_chunk

            idx = np.arange(n_trials)
            if reminder > 0:
                idx = idx[:-reminder]

            split = np.split(np.asarray(d[alt])[idx], n_chunk)

            for j, sp in enumerate(split):
                # Skip empty slices
                if len(sp):
                    results[cond][j][alt] = np.mean(sp)

    return results
