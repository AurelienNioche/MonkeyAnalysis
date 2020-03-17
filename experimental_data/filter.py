import numpy as np
import pandas as pd
import scipy.stats

from utils.log import log

NAME = 'experimental_data.filter'

control_conditions = [
        'identical p, positive vs negative x0',
        'identical p, positive x0',
        'identical p, negative x0',
        'identical x, positive x0',
        'identical x, negative x0'
    ]


def _equal_expected_value(d, t):
    return d.p.left[t] * d.x.left[t] == \
           d.p.right[t] * d.x.right[t]


def _certain_option(d, t):
    return d.p.left[t] == 1. or d.p.right[t] == 1.


def _losses_only(d, t):
    return d.x.left[t] < 0 and d.x.right[t] < 0


def _gains_only(d, t):
    return d.x.left[t] > 0 and d.x.right[t] > 0


def _riskiest_option_on_left(d, t):

    if _gains_only(d, t) or _losses_only(d, t):
        return d.p.left[t] < d.p.right[t] \
               and np.abs(d.x.left[t]) > np.abs(d.x.right[t])

    else:
        return False


def _riskiest_option_on_right(d, t):

    if _gains_only(d, t) or _losses_only(d, t):
        return d.p.left[t] > d.p.right[t] \
               and np.abs(d.x.left[t]) < np.abs(d.x.right[t])

    else:
        return False


def _fixed_p(d, t):
    return d.p.left[t] == d.p.right[t]


def _fixed_x(d, t):
    return d.x.left[t] == d.x.right[t]


def _best_option_on_left(d, t, condition):

    if condition in \
            ('identical p, positive vs negative x0',
             'identical p, negative x0',
             'identical p, positive x0'):
        return d.x.left[t] > d.x.right[t]

    elif condition == 'identical x, negative x0':
        return d.p.left[t] < d.p.right[t]

    elif condition == 'identical x, positive x0':
        return d.p.left[t] > d.p.right[t]

    else:
        raise Exception('Condition not understood.')


def _hit(d, t, best_option):
    return d.choice[t] == (best_option == 'right')


def _choose_risky(d, t, risky):
    return int(d.choice[t] == (risky == 'right'))


def _best_option(d, t, condition):

    best_is_left = _best_option_on_left(d, t, condition)
    return 'left' if best_is_left else 'right'


def _control_alternative(d, t, best_option):
    
    if best_option == 'left':
        alternative = (
            (d.p.left[t], d.x.left[t]),
            (d.p.right[t], d.x.right[t])
        )

    else:
        alternative = (
            (d.p.right[t], d.x.right[t]),
            (d.p.left[t], d.x.left[t])
        )
        
    return alternative


def _type_of_control(d, t):

    type_of_control = None

    if _fixed_p(d, t):

        if _gains_only(d, t):
            type_of_control = 'identical p, positive x0'

        elif _losses_only(d, t):
            type_of_control = 'identical p, negative x0'

        else:
            type_of_control = 'identical p, positive vs negative x0'

    elif _fixed_x(d, t):

        if _gains_only(d, t):
            type_of_control = 'identical x, positive x0'

        elif _losses_only(d, t):
            type_of_control = 'identical x, negative x0'

        else:
            raise Exception('Revise your logic!')

    return type_of_control


def _expected_value(lottery):
    return lottery[0] * lottery[1]


def get_control(d):

    alternatives = []
    control_types = []
    hits = []

    n_trials = len(d.p.left)

    for t in range(n_trials):
        ct = _type_of_control(d, t)

        if ct is None:
            continue

        best_option = _best_option(d, t, ct)
        hit = _hit(d, t, best_option)
        alt = _control_alternative(d, t, best_option)

        alternatives.append(alt)
        control_types.append(ct)
        hits.append(hit)

    return alternatives, control_types, hits


def cluster_hit_by_control_cond(alternatives, control_types, hits):

    sorted_data = {i: {} for i in control_conditions}

    for alt, ct, hit in zip(alternatives, control_types, hits):

        if alt not in sorted_data[ct].keys():
            sorted_data[ct][alt] = []

        sorted_data[ct][alt].append(hit)

    results = {i: {} for i in control_conditions}

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


def get_choose_risky(d):

    alternatives = []
    choose_risky = []

    n_trials = len(d.p.left)

    for t in range(n_trials):

        if _riskiest_option_on_left(d, t):
            risky, safe = 'left', 'right'

        elif _riskiest_option_on_right(d, t):
            risky, safe = 'right', 'left'

        else:
            continue

        alt = (
            (getattr(d.p, risky)[t], getattr(d.x, risky)[t]),
            (getattr(d.p, safe)[t], getattr(d.x, safe)[t]),
        )

        cr = _choose_risky(d, t, risky)

        alternatives.append(alt)
        choose_risky.append(cr)

    return np.asarray(alternatives), np.asarray(choose_risky)


def cluster_risky_choice_by_alternative(alternatives, choose_risky):

    unique_alt = [(tuple(i[0]), tuple(i[1]))
                  for i in np.unique(alternatives, axis=0)]
    results = {i: [] for i in unique_alt}

    alternatives = [(tuple(i[0]), tuple(i[1])) for i in alternatives]

    for alt, cr in zip(alternatives, choose_risky):
        results[alt].append(cr)

    n = np.zeros(len(unique_alt), dtype=int)
    k = np.zeros(len(unique_alt), dtype=int)

    for i, alt in enumerate(unique_alt):
        n[i] = len(results[alt])
        k[i] = sum(results[alt])

    return unique_alt, n, k


