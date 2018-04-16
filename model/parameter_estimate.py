import numpy as np
import scipy.stats
import scipy.optimize

import data.filter
import data.manager

from utils import utils
from model import model


def objective(parameters, alternatives, n, k):

    negative_risk_aversion, positive_risk_aversion, distortion, precision = parameters

    if np.any(np.isnan(parameters)):
        return np.inf

    lls = 0

    for i, alt in enumerate(alternatives):

        (p0, m0), (p1, m1) = alt

        ki, ni, pi = k[i], n[i], model.get_p(
            p0, m0, p1, m1, negative_risk_aversion, positive_risk_aversion, distortion, precision)

        log_likelihood = scipy.stats.binom.logpmf(k=ki, n=ni, p=pi)

        if log_likelihood == -np.inf:
            lls = - np.inf
            break

        else:
            lls += log_likelihood

    return lls * -1


def objective_multi(parameters, alternatives, n, k):

    neg_risk_aversion, pos_risk_aversion, neg_distortion, pos_distortion, \
        neg_precision, pos_precision = parameters

    if np.any(np.isnan(parameters)):
        return np.inf

    lls = 0

    for i, alt in enumerate(alternatives):

        (p0, m0), (p1, m1) = alt

        ki, ni, pi = k[i], n[i], model.get_p2(
            p0, m0, p1, m1, neg_risk_aversion, pos_risk_aversion, neg_distortion, pos_distortion,
            neg_precision, pos_precision)

        log_likelihood = scipy.stats.binom.logpmf(k=ki, n=ni, p=pi)

        if log_likelihood == -np.inf:
            lls = - np.inf
            break

        else:
            lls += log_likelihood

    return lls * -1


def run(force=False):

    monkeys = "Havane", "Gladys"

    r = {i: {} for i in monkeys}

    for monkey in monkeys:

        d = data.manager.import_data(
            monkey=monkey, starting_point="2017-04-01", end_point=utils.today(),
            database_path="data/results.db", force=force)

        alternatives, n, k = data.filter.get_choose_risky(d)

        #
        # res = scipy.optimize.minimize(
        #     objective, np.array([0, 0, 0.5, 7]), args=(alternatives, n, k, ), bounds=
        #     ((-1, 1), (-1, 1), (0, 1), (0, 20)))  # method=SLSQP

        res = scipy.optimize.minimize(
            objective_multi, np.array([0, 0, 0.5, 0.5, 7, 7]), args=(alternatives, n, k, ), bounds=
            ((-1, 1), (-1, 1), (0, 1), (0, 1), (0, 20), (0, 20)))  # method=SLSQP

        neg_risk_aversion, pos_risk_aversion, neg_distortion, pos_distortion, \
            neg_precision, pos_precision = \
            res.x

        r[monkey]["neg_risk_aversion"] = neg_risk_aversion
        r[monkey]["pos_risk_aversion"] = pos_risk_aversion
        r[monkey]["neg_distortion"] = neg_distortion
        r[monkey]["pos_distortion"] = neg_distortion
        r[monkey]["neg_precision"] = neg_precision
        r[monkey]["pos_precision"] = pos_precision

        print(f"{monkey}: parameters = {res.x}")
        print(f"{monkey}: log-likelihood sum = {res.fun}")

    return r
