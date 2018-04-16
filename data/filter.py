import numpy as np


def _expected_value(lottery):
    return lottery[0] * lottery[1]


def _losses_only(d, t):
    return d.x.left[t] < 0 and d.x.right[t] < 0


def _gains_only(d, t):
    return d.x.left[t] > 0 and d.x.right[t] > 0


def _riskiest_option_on_left(d, t):
    if _gains_only(d, t) or _losses_only(d, t):

        return d.p.left[t] < d.p.right[t] and \
               np.absolute(d.x.left[t]) > np.absolute(d.x.right[t])

    else:
        return False


def _riskiest_option_on_right(d, t):

    if _gains_only(d, t) or _losses_only(d, t):

        return d.p.left[t] > d.p.right[t] and \
               np.absolute(d.x.left[t]) < np.absolute(d.x.right[t])

    else:
        return False


def get_choose_risky(d):

    results = {}

    n_trials = len(d.p.left)

    for t in range(n_trials):

        if _riskiest_option_on_left(d, t):
            risky, safe = "left", "right"

        elif _riskiest_option_on_right(d, t):
            risky, safe = "right", "left"

        else:
            continue

        alternative = (
            (getattr(d.p, risky)[t], getattr(d.x, risky)[t]),
            (getattr(d.p, safe)[t], getattr(d.x, safe)[t]),
        )

        choose_risky = int(d.choice[t] == (risky == "right"))

        if alternative not in results.keys():
            results[alternative] = []

        results[alternative].append(choose_risky)

    alternatives = sorted(results.keys())

    n = np.zeros(len(alternatives), dtype=int)
    k = np.zeros(len(alternatives), dtype=int)

    for i, alt in enumerate(alternatives):
        n[i] = len(results[alt])
        k[i] = sum(results[alt])

    return alternatives, n, k

