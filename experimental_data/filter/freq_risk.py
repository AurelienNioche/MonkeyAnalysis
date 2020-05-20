from experimental_data.filter.risk import get_choose_risky_loss_or_gain_only
from sigmoid_fit.sigmoid_fit import sigmoid_fit

from utils.log import log

from parameters.parameters import GAIN, LOSS

NAME = "experimental_data.filter.freq_risk_against_exp_value"


def get(d, verbose=True):
    conditions = GAIN, LOSS

    data = {}

    for i, cd in enumerate(conditions):

        x, y = get_choose_risky_loss_or_gain_only(d, gain_only=cd == GAIN,
                                                  verbose=verbose)

        try:
            fit = sigmoid_fit(x=x, y=y)

        except RuntimeError as e:
            log(e, NAME)
            fit = None

        data[cd] = {'x': x, 'y': y, 'fit': fit}

    return data