def get_exemplary_case(d):

    log('Getting data for exemplary case...', NAME)

    sorted_data = {'losses': {}, 'gains': {}, 'n_trials': 0}

    n_trials = len(d.p.left)

    for t in range(n_trials):

        if not _certain_option(d, t):
            continue

        if not _equal_expected_value(d, t):
            continue

        if _riskiest_option_on_left(d, t):
            risky, safe = 'left', 'right'

        elif _riskiest_option_on_right(d, t):
            risky, safe = 'right', 'left'

        else:
            continue

        alternative = (
            (getattr(d.p, risky)[t], getattr(d.x, risky)[t]),
            (getattr(d.p, safe)[t], getattr(d.x, safe)[t]),
        )

        choose_risky = _choose_risky(d, t, risky)

        if _gains_only(d, t):
            cond = 'gains'

        elif _losses_only(d, t):
            cond = 'losses'

        else:
            continue

        if alternative not in sorted_data[cond].keys():
            sorted_data[cond][alternative] = []

        sorted_data[cond][alternative].append(choose_risky)

        sorted_data['n_trials'] += 1

    # ---------------- #

    conditions = ('gains', 'losses')

    # For plot
    results = {}

    # For Chi2
    data_frames = dict()

    for c in conditions:

        pairs = list(sorted_data[c].keys())
        log(f'For condition "{c}", '
            f'I got {len(pairs)} pair(s) of lotteries ({pairs}).', NAME)

        if len(pairs) != 1:

            log(
                f'[{NAME}] Exemplary case: '
                f'I expected one (and only one) pair of lotteries to meet '
                f'the conditions but I got {len(pairs)} instead.',
                name="WARNING")
            return None

        chosen = sorted_data[c][pairs[0]]

        mean = np.mean(chosen)
        n = len(chosen)
        results[c] = mean

        log(f'Observed freq is {mean:.2f} ({n} trials)', NAME)

        # For Chi2
        n_hit = np.sum(chosen)

        data_frames[c] = pd.DataFrame(['yes'] * n_hit + ['no'] * (n - n_hit))
        data_frames[c] = pd.crosstab(index=data_frames[c][0], columns='count')

    first_sample = data_frames['gains']
    second_sample = data_frames['losses']

    observed = first_sample
    expected = second_sample/len(second_sample) * len(first_sample)

    chi_squared_stat = (((observed - expected) ** 2) / expected).sum()

    crt = scipy.stats.chi2.ppf(
        q=0.95,  # Find the critical value for 95% confidence*
        df=1)  # Df = number of variable categories - 1

    # Find the p-value
    p_value = 1 - scipy.stats.chi2.cdf(
        x=chi_squared_stat,
        df=1)

    log(f'Chi squared stat: {chi_squared_stat["count"]}', NAME)
    log(f'Critical value: {crt}', NAME)
    log(f'P value: {p_value[0]}\n', NAME)

    return results


def get_choose_risky_loss_or_gain_only(d, gain_only):

    results = {}

    n_trials = len(d.p.left)

    for t in range(n_trials):

        if not (
                (gain_only and _gains_only(d, t)) or
                (not gain_only and _losses_only(d, t))):
            continue

        if _riskiest_option_on_left(d, t):
            risky, safe = 'left', 'right'

        elif _riskiest_option_on_right(d, t):
            risky, safe = 'right', 'left'

        else:
            continue

        alternative = (
            (getattr(d.p, risky)[t], getattr(d.x, risky)[t]),
            (getattr(d.p, safe)[t], getattr(d.x, safe)[t]),
        )

        choose_risky = _choose_risky(d, t, risky)

        if alternative not in results.keys():
            results[alternative] = []

        results[alternative].append(choose_risky)

    alternatives = sorted(results.keys())

    expected_values_differences = []
    means = []
    n_trials = []

    log('Pairs of lotteries used:', NAME)

    for i, alt in enumerate(alternatives):
        delta = _expected_value(alt[0]) - _expected_value(alt[1])
        expected_values_differences.append(delta)

        mean = np.mean(results[alt])
        means.append(mean)

        n = len(results[alt])

        n_trials.append(n)
        log(f'({i}) {alt} delta: {delta}, mean: {mean:.2f}, n: {n}', NAME)

        # # -------------------- #
        #
        # p = scipy.stats.binom.pmf(k=np.sum(results[alt]),
        #                           n=len(results[alt]), p=0.5)
        # log(f'P sample if random DM (binomial law): {p:.03f}', "Stats")
        #
        # # -------------------- #

    # fake_means = [np.mean(np.random.randint(2, size=i)) for i in n_trials]
    # u, p = scipy.stats.mannwhitneyu(means, fake_means)
    # log(f'Different from random: u= {u:.02f}, p={p:.03f}', "Stats")

    log(f'Number of pairs of lotteries for risky choices '
        f'(gains only = {gain_only}): {len(n_trials)}', NAME)
    log(f'Min: {np.min(n_trials)}', NAME)
    log(f'Max: {np.max(n_trials)}', NAME)
    log(f'Median: {np.median(n_trials):.2f}', NAME)
    log(f'Mean: {np.mean(n_trials):.2f}', NAME)
    log(f'Std: {np.std(n_trials):.2f}', NAME)
    log(f'Sum: {np.sum(n_trials)}\n', NAME)

    return expected_values_differences, means


def control_history_sort_data(alternatives, control_types, hits, n_chunk):

    # Pre-sort data
    sorted_data = {i: {} for i in control_conditions}

    for alt, ct, hit in zip(alternatives, control_types, hits):

        if alt not in sorted_data[ct].keys():
            sorted_data[ct][alt] = []

        sorted_data[ct][alt].append(hit)

    # Prepare container for output
    results = {i: [{} for _ in range(n_chunk)] for i in control_conditions}

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
