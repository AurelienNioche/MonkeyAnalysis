import numpy as np
import pandas as pd
import scipy.stats

from experimental_data.filter.tools import _losses_only, _gains_only
from experimental_data.filter.risk import get_risky_safe_option, _choose_risky
from parameters.parameters import LOSS, GAIN
from utils.log import log

NAME = "experimental_data.filter.exemplary"


def _equal_expected_value(d, t):
    return d.p.left[t] * d.x.left[t] == \
           d.p.right[t] * d.x.right[t]


def _certain_option(d, t):
    return d.p.left[t] == 1. or d.p.right[t] == 1.


def get(d, verbose=True):

    if verbose:
        log('Getting data for exemplary case...', NAME)

    sorted_data = {LOSS: {}, GAIN: {}, 'n_trials': 0}

    n_trials = len(d.p.left)

    for t in range(n_trials):

        if not _certain_option(d, t):
            continue

        if not _equal_expected_value(d, t):
            continue

        risky, safe = get_risky_safe_option(d=d, t=t)

        if risky is None:
            continue

        alternative = (
            (getattr(d.p, risky)[t], getattr(d.x, risky)[t]),
            (getattr(d.p, safe)[t], getattr(d.x, safe)[t]),
        )

        choose_risky = _choose_risky(d, t, risky)

        if _gains_only(d, t):
            cond = GAIN

        elif _losses_only(d, t):
            cond = LOSS

        else:
            continue

        if alternative not in sorted_data[cond].keys():
            sorted_data[cond][alternative] = []

        sorted_data[cond][alternative].append(choose_risky)

        sorted_data['n_trials'] += 1

    # ---------------- #

    conditions = (GAIN, LOSS)

    # For plot
    results = {}

    # For Chi2
    data_frames = dict()

    for c in conditions:

        pairs = list(sorted_data[c].keys())

        if verbose:
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

        if verbose:
            log(f'Observed freq is {mean:.2f} ({n} trials)', NAME)

        # For Chi2
        n_hit = np.sum(chosen)

        data_frames[c] = pd.DataFrame(['yes'] * n_hit + ['no'] * (n - n_hit))
        data_frames[c] = pd.crosstab(index=data_frames[c][0], columns='count')

    first_sample = data_frames[GAIN]
    second_sample = data_frames[LOSS]

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
    p = p_value[0]
    chi = chi_squared_stat["count"]

    if verbose:
        log(f'Chi squared stat: {chi}', NAME)
        log(f'Critical value: {crt}', NAME)
        log(f'P value: {p}\n', NAME)

    results["stats"] = {
        "val": chi,
        "p": p
    }

    return results
