import numpy as np
import scipy.stats
import statsmodels.stats
import statsmodels.stats.multitest
from sklearn.linear_model import LinearRegression
from statsmodels import api as sm

from utils.log import log


NAME = "model.stats"


# def stats_comparison_best_values(fit, monkey):
#
#     us = []
#     ps = []
#
#     pra = fit['pos_risk_aversion']
#     nra = fit['neg_risk_aversion']
#     pdi = fit['pos_distortion']
#     ndi = fit['neg_distortion']
#     ppr = fit['pos_precision']
#     npr = fit['neg_precision']
#
#     to_compare = [
#         (pra, nra),
#         (pdi, ndi),
#         (ppr, npr)
#     ]
#
#     for x1, x2 in to_compare:
#         try:
#             u, p = scipy.stats.mannwhitneyu(x1, x2)
#         except ValueError:
#             u, p = None, np.inf
#         ps.append(p)
#         us.append(u)
#
#     valid, p_corr, alpha_c_sidak, alpha_c_bonf = \
#         statsmodels.stats.multitest.multipletests(pvals=ps, alpha=0.01,
#                                                   method="b")
#
#     labels = [f"{monkey} - {param}"
#               for param in ("risk aversion", "distortion", "precision")]
#
#     log("Comparison parameter values (Mann–Whitney U test)", name=NAME)
#     for label, u, p, p_c in zip(labels, us, ps, p_corr):
#         log(f'{label}: '
#             f'u = {u}, p = {p:.3f}, p_c = {p_c:.3f}', name=NAME)
#     print()


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


def stats_regression_best_values(fit, class_model):

    fs, ps, ns, alphas, betas = [], [], [], [], []

    for param in class_model.param_labels:

        y = fit[param]

        f, p, n, alpha, beta = regression(np.arange(len(y)), y)
        fs.append(f)
        ps.append(p)
        ns.append(n)
        alphas.append(alpha)
        betas.append(beta)

    valid, p_corr, alpha_c_sidak, alpha_c_bonf = \
        statsmodels.stats.multitest.multipletests(pvals=ps, alpha=0.01,
                                                  method="b")

    rgr_line_param = {}

    for i, param in enumerate(class_model.param_labels):
        rgr_line_param[param] = \
            alphas[i], betas[i], p_corr[i] < 0.01

    log(f'Linear regression for parameter values over time: ', NAME)

    labels = [f"{param}"
              for param in class_model.param_labels]

    for label, f, p, p_c, n, alpha, beta \
            in zip(labels, fs, ps, p_corr, ns, alphas, betas):
        log(f'{label}: '
            f'F = {f:.3f}, p = {p:.3f}, p_c = {p_c:.3f}, n={n}'
            f', alpha = {alpha:.2f}, beta = {beta:.2f}',
            name=NAME)
    print()
    return rgr_line_param

    # if print_latex:
    #     print("[LATEX TABLE CONTENT]")
    #     for monkey, param, fstat, p, p_c, n, alpha, beta in zip(
    #             ["Monkey H", ] * 6 + ["Monkey G", ] * 6,
    #             [i for i in [
    #             r"\omega_G",
    #             r"\omega_L",
    #             r"\alpha_G",
    #             r"\alpha_L",
    #             r"\lambda_G",
    #             r"\lambda_L"]]*2, fs, ps, p_corr, ns, alphas, betas):
    #
    #         p_str = "p<0.001" if p == 0 else f"p={p:.3f}"
    #         p_c_str = "p<0.001" if p_c == 0 else f"p={p_c:.3f}"
    #
    #         if p_c < 0.01:
    #             p_c_str += '^*'
    #         print(f"{monkey} & ${param}$ &" + r'$2\times'
    #               + f"{n}$ & ${alpha:.2f}$ & ${beta:.2f}$ & "
    #               + f"{fstat:.2f} & ${p_str}$ & ${p_c_str}$" + r"\\")
    #     print("[LATEX TABLE CONTENT]\n")


# def display_table_content(fit):
#
#     print("[LATEX TABLE CONTENT]")
#     monkeys = sorted(fit.keys())
#     for monkey in monkeys:
#
#         # To display
#         dsp = ""
#
#         for param_pos, param_neg in (
#             ('pos_risk_aversion', 'neg_risk_aversion'),
#             ('pos_distortion', 'neg_distortion'),
#             ('pos_precision', 'neg_precision')
#
#         ):
#             mean_pos = np.mean(fit[monkey][param_pos])
#             std_pos = np.std(fit[monkey][param_pos])
#
#             mean_neg = np.mean(fit[monkey][param_neg])
#             std_neg = np.std(fit[monkey][param_neg])
#
#             dsp += f"${mean_pos:.2f}$ " + r"($\pm " + f"{std_pos:.2f}$); " \
#                 f"${mean_neg:.2f}$ " + r"($\pm " + f"{std_neg:.2f}$) &"
#
#         dsp = dsp[:-1] + "\\"
#         log(f"Line for {monkey} for table displaying best parameter values",
#             name=NAME)
#         print(dsp)
#     print("[LATEX TABLE CONTENT]\n")