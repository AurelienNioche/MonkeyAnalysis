import numpy as np
import pickle
import os
import scipy.stats
import scipy.optimize

import experimental_data.filter
import experimental_data.filter.risk
from parameters.parameters import MODEL_PARAMETERS, BACKUP_FOLDER
from utils.log import log
from model import model

NAME = 'model.parameter_estimate'


def _objective(parameters, alternatives, n, k):

    neg_risk_aversion, pos_risk_aversion, neg_distortion, pos_distortion, \
        neg_precision, pos_precision = parameters

    if np.any(np.isnan(parameters)):
        return np.inf

    lls = 0

    for i, alt in enumerate(alternatives):

        (p0, m0), (p1, m1) = alt

        ki, ni, pi = k[i], n[i], model.get_p_multi(
            p0, m0, p1, m1, neg_risk_aversion, pos_risk_aversion,
            neg_distortion, pos_distortion,
            neg_precision, pos_precision)

        log_likelihood = scipy.stats.binom.logpmf(k=ki, n=ni, p=pi)

        if log_likelihood == -np.inf:
            lls = - np.inf
            break

        else:
            lls += log_likelihood

    return lls * -1


def _get_cross_validation(d, monkey, randomize, n_chunk,
                          bounds=((-0.99, 0.99), (-0.99, 0.99), (0.01, 1),
                                  (0.01, 1), (0, 5), (0, 5)),
                          init_guess=None,
                          method='evolutionary'):
    print()
    log(f'Getting fit for {monkey}...', NAME)
    fit = {}

    alternatives, choose_risky = experimental_data.filter.risk.get_choose_risky(d)

    n_trials = len(alternatives)
    reminder = n_trials % n_chunk

    idx = np.arange(n_trials)
    if randomize:
        np.random.shuffle(idx)

    if reminder > 0:
        idx = idx[:-reminder]

    parts = np.split(idx, n_chunk)

    log(f'Chunk using '
        f'{"chronological" if not randomize else "randomized"} '
        f'order', NAME)
    log(f'N trials = {n_trials}', NAME)
    log(f'N parts = {len(parts)} '
        f'(n trials per part = {int(n_trials / n_chunk)}, '
        f'reminder = {reminder})', NAME)

    for label in [
            'pos_risk_aversion', 'neg_risk_aversion', 'pos_distortion',
            'neg_distortion',
            'pos_precision', 'neg_precision', 'log_likelihood_sum']:
        fit[label] = []

    for p in parts:

        alt, n, k = experimental_data.filter.risk.cluster_risky_choice_by_alternative(
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
                raise AttributeError(
                    "Method '{}' can not handle an initial guess")
            res = scipy.optimize.differential_evolution(
                func=_objective, args=args, bounds=bounds)

        else:
            raise NotImplementedError(
                f"Method '{method}' is not implemented")

        nra, pra, ndi, pdi, npr, ppr = res.x
        lls = res.fun * -1

        fit['neg_risk_aversion'].append(nra)
        fit['pos_risk_aversion'].append(pra)
        fit['neg_distortion'].append(ndi)
        fit['pos_distortion'].append(pdi)
        fit['neg_precision'].append(npr)
        fit['pos_precision'].append(ppr)
        fit['log_likelihood_sum'].append(lls)

    return fit


def _pickle_load(d, monkey, force, randomize, n_chunk, method):

    randomize_str = "random_order" if randomize else "chronological_order"
    fit_path = os.path.join(BACKUP_FOLDER,
                            f'fit_{monkey}_{randomize_str}_'
                            f'{n_chunk}chunk_{method}.p')

    if not os.path.exists(fit_path) or force:

        fit = _get_cross_validation(d, monkey=monkey,
                                    randomize=randomize, n_chunk=n_chunk,
                                    method=method)

        os.makedirs(os.path.dirname(fit_path), exist_ok=True)
        with open(fit_path, 'wb') as f:
            pickle.dump(fit, f)

    else:
        with open(fit_path, 'rb') as f:
            fit = pickle.load(f)

    return fit


def run(d, monkey, n_chunk, force, randomize,
        method='SLSQP'):

    fit = _pickle_load(d=d, monkey=monkey,
                       force=force, randomize=randomize, n_chunk=n_chunk,
                       method=method)

    log(f'Results fit: {monkey}', NAME)
    for label in MODEL_PARAMETERS + ['log_likelihood_sum', ]:
        log(f'{label} = {np.mean(fit[label]):.2f} '
            f'(+/-{np.std(fit[label]):.2f} SD)', NAME)
    print()

    return fit
