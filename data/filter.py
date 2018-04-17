import numpy as np
import pandas as pd
import scipy.stats

from utils.utils import log

name = 'DataFilter'


def _equal_expected_value(d, t):
    return \
        d.p.left[t] * \
        d.x.left[t] == \
        d.p.right[t] * \
        d.x.right[t]


def _certain_option(d, t):
    return d.p.left[t] == 1. or d.p.right[t] == 1.


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


def _fixed_p(d, t):

    return d.p.left[t] == d.p.right[t]


def _fixed_x(d, t):

    return d.x.left[t] == d.x.right[t]


def _best_option_on_left(d, t, condition):

    if condition in \
            ("identical p, positive vs negative x0",
             "identical p, negative x0",
             "identical p, positive x0"):
        return d.x.left[t] > d.x.right[t]

    elif condition == "identical x, negative x0":
        return d.p.left[t] < d.p.right[t]

    elif condition == "identical x, positive x0":
        return d.p.left[t] > d.p.right[t]

    else:
        raise Exception("Condition not understood.")


def _hit(d, t, best_option):
    return d.choice[t] == (best_option == 'right')


def _choose_risky(d, t, risky):
    return int(d.choice[t] == (risky == "right"))


def _best_option(d, t, condition):

    best_is_left = _best_option_on_left(d, t, condition)
    return "left" if best_is_left else "right"


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
            type_of_control = "identical p, positive x0"

        elif _losses_only(d, t):
            type_of_control = "identical p, negative x0"

        else:
            type_of_control = "identical p, positive vs negative x0"

    elif _fixed_x(d, t):

        if _gains_only(d, t):
            type_of_control = "identical x, positive x0"

        elif _losses_only(d, t):
            type_of_control = "identical x, negative x0"

        else:
            raise Exception("Revise your logic!")

    return type_of_control


def _expected_value(lottery):
    return lottery[0] * lottery[1]


def get_control(d):

    control_conditions = [
        "identical p, positive vs negative x0",
        "identical p, positive x0",
        "identical p, negative x0",
        "identical x, positive x0",
        "identical x, negative x0"
    ]

    sorted_data = {i: {} for i in control_conditions}

    n_trials = len(d.p.left)

    for t in range(n_trials):
        control_type = _type_of_control(d, t)

        if control_type is None:
            continue

        best_option = _best_option(d, t, control_type)
        is_a_hit = _hit(d, t, best_option)
        alternative = _control_alternative(d, t, best_option)

        if alternative not in sorted_data[control_type].keys():
            sorted_data[control_type][alternative] = []

        sorted_data[control_type][alternative].append(is_a_hit)

    results = {i: {} for i in control_conditions}

    for cond in sorted_data.keys():

        log("Condition '{}'.".format(cond), name)

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

            log("{} {}: mean {}, n {}".format(i, alt, mean, n), name)

        # noinspection PyTypeChecker
        perc_75, perc_25 = np.percentile(means, [75, 25])

        log("Number of pairs of lotteries: {}".format(len(n_trials)), name)

        log("The median of frequencies for {}: {:.02f} (IQR = {:.02f} -- {:.02f})"
            .format(cond, np.median(means), perc_25, perc_75), name)

        log("A few other stats about the number of trials for a specific pair", name)

        log("Min: {}".format(np.min(n_trials)), name)
        log("Max: {}".format(np.max(n_trials)), name)
        log("Median: {}".format(np.median(n_trials)), name)
        log("Mean: {}".format(np.mean(n_trials)), name)
        log("Std: {}".format(np.std(n_trials)), name)
        log("Sum: {}".format(np.sum(n_trials)), name)

    return results


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

        choose_risky = _choose_risky(d, t, risky)

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


def get_exemplary_case(d):

        sorted_data = {"losses": {}, "gains": {}, "n_trials": 0}

        n_trials = len(d.p.left)

        for t in range(n_trials):

            if not _certain_option(d, t):
                continue

            if not _equal_expected_value(d, t):
                continue

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

            choose_risky = _choose_risky(d, t, risky)

            if _gains_only(d, t):
                cond = "gains"

            elif _losses_only(d, t):
                cond = "losses"

            else:
                continue

            if alternative not in sorted_data[cond].keys():
                sorted_data[cond][alternative] = []

            sorted_data[cond][alternative].append(choose_risky)

            sorted_data["n_trials"] += 1

        # ---------------- #

        conditions = ("gains", "losses")

        # For plot
        results = {}

        # For Chi2
        data_frames = dict()

        for c in conditions:

            pairs = list(sorted_data[c].keys())
            log("For condition {}, I got {} pair(s) of lotteries ({}).".format(c, len(pairs), pairs), name)

            assert len(pairs) == 1, 'I expected only one pair of lotteries to meet the conditions.'

            chosen = sorted_data[c][pairs[0]]

            mean = np.mean(chosen)
            n = len(chosen)
            results[c] = mean

            log("Observed freq is {:.2f} ({} trials)".format(mean, n), name)

            # For Chi2
            n_hit = np.sum(chosen)

            data_frames[c] = pd.DataFrame(["yes"] * n_hit + ["no"] * (n - n_hit))
            data_frames[c] = pd.crosstab(index=data_frames[c][0], columns="count")

        # log(data_frames)

        first_sample = data_frames["gains"]
        second_sample = data_frames["losses"]

        observed = first_sample
        expected = second_sample/len(second_sample) * len(first_sample)

        chi_squared_stat = (((observed - expected) ** 2) / expected).sum()

        log("Chi squared stat: {}".format(chi_squared_stat["count"]), name)

        crt = scipy.stats.chi2.ppf(
            q=0.95,  # Find the critical value for 95% confidence*
            df=1)  # Df = number of variable categories - 1

        log("Critical value: {}".format(crt), name)

        # Find the p-value
        p_value = 1 - scipy.stats.chi2.cdf(
            x=chi_squared_stat,
            df=1)

        log("P value: {}".format(p_value[0]), name)

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
            risky, safe = "left", "right"

        elif _riskiest_option_on_right(d, t):
            risky, safe = "right", "left"

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
    risky_choice_means = []
    n_trials = []

    log("Pairs of lotteries used:", name)

    for i, alt in enumerate(alternatives):
        delta = _expected_value(alt[0]) - _expected_value(alt[1])
        expected_values_differences.append(delta)

        mean = np.mean(results[alt])
        risky_choice_means.append(mean)

        n = len(results[alt])

        n_trials.append(n)

        log("({}) {} delta: {}, mean: {}, n: {}".format(i, alt, delta, ", mean: ", mean, ", n:", n),
            name)

    log("Number of pairs of lotteries: {}".format(len(n_trials)), name)

    log("A few stats about the number of trials for a specific pair", name)

    log("Min: {}".format(np.min(n_trials)), name)
    log("Max: {}".format(np.max(n_trials)), name)
    log("Median {}:".format(np.median(n_trials)), name)
    log("Mean: {}".format(np.mean(n_trials)), name)
    log("Std: {}".format(np.std(n_trials)), name)
    log("Sum: {}".format(np.sum(n_trials)), name)

    return expected_values_differences, risky_choice_means
