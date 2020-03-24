import numpy as np
from scipy.optimize import curve_fit
from scipy.stats.distributions import t

from utils.log import log

NAME = "sigmoid_fit.sigmoid_fit"


def sigmoid(x, x0, k):
    y = 1 / (1 + np.exp(-k * (x - x0)))
    return y


def sigmoid_one_param(x, theta):
    # Activation function used to map any real value between 0 and 1
    return 1 / (1 + np.exp(-theta * x))


def sigmoid_fit(x_data, y_data, f=sigmoid, n_points=50, make_stats=True):
    # Fit sigmoid
    p_opt, p_cov = curve_fit(f, x_data, y_data,
                             maxfev=10000)

    # Plot
    x = np.linspace(min(x_data), max(x_data), n_points)
    y = f(x, *p_opt)

    if make_stats:
        # Do stats about fit
        stats_r = stats(y=y_data, p_cov=p_cov, p_opt=p_opt)

        return x, y, stats_r
    else:
        return x, y


def stats(y, p_opt, p_cov, alpha=0.01):
    # 95% confidence interval = 100*(1-alpha)

    n = len(y)  # number of data points
    p = len(p_opt)  # number of parameters

    # print(n, p)

    dof = max(0, n - p)  # number of degrees of freedom

    # student-t value for the dof and confidence level
    tval = t.ppf(1.0 - alpha / 2., dof)

    log(f"Stats for the sigmoid fit:",
        name=NAME)
    # log(f"student-t value: {tval:.2f}", name=NAME)

    try:
        p_err = np.sqrt(np.diag(p_cov))
    except FloatingPointError:
        print(np.diag(p_cov))
        d = np.diag(p_cov)
        d.setflags(write=True)
        d[d < 0] = 0
        p_err = np.sqrt(d)

    r = []

    for i, p, std in zip(range(n), p_opt, p_err):

        me = std * tval
        log(f'p{i}: {p:.2f} [{p - me:.2f}  {p + me:.2f}]', name=NAME)
        r.append(
            {"val": p, "ic-": p - me, "ic+": p + me}
        )
    print()

    return r