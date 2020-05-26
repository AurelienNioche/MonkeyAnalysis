import numpy as np
import pickle
import os
import scipy.stats
import scipy.optimize

from analysis.parameters.parameters import BACKUP_FOLDER
from data_interface.models import Data


def _get_chunk(monkey, randomize=False, n_chunk=None, n_trials_per_chunk=None):

    entries = Data.objects.filter(monkey=monkey, is_risky=True)

    data = np.array(entries.values('p0', 'x0', 'p1', 'x1', 'c').order_by("id"))
    n = len(data)

    # Normalize amounts
    max_x = max(max(entries.values_list('x0', flat=True)),
                max(entries.values_list('x1', flat=True)))
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

    print(f'Chunk using '
          f'{"chronological" if not randomize else "randomized"} '
          f'order')
    print(f'N trials = {n-remainder}')
    print(f'N parts = {len(parts)} '
          f'(n trials per part = {int((n-remainder) / n_chunk)}, '
          f'remainder = {remainder})')

    return data, parts, n-remainder


def _get_cross_validation(monkey, randomize, n_chunk, class_model,
                          n_trials_per_chunk, method):

    print(f'Getting the fit for {monkey}...')
    fit = {
        k: [] for k in class_model.param_labels
    }

    fit['LLS'] = []

    data, parts, n_trial = _get_chunk(
        monkey=monkey,
        n_chunk=n_chunk,
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


def _pickle_load(monkey, force, randomize, n_chunk, n_trials_per_chunk,
                 class_model, method):

    randomize_str = "random_order" if randomize else "chronological_order"
    fit_path = os.path.join(BACKUP_FOLDER,
                            f'fit_{monkey}_{randomize_str}_method_{method}_'
                            f'n_trials_per_chunk_{n_trials_per_chunk}_'
                            f'{n_chunk}chunk_{class_model.__name__}.p')

    if not os.path.exists(fit_path) or force:

        fit = _get_cross_validation(monkey=monkey,
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


def get_parameter_estimate(
        monkey, randomize, class_model, method, force=False,
        n_chunk=None, n_trials_per_chunk=None):

    fit = _pickle_load(monkey=monkey,
                       randomize=randomize,
                       n_chunk=n_chunk,
                       n_trials_per_chunk=n_trials_per_chunk,
                       class_model=class_model,
                       method=method,
                       force=force)

    print(f'Results fit: {monkey}')
    for label in class_model.param_labels + ['LLS', ]:
        print(f'{label} = {np.mean(fit[label]):.2f} '
            f'(+/-{np.std(fit[label]):.2f} SD)')
    print()

    return fit