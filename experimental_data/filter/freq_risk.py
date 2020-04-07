import matplotlib.pyplot as plt

from experimental_data.filter.risk import get_choose_risky_loss_or_gain_only
from sigmoid_fit.sigmoid_fit import sigmoid_fit

from utils.log import log
# from plot.utils import save_fig

from parameters.parameters import \
    GAIN, LOSS, \
    SIG_MID, SIG_STEEP

NAME = "experimental_data.filter.freq_risk_against_exp_value"


def get(d):
    conditions = GAIN, LOSS

    x_data = {}
    y_data = {}
    x_fit = {}
    y_fit = {}

    fit = {}

    for i, cd in enumerate(conditions):

        log(
            f"Stats for risk against exp value "
            f"- {cd}:", name=NAME)

        x_data_cd, y_data_cd = \
            get_choose_risky_loss_or_gain_only(
                d, gain_only=cd == GAIN)

        try:
            x_fit_cd, y_fit_cd, p_opt, stats_cond = \
                sigmoid_fit(x_data=x_data_cd, y_data=y_data_cd,
                            return_p_opt=True)

        except RuntimeError as e:
            log(e, NAME)
            x_fit_cd, y_fit_cd = None, None
            p_opt = None, None

        x_data[cd] = x_data_cd
        y_data[cd] = y_data_cd
        x_fit[cd] = x_fit_cd
        y_fit[cd] = y_fit_cd

        fit[cd] = {
            SIG_MID: p_opt[SIG_MID],
            SIG_STEEP: p_opt[SIG_STEEP]
        }

    print()

    return \
        {
            "x": x_data,
            "y": y_data,
            "x_fit": x_fit,
            "y_fit": y_fit,
            "fit": fit
        }
