import numpy as np

from experimental_data.filter.risk import _gains_only, _riskiest_option_on_right, _riskiest_option_on_left, _choose_risky
from experimental_data.filter.tools import _expected_value
from sigmoid_fit.sigmoid_fit import sigmoid_fit

from utils.log import log

from parameters.parameters import LEFT, RIGHT


NAME = "experimental_data.filter.freq_risk_against_exp_value"


def _analyse(d, verbose):

    results = {}

    n_trials = len(d.p.left)

    for t in range(n_trials):

        if _gains_only(d=d, t=t):

            if _riskiest_option_on_left(d=d, t=t):
                risky, safe = LEFT, RIGHT

            elif _riskiest_option_on_right(d=d, t=t):
                risky, safe = RIGHT, LEFT

            else:
                continue
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

    if verbose:
        log(
            f"Stats for risk against exp value:", name=NAME)
        log('Pairs of lotteries used:', NAME)

    for i, alt in enumerate(alternatives):
        delta = _expected_value(alt[0]) - _expected_value(alt[1])
        expected_values_differences.append(delta)

        mean = np.mean(results[alt])
        means.append(mean)

        n = len(results[alt])

        n_trials.append(n)
        if verbose:
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

    if verbose:
        log(f'Number of pairs of lotteries for risky choices: {len(n_trials)}', NAME)
        log(f'Min: {np.min(n_trials)}', NAME)
        log(f'Max: {np.max(n_trials)}', NAME)
        log(f'Median: {np.median(n_trials):.2f}', NAME)
        log(f'Mean: {np.mean(n_trials):.2f}', NAME)
        log(f'Std: {np.std(n_trials):.2f}', NAME)
        log(f'Sum: {np.sum(n_trials)}\n', NAME)
        print()

    return expected_values_differences, means


def get(d, verbose=True):

    x, y = _analyse(d, verbose=verbose)

    try:
        fit = sigmoid_fit(x=x, y=y)

    except RuntimeError as e:
        log(e, NAME)
        fit = None

    data = {'x': x, 'y': y, 'fit': fit}

    return data
