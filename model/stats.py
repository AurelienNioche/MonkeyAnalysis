import numpy as np
import scipy.stats
import statsmodels.stats
import statsmodels.stats.multitest
from sklearn.linear_model import LinearRegression
from statsmodels import api as sm

from parameters.parameters import PARAMETERS
from utils.utils import log


NAME = "model.stats"


def stats_comparison_best_values(fit):

    monkeys = sorted(fit.keys())

    us = []
    ps = []

    for i, monkey in enumerate(monkeys):

        pra = fit[monkey]['pos_risk_aversion']
        nra = fit[monkey]['neg_risk_aversion']
        pdi = fit[monkey]['pos_distortion']
        ndi = fit[monkey]['neg_distortion']
        ppr = fit[monkey]['pos_precision']
        npr = fit[monkey]['neg_precision']

        to_compare = [
            (pra, nra),
            (pdi, ndi),
            (ppr, npr)
        ]

        for x1, x2 in to_compare:
            u, p = scipy.stats.mannwhitneyu(x1, x2)
            ps.append(p)
            us.append(u)

    valid, p_corr, alpha_c_sidak, alpha_c_bonf = \
        statsmodels.stats.multitest.multipletests(pvals=ps, alpha=0.01,
                                                  method="b")

    for param, u, p, p_c in zip(("H: risk aversion",
                                 "H: distortion", "H: precision",
                                 "G: risk aversion",
                                 "G: distortion", "G: precision"),
                                us, ps, p_corr):
        log(f'Comparision for {param} parameter values: '
            f'u = {u}, p = {p:.3f}, p_c = {p_c:.3f}', name=NAME)


def regression(x, y):

    reg = LinearRegression()
    reg.fit(np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1))
    # print("The linear model is: Y = {:.5} + {:.5}X"
    # .format(reg.intercept_[0], reg.coef_[0][0]))
    # predictions = reg.predict(np.array(x).reshape(-1, 1))

    alpha, beta = reg.intercept_[0], reg.coef_[0][0]

    x_2 = sm.add_constant(x)
    est = sm.OLS(y, x_2).fit()   # print(est.summary())
    f, p = est.fvalue, est.f_pvalue   # print(f"F={est.fvalue:.3f},
    # p={est.f_pvalue:.3f}, n={len(y)}")
    n = len(y)
    return f, p, n, alpha, beta


def stats_regression_best_values(fit):

    monkeys = sorted(fit.keys())

    fs, ps, ns, alphas, betas = [], [], [], [], []

    for i, monkey in enumerate(monkeys):

        for param in PARAMETERS:

            y = fit[monkey][param]

            # print(monkey, param)
            f, p, n, alpha, beta = regression(np.arange(len(y)), y)
            fs.append(f)
            ps.append(p)
            ns.append(n)
            alphas.append(alpha)
            betas.append(beta)

    valid, p_corr, alpha_c_sidak, alpha_c_bonf = \
        statsmodels.stats.multitest.multipletests(pvals=ps, alpha=0.01,
                                                  method="b")

    rgr_line_param = {m: {} for m in monkeys}
    i = 0
    for monkey in monkeys:
        for param in PARAMETERS:
            rgr_line_param[monkey][param] = \
                alphas[i], betas[i], p_corr[i] < 0.01
            i += 1

    for param, f, p, p_c, n, alpha, beta in zip((
            "H: risk aversion + ",
            "H: risk aversion - ",
            "H: distortion +",
            "H: distortion -",
            "H: precision +",
            "H: precision -",
            "G: risk aversion + ",
            "G: risk aversion - ",
            "G: distortion +",
            "G: distortion -",
            "G: precision +",
            "G: precision -",), fs, ps, p_corr, ns, alphas, betas):
        log(f'Linear regression stats for {param} parameter values: '
            f'F = {f:.3f}, p = {p:.3f}, p_c = {p_c:.3f}, n={n}'
            f', alpha = {alpha:.2f}, beta = {beta:.2f}',
            name=NAME)

    print("[LATEX TABLE CONTENT]")
    for monkey, param, fstat, p, p_c, n, alpha, beta in zip(
            ["Monkey H", ] * 6 + ["Monkey G", ] * 6,
            [i for i in [
            r"\omega_G",
            r"\omega_L",
            r"\alpha_G",
            r"\alpha_L",
            r"\lambda_G",
            r"\lambda_L"]]*2, fs, ps, p_corr, ns, alphas, betas):

        p_str = "p<0.001" if p == 0 else f"p={p:.3f}"
        p_c_str = "p<0.001" if p_c == 0 else f"p={p_c:.3f}"

        if p_c < 0.01:
            p_c_str += '^*'
        print(f"{monkey} & ${param}$ &" + r'$2\times'
              + f"{n}$ & ${alpha:.2f}$ & ${beta:.2f}$ & "
              + f"{fstat:.2f} & ${p_str}$ & ${p_c_str}$" + r"\\")
    print("[LATEX TABLE CONTENT]")

    return rgr_line_param


def display_table_content(fit):

    print("[LATEX TABLE CONTENT]")
    monkeys = sorted(fit.keys())
    for monkey in monkeys:

        # To display
        dsp = ""

        for param_pos, param_neg in (
            ('pos_risk_aversion', 'neg_risk_aversion'),
            ('pos_distortion', 'neg_distortion'),
            ('pos_precision', 'neg_precision')

        ):
            mean_pos = np.mean(fit[monkey][param_pos])
            std_pos = np.std(fit[monkey][param_pos])

            mean_neg = np.mean(fit[monkey][param_neg])
            std_neg = np.std(fit[monkey][param_neg])

            dsp += f"${mean_pos:.2f}$ " + r"($\pm " + f"{std_pos:.2f}$); " \
                f"${mean_neg:.2f}$ " + r"($\pm " + f"{std_neg:.2f}$) &"

        dsp = dsp[:-1] + "\\"
        log(f"Line for {monkey} for table displaying best parameter values",
            name=NAME)
        print(dsp)
    print("[LATEX TABLE CONTENT]")
