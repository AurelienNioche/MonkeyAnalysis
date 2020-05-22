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


NAME = 'model.parameter_estimate'


def _get_cross_validation(d, monkey, randomize, n_chunk, class_model):

    log(f'Getting the fit for {monkey}...', NAME)
    fit = {
        k: [] for k in class_model.param_labels
    }

    fit['LLS'] = []

    data, parts = \
        experimental_data.filter.risk.get_chunk(
            d=d, n_chunk=n_chunk, randomize=randomize)

    for p in parts:
        args = (data[p], )

        res = scipy.optimize.differential_evolution(
            func=class_model.objective, args=args, bounds=class_model.bounds)
        # res = scipy.optimize.minimize(
        #     class_model.objective, x0=class_model.init_guess, args=args,
        #     bounds=class_model.bounds, method='SLSQP')

        lls = - res.fun

        for k, v in zip(class_model.param_labels, res.x):
            fit[k].append(v)

        fit['LLS'].append(lls)

    return fit


def _pickle_load(d, monkey, force, randomize, n_chunk, class_model):

    randomize_str = "random_order" if randomize else "chronological_order"
    fit_path = os.path.join(BACKUP_FOLDER,
                            f'fit_{monkey}_{randomize_str}_'
                            f'{n_chunk}chunk_{class_model.__name__}.p')

    if not os.path.exists(fit_path) or force:

        fit = _get_cross_validation(d, monkey=monkey,
                                    randomize=randomize, n_chunk=n_chunk,
                                    class_model=class_model)

        os.makedirs(os.path.dirname(fit_path), exist_ok=True)
        with open(fit_path, 'wb') as f:
            pickle.dump(fit, f)

    else:
        with open(fit_path, 'rb') as f:
            fit = pickle.load(f)

    return fit


def run(d, monkey, n_chunk, randomize, class_model, force):

    fit = _pickle_load(d=d, monkey=monkey,
                       randomize=randomize, n_chunk=n_chunk,
                       class_model=class_model,
                       force=force)

    log(f'Results fit: {monkey}', NAME)
    for label in class_model.param_labels + ['LLS', ]:
        log(f'{label} = {np.mean(fit[label]):.2f} '
            f'(+/-{np.std(fit[label]):.2f} SD)', NAME)
    print()

    return fit
