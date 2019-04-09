import numpy as np
import pickle
import os
import scipy.stats
import scipy.optimize

import data.filter

from utils.utils import log
from model import model

NAME = 'ParameterEstimate'
BACKUP_FOLDER = "model/pickle"

os.makedirs(BACKUP_FOLDER, exist_ok=True)


def _objective(parameters, alternatives, n, k):

    neg_risk_aversion, pos_risk_aversion, neg_distortion, pos_distortion, \
        neg_precision, pos_precision = parameters

    if np.any(np.isnan(parameters)):
        return np.inf

    lls = 0

    for i, alt in enumerate(alternatives):

        (p0, m0), (p1, m1) = alt

        ki, ni, pi = k[i], n[i], model.get_p_multi(
            p0, m0, p1, m1, neg_risk_aversion, pos_risk_aversion, neg_distortion, pos_distortion,
            neg_precision, pos_precision)

        log_likelihood = scipy.stats.binom.logpmf(k=ki, n=ni, p=pi)

        if log_likelihood == -np.inf:
            lls = - np.inf
            break

        else:
            lls += log_likelihood

    return lls * -1


def _get_cross_validation(d, randomize, n_chunk,
                          bounds=((-0.99, 0.99), (-0.99, 0.99), (0.01, 1), (0.01, 1), (0, 5), (0, 5)),
                          init_guess=None,
                          method='evolutionary'):

    monkeys = d.keys()

    fit = {i: {} for i in monkeys}

    for monkey in monkeys:

        log(f'Getting fit for {monkey}...', NAME)

        alternatives, choose_risky = data.filter.get_choose_risky(d[monkey])

        n_trials = len(alternatives)
        reminder = n_trials % n_chunk

        idx = np.arange(n_trials)
        if randomize:
            np.random.shuffle(idx)

        if reminder > 0:
            idx = idx[:-reminder]

        parts = np.split(idx, n_chunk)

        log(f'Order of trials for composing is {"chronological" if not randomize else "randomized"}', NAME)
        log(f'N trials = {n_trials}', NAME)
        log(f'N parts = {len(parts)} (n trials per part = {int(n_trials / n_chunk)}, '
            f'reminder = {reminder})', NAME)

        for label in [
                'pos_risk_aversion', 'neg_risk_aversion', 'pos_distortion', 'neg_distortion',
                'pos_precision', 'neg_precision', 'log_likelihood_sum']:
            fit[monkey][label] = []

        for p in parts:

            alt, n, k = data.filter.cluster_risky_choice_by_alternative(
                alternatives[p], choose_risky[p])

            args = (alt, n, k,)

            if method == "SLSQP":

                if init_guess is None:
                    init_guess = np.array([0, 0, 0.5, 0.5, 1, 1])
                res = scipy.optimize.minimize(
                    _objective, init_guess, args=args,
                    bounds=bounds)  # method=SLSQP

            elif method == "evolutionary":
                if init_guess is not None:
                    raise AttributeError("Method '{}' can not handle an initial guess")
                res = scipy.optimize.differential_evolution(
                    func=_objective, args=args, bounds=bounds)

            else:
                raise NotImplementedError(f"Method '{method}' is not implemented")

            nra, pra, ndi, pdi, npr, ppr = res.x
            lls = res.fun * -1

            fit[monkey]['neg_risk_aversion'].append(nra)
            fit[monkey]['pos_risk_aversion'].append(pra)
            fit[monkey]['neg_distortion'].append(ndi)
            fit[monkey]['pos_distortion'].append(pdi)
            fit[monkey]['neg_precision'].append(npr)
            fit[monkey]['pos_precision'].append(ppr)
            fit[monkey]['log_likelihood_sum'].append(lls)

        for label in [
                'pos_risk_aversion', 'neg_risk_aversion', 'pos_distortion', 'neg_distortion',
                'pos_precision', 'neg_precision', 'log_likelihood_sum']:
            log(f'{label} = {np.mean(fit[monkey][label]):.2f} '
                f'(+/-{np.std(fit[monkey][label]):.2f} SD)', NAME)

    return fit


def _pickle_load(d, force, randomize, n_chunk, method):

    randomize_str = "random_order" if randomize else "chronological_order"
    fit_path = f'{BACKUP_FOLDER}/fit_{randomize_str}_{n_chunk}chunk_{method}.p'

    if not os.path.exists(fit_path) or force:

        fit = _get_cross_validation(d, randomize=randomize, n_chunk=n_chunk, method=method)

        os.makedirs(os.path.dirname(fit_path), exist_ok=True)
        with open(fit_path, 'wb') as f:
            pickle.dump(fit, f)

    else:
        with open(fit_path, 'rb') as f:
            fit = pickle.load(f)

    return fit


def run_cross_validation(d, n_chunk=20, force=False, randomize=False, method='SLSQP'):

    fit = _pickle_load(d=d, force=force, randomize=randomize, n_chunk=n_chunk, method=method)

    for monkey in d.keys():
        log(f'{monkey}', NAME)
        for label in [
                'pos_risk_aversion', 'neg_risk_aversion', 'pos_distortion', 'neg_distortion',
                'pos_precision', 'neg_precision', 'log_likelihood_sum'
        ]:
            log(f'{label} = {np.mean(fit[monkey][label]):.2f} '
                f'(+/-{np.std(fit[monkey][label]):.2f} SD)', NAME)

    return fit
