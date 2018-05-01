import numpy as np
import pickle
import os
import scipy.stats
import scipy.optimize

import data.filter

from utils.utils import log
from model import model

name = 'ParameterEstimate'


def _objective_multi(parameters, alternatives, n, k):

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


def _get_cross_validation(d, n_chunk=10):

    monkeys = d.keys()

    fit = {i: {} for i in monkeys}

    for monkey in monkeys:

        log(f'Getting fit for {monkey}...', name)

        alternatives, choose_risky = data.filter.get_choose_risky(d[monkey])

        n_trials = len(alternatives)

        reminder = n_trials % n_chunk

        idx = np.random.permutation(np.arange(n_trials))
        if reminder > 0:
            idx = idx[:-reminder]

        parts = np.split(idx, n_chunk)

        log(f'N trials = {n_trials}', name)
        log(f'N parts = {len(parts)} (n trials per part = {int(n_trials / n_chunk)}, '
            f'reminder = {reminder})', name)

        for label in [
                'pos_risk_aversion', 'neg_risk_aversion', 'pos_distortion', 'neg_distortion',
                'pos_precision', 'neg_precision', 'log_likelihood_sum']:
            fit[monkey][label] = []

        for p in parts:

            alt, n, k = data.filter.cluster_risky_choice_by_alternative(
                alternatives[p], choose_risky[p])

            res = scipy.optimize.minimize(
                _objective_multi, np.array([0, 0, 0.5, 0.5, 1, 1]), args=(alt, n, k,),
                bounds=((-0.99, 0.99), (-0.99, 0.99), (0.01, 1), (0.01, 1), (0, 5), (0, 5)))  # method=SLSQP

            nra, pra, ndi, pdi, npr, ppr = res.x

            fit[monkey]['neg_risk_aversion'].append(nra)
            fit[monkey]['pos_risk_aversion'].append(pra)
            fit[monkey]['neg_distortion'].append(ndi)
            fit[monkey]['pos_distortion'].append(pdi)
            fit[monkey]['neg_precision'].append(npr)
            fit[monkey]['pos_precision'].append(ppr)
            fit[monkey]['log_likelihood_sum'].append(res.fun)

        for label in [
                'pos_risk_aversion', 'neg_risk_aversion', 'pos_distortion', 'neg_distortion',
                'pos_precision', 'neg_precision', 'log_likelihood_sum']:
            log(f'{label} = {np.mean(fit[monkey][label]):.2f} '
                f'(+/-{np.std(fit[monkey][label]):.2f} SD)', name)

    return fit


def _pickle_load(d, func, fit_path, force, *args):

    if not os.path.exists(fit_path) or force:

        fit = func(d, *args)
        os.makedirs(os.path.dirname(fit_path), exist_ok=True)
        with open(fit_path, 'wb') as f:
            pickle.dump(fit, f)

    else:
        with open(fit_path, 'rb') as f:
            fit = pickle.load(f)

    return fit


def run_cross_validation(d, force=False):

    fit = _pickle_load(d=d, force=force, func=_get_cross_validation,
                       fit_path='model/pickle/fit_cross_validation.p')

    for monkey in d.keys():
        log(f'{monkey}', name)
        for label in [
            'pos_risk_aversion', 'neg_risk_aversion', 'pos_distortion', 'neg_distortion',
            'pos_precision', 'neg_precision', 'log_likelihood_sum']:
            log(f'{label} = {np.mean(fit[monkey][label]):.2f} '
                f'(+/-{np.std(fit[monkey][label]):.2f} SD)', name)

    return fit
