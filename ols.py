import numpy as np
import statsmodels.api as sm
import statsmodels.stats.api as sms
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import statsmodels.formula.api as smf
from scipy import stats
from matplotlib import pyplot as plt

import seaborn as sns

import pandas as pd
from sklearn import preprocessing


def main():

    df = pd.read_excel(
        'data/summary_good.xlsx',
        usecols=("idname", "MDS", "weight", "neg_risk_aversion", "neg_distortion", "neg_precision",),
        index_col=0,
        sheet_name='data')

    print(df)

    # n_rows, n_cols = 2, 1
    # fig, axes = plt.subplots(figsize=(n_cols*6, n_rows*6), nrows=n_rows,
    #                          ncols=n_cols)
    #
    # ax = axes[0]

    # ax.scatter(df["MDS"], df["weight"])

    # df = (df - df.min()) / (df.max() - df.min())
    min_max_scaler = preprocessing.MinMaxScaler()
    df = pd.DataFrame(min_max_scaler.fit_transform(df), columns=df.columns,
                 index=df.index)

    print(df)

    # # Compute both correlation matrices
    # corr = np.corrcoef(df, rowvar=0)
    # print(np.linalg.det(corr))  # 0.988532159861
    # # x = df.values  # returns a numpy array
    # #

    # x_scaled = min_max_scaler.fit_transform(x)
    # df = pd.DataFrame(x_scaled)

    # df = sm.add_constant(df)
    #print(df)

    formula = "MDS ~ weight " \
              "+ neg_risk_aversion + neg_distortion + neg_precision"
    # nobs2 = 100
    # x = np.arange(nobs2)
    # np.random.seed(54321)
    # X = np.column_stack((x, x ** 2))
    # X = sm.add_constant(X, prepend=False)
    # lny = np.exp(-(.03 * x + .0001 * x ** 2 - 1.0)) + .001 * np.random.rand(
    #     nobs2)
    #
    # gauss_log = sm.GLM(lny, X,
    #                    family=sm.families.Gaussian(sm.families.links.log()))
    # gauss_log_results = gauss_log.fit()
    # print(gauss_log_results.summary())

    # family = sm.families.Gaussian()
    #
    # mod = smf.glm(formula=formula, data=df, family=family)
    # r = mod.fit()
    #
    # r_squared = 1-(r.deviance/r.null_deviance)
    # print(r.summary())
    # print(f"R2={r_squared}")

    mod = smf.ols(formula=formula, data=df)

    res = mod.fit()

    print(res.summary())

    print('Parameters: ', res.params)
    print('R2: ', res.rsquared)

    # normality
    name = ['Jarque-Bera', 'Chi^2 two-tail prob.', 'Skew', 'Kurtosis']
    test = sms.jarque_bera(res.resid)
    for n, m in zip(name, test):
        print(n, m)

    # Mutlicollinearity
    print("multicollinearity", np.linalg.cond(res.model.exog))

    # Heteroskedasticity
    print("heteroskedasticity")
    name = ['Lagrange multiplier statistic', 'p-value',
            'f-value', 'f p-value']
    test = sms.het_breuschpagan(res.resid, res.model.exog)
    for n, m in zip(name, test):
        print(n, m)

    # Linearity
    print("linearity")
    name = ['t value', 'p value']
    test = sms.linear_harvey_collier(res)
    for n, m in zip(name, test):
        print(n, m)

    fig = plt.figure(figsize=(12, 20))
    fig = sm.graphics.plot_partregress_grid(res, fig=fig)
    plt.tight_layout()
    plt.show()

    fig = plt.figure(figsize=(12, 8))
    fig = sm.graphics.plot_ccpr_grid(res, fig=fig)

    plt.show()

    fig, ax = plt.subplots(figsize=(12, 8))
    fig = sm.graphics.influence_plot(res, ax=ax, criterion="cooks")

    plt.show()

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(res.predict(), res.resid_pearson)
    ax.set_xlabel("Fitted")
    ax.set_ylabel("Residuals (normalized)")
    plt.show()

    sns.distplot(res.resid, hist=False, kde=True,
                 color='darkblue',
                 hist_kws={'edgecolor': 'black'},
                 kde_kws={'linewidth': 4})
    plt.show()

    # Normal probability plot
    fig, ax = plt.subplots(figsize=(6, 2.5))
    stats.probplot(res.resid, plot=ax, fit=True)
    plt.show()

    # fig = plt.figure(figsize=(12, 8))
    # fig = sm.graphics.plot_regress_exog(prestige_model, "education", fig=fig)


    # itc = res.params["Intercept"]
    # slp = res.params["weight"]
    #
    # x = df["weight"]
    # y = df["MDS"]
    # x_fit = np.linspace(np.min(x), np.max(x), 10)
    # y_fit = itc + slp*x_fit

    # ax.scatter(x, y)
    # ax.plot(x_fit, y_fit)

    # prstd, iv_l, iv_u = wls_prediction_std(res)
    #
    # print(prstd)
    # print()
    # print(iv_l)
    # print()
    # print(iv_u)
    #print(res.normalized_cov_params)

    # inf = results.get_influence()
    # print(inf.summary_frame())

    # param_without_itc = res.params.copy()
    # param_without_itc.pop('Intercept')
    #
    # ordered = [k for k, v in sorted(param_without_itc.items(),
    #                                    key=lambda item: item[1],
    #                                    reverse=True)]
    #
    # formula = "MDS ~ "
    # for i in range(len(ordered)):
    #
    #     formula += f'+ {ordered[i]}'
    #
    #     print()
    #     print(f"Formula: {formula}")
    #     mod = smf.ols(formula=formula, data=df)
    #
    #     res = mod.fit()
    #
    #     print(res.summary())
    #
    #     print('Parameters: ', res.params)
    #     print('R2: ', res.rsquared)
    #
    # print(ordered)

    # plt.show()


if __name__ == "__main__":
    main()
