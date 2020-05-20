import numpy as np
import pickle
import os
import scipy.stats
import scipy.optimize

import experimental_data.filter
import experimental_data.filter.risk
import experimental_data.filter.risk
from parameters.parameters import BACKUP_FOLDER
from utils.log import log
from model.model import DecisionMakingModel

NAME = 'model.parameter_estimate'

EPS = np.finfo(float).eps


def _objective(param, *args):

    p0, p1, x0, x1 = args

    model = DecisionMakingModel(param=param)

    ll = np.zeros(len(p0))

    for i, (p0_i, p1_i, x0_i, x1_i) in enumerate(zip(p0, p1, x0, x1)):

        pi = model.p_choice_L0(p0=p0_i, p1=p1_i, x0=x0_i, x1=x1_i)
        ll[i] = np.log(pi+EPS)

    return -ll.sum()


def _get_cross_validation(d, monkey, randomize, n_chunk):

    log(f'Getting the fit for {monkey}...', NAME)
    fit = {
        k: [] for k in DecisionMakingModel.param_labels
    }

    fit['LLS'] = []

    p0, p1, x0, x1, parts = \
        experimental_data.filter.risk.get_chunk(
            d=d, n_chunk=n_chunk, randomize=randomize)

    for p in parts:

        args = (p0[p], p1[p], x0[p], x1[p])

        res = scipy.optimize.differential_evolution(
            func=_objective, args=args, bounds=DecisionMakingModel.bounds)

        lls = - res.fun

        for k, v in zip(DecisionMakingModel.param_labels, res.x):
            fit[k].append(v)

        fit['LLS'].append(lls)

    return fit


def _pickle_load(d, monkey, force, randomize, n_chunk):

    randomize_str = "random_order" if randomize else "chronological_order"
    fit_path = os.path.join(BACKUP_FOLDER,
                            f'fit_{monkey}_{randomize_str}_'
                            f'{n_chunk}chunk.p')

    if not os.path.exists(fit_path) or force:

        fit = _get_cross_validation(d, monkey=monkey,
                                    randomize=randomize, n_chunk=n_chunk)

        os.makedirs(os.path.dirname(fit_path), exist_ok=True)
        with open(fit_path, 'wb') as f:
            pickle.dump(fit, f)

    else:
        with open(fit_path, 'rb') as f:
            fit = pickle.load(f)

    return fit


def run(d, monkey, n_chunk, randomize, force):

    fit = _pickle_load(d=d, monkey=monkey,
                       randomize=randomize, n_chunk=n_chunk,
                       force=force)

    log(f'Results fit: {monkey}', NAME)
    for label in DecisionMakingModel.param_labels + ['LLS', ]:
        log(f'{label} = {np.mean(fit[label]):.2f} '
            f'(+/-{np.std(fit[label]):.2f} SD)', NAME)
    print()

    return fit
