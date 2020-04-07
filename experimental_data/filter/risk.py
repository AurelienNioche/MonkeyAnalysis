import numpy as np

from parameters.parameters import LEFT, RIGHT
from utils.log import log
from .tools import _expected_value

from . gain_vs_loss import _gains_only, _losses_only


NAME = "experimental_data.filter.risk"


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


def _choose_risky(d, t, risky):
    return int(d.choice[t] == (risky == RIGHT))


def get_risky_safe_option(d, t):

    if _riskiest_option_on_left(d, t):
        risky, safe = LEFT, RIGHT

    elif _riskiest_option_on_right(d, t):
        risky, safe = RIGHT, LEFT

    else:
        risky, safe = None, None

    return risky, safe


def get_choose_risky(d):

    alternatives = []
    choose_risky = []

    n_trials = len(d.p.left)

    for t in range(n_trials):

        risky, safe = get_risky_safe_option(d=d, t=t)
        if risky is None:
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


def get_choose_risky_loss_or_gain_only(d, gain_only):

    results = {}

    n_trials = len(d.p.left)

    for t in range(n_trials):

        if not (
                (gain_only and _gains_only(d, t)) or
                (not gain_only and _losses_only(d, t))):
            continue

        if _riskiest_option_on_left(d, t):
            risky, safe = LEFT, RIGHT

        elif _riskiest_option_on_right(d, t):
            risky, safe = RIGHT, LEFT

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
        # p = scipy.stats.binom.pmf(k=np.sum(exemplary_d[alt]),
        #                           n=len(exemplary_d[alt]), p=0.5)
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