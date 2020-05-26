import numpy as np

from parameters.parameters import LEFT, RIGHT
from utils.log import log
from .tools import _expected_value, _losses_only, _gains_only

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


# def get_choose_risky_loss_or_gain_only(d, gain_only, verbose=True):
#




# def get_choose_risky(d):
#
#     alternatives = []
#     choose_risky = []
#
#     n_trials = len(d.p.left)
#
#     for t in range(n_trials):
#
#         risky, safe = get_risky_safe_option(d=d, t=t)
#         if risky is None:
#             continue
#
#         alt = (
#             (getattr(d.p, risky)[t], getattr(d.x, risky)[t]),
#             (getattr(d.p, safe)[t], getattr(d.x, safe)[t]),
#         )
#
#         cr = _choose_risky(d, t, risky)
#
#         alternatives.append(alt)
#         choose_risky.append(cr)
#
#     return np.asarray(alternatives), np.asarray(choose_risky)


# def cluster_risky_choice_by_alternative(alternatives, choose_risky):
#
#     unique_alt = [(tuple(i[0]), tuple(i[1]))
#                   for i in np.unique(alternatives, axis=0)]
#     results = {i: [] for i in unique_alt}
#
#     alternatives = [(tuple(i[0]), tuple(i[1])) for i in alternatives]
#
#     for alt, cr in zip(alternatives, choose_risky):
#         results[alt].append(cr)
#
#     n = np.zeros(len(unique_alt), dtype=int)
#     k = np.zeros(len(unique_alt), dtype=int)
#
#     for i, alt in enumerate(unique_alt):
#         n[i] = len(results[alt])
#         k[i] = sum(results[alt])
#
#     return unique_alt, n, k
