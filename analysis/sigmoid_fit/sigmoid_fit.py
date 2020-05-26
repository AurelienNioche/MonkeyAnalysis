import numpy as np
from scipy.optimize import curve_fit
# from scipy.stats.distributions import t

from analysis.parameters.parameters import SIG_MID, SIG_STEEP

NAME = "sigmoid_fit.sigmoid_fit"


def sigmoid(x, x0, k):
    y = 1 / (1 + np.exp(-k * (x - x0)))
    return y


def sigmoid_fit(x, y, n_points=100, max_eval=10000):

    p_opt, p_cov = curve_fit(f=sigmoid, xdata=x, ydata=y,
                             maxfev=max_eval)

    x_fit = np.linspace(min(x), max(x), n_points)
    y_fit = sigmoid(x_fit, *p_opt)

    return {
        'x': x_fit,
        'y': y_fit,
        SIG_MID: p_opt[0],
        SIG_STEEP: p_opt[1]
    }

    # if return_p_opt:
    #     to_return += (
    #         {SIG_MID: p_opt[0], SIG_STEEP: p_opt[1]}, )

    # if make_stats:
    #     # Do stats about fit
    #     stats_r = stats(y=y_data, p_cov=p_cov, p_opt=p_opt)
    #
    #     to_return += (stats_r,)

    # return to_return


# def sigmoid_one_param(x, theta):
#     # Activation function used to map any real value between 0 and 1
#     return 1 / (1 + np.exp(-theta * x))

# def stats(y, p_opt, p_cov, alpha=0.01):
#     # 95% confidence interval = 100*(1-alpha)
#
#     n = len(y)  # number of data points
#     p = len(p_opt)  # number of parameters
#
#     # print(n, p)
#
#     dof = max(0, n - p)  # number of degrees of freedom
#
#     # student-t value for the dof and confidence level
#     tval = t.ppf(1.0 - alpha / 2., dof)
#
#     log(f"Stats for the sigmoid fit:",
#         name=NAME)
#     # log(f"student-t value: {tval:.2f}", name=NAME)
#
#     try:
#         p_err = np.sqrt(np.diag(p_cov))
#     except FloatingPointError:
#         print(np.diag(p_cov))
#         d = np.diag(p_cov)
#         d.setflags(write=True)
#         d[d < 0] = 0
#         p_err = np.sqrt(d)
#
#     r = []
#
#     for i, p, std in zip(range(n), p_opt, p_err):
#
#         me = std * tval
#         log(f'p{i}: {p:.2f} [{p - me:.2f}  {p + me:.2f}]', name=NAME)
#         r.append(
#             {"val": p, "ic-": p - me, "ic+": p + me}
#         )
#     print()
#
#     return r