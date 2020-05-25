import numpy as np
import pickle
import os
import scipy.stats
import scipy.optimize

import experimental_data.filter
from experimental_data.filter.risk import _gains_only, _riskiest_option_on_left, _riskiest_option_on_right
import experimental_data.filter.risk
from parameters.parameters import BACKUP_FOLDER
from utils.log import log


NAME = 'model.parameter_estimate'


def _get_chunk(d, randomize=False, n_chunk=None, n_trials_per_chunk=None):

    data = []

    total_n = len(d.p.left)

    for t in range(total_n):

        if _gains_only(d=d, t=t) \
            and (_riskiest_option_on_left(d, t)
                 or _riskiest_option_on_right(d, t)):

            data.append({
                'p0': d.p.left[t],
                'p1': d.p.right[t],
                'x0': d.x.left[t],
                'x1': d.x.right[t],
                'c': d.choice[t]
            })

    data = np.array(data)
    n = len(data)

    # Normalize amounts
    max_x = max(max(d.x.left), max(d.x.right))
    assert max_x == 3

    for i in range(n):
        for k in 'x0', 'x1':
            data[i][k] = data[i][k] / max_x

    if n_chunk is None:
        assert n_trials_per_chunk is not None
        n_chunk = n // n_trials_per_chunk
        remainder = n % n_trials_per_chunk
    else:
        remainder = n % n_chunk

    # Drop the remainder
    idx = np.arange(n)
    if remainder > 0:
        idx = idx[remainder:]

    if randomize:
        np.random.shuffle(idx)

    parts = np.split(idx, n_chunk)

    log(f'Chunk using '
        f'{"chronological" if not randomize else "randomized"} '
        f'order', NAME)
    log(f'N trials = {n-remainder}', NAME)
    log(f'N parts = {len(parts)} '
        f'(n trials per part = {int((n-remainder) / n_chunk)}, '
        f'remainder = {remainder})', NAME)

    return data, parts, n-remainder


def _get_cross_validation(d, monkey, randomize, n_chunk, class_model,
                          n_trials_per_chunk, method):

    log(f'Getting the fit for {monkey}...', NAME)
    fit = {
        k: [] for k in class_model.param_labels
    }

    fit['LLS'] = []

    data, parts, n_trial = _get_chunk(
            d=d, n_chunk=n_chunk,
            n_trials_per_chunk=n_trials_per_chunk,
            randomize=randomize)

    for p in parts:
        args = (data[p], )

        if method == "SLSQP":
            res = scipy.optimize.minimize(
                class_model.objective, x0=class_model.init_guess, args=args,
                bounds=class_model.bounds, method='SLSQP')
        elif method == "evolution":
            res = scipy.optimize.differential_evolution(
                func=class_model.objective, args=args,
                bounds=class_model.bounds)
        else:
            raise ValueError(f"Optimization method not recognized: '{method}'")

        lls = - res.fun

        for k, v in zip(class_model.param_labels, res.x):
            fit[k].append(v)

        fit['LLS'].append(lls)

    fit['n_trial'] = n_trial
    fit['class_model'] = class_model
    return fit


def _pickle_load(d, monkey, force, randomize, n_chunk, n_trials_per_chunk,
                 class_model, method):

    randomize_str = "random_order" if randomize else "chronological_order"
    fit_path = os.path.join(BACKUP_FOLDER,
                            f'fit_{monkey}_{randomize_str}_method_{method}_'
                            f'n_trials_per_chunk_{n_trials_per_chunk}_'
                            f'{n_chunk}chunk_{class_model.__name__}.p')

    if not os.path.exists(fit_path) or force:

        fit = _get_cross_validation(d, monkey=monkey,
                                    n_trials_per_chunk=n_trials_per_chunk,
                                    randomize=randomize, n_chunk=n_chunk,
                                    class_model=class_model,
                                    method=method)

        os.makedirs(os.path.dirname(fit_path), exist_ok=True)
        with open(fit_path, 'wb') as f:
            pickle.dump(fit, f)

    else:
        with open(fit_path, 'rb') as f:
            fit = pickle.load(f)

    return fit


def run(d, monkey, randomize, class_model, method, force=False,
        n_chunk=None, n_trials_per_chunk=None):

    fit = _pickle_load(d=d, monkey=monkey,
                       randomize=randomize,
                       n_chunk=n_chunk,
                       n_trials_per_chunk=n_trials_per_chunk,
                       class_model=class_model,
                       method=method,
                       force=force)

    log(f'Results fit: {monkey}', NAME)
    for label in class_model.param_labels + ['LLS', ]:
        log(f'{label} = {np.mean(fit[label]):.2f} '
            f'(+/-{np.std(fit[label]):.2f} SD)', NAME)
    print()

    return fit
