import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats
from matplotlib import pyplot as plt

import pandas as pd
from sklearn import preprocessing


def main():
    df = pd.read_excel(
        'data/summary_good.xlsx',
        usecols=("MDS", "weight", "neg_risk_aversion", "neg_distortion", "neg_precision", ),
        sheet_name='data')

    print(df)

    # df = (df - df.min()) / (df.max() - df.min())
    min_max_scaler = preprocessing.MinMaxScaler()
    df = pd.DataFrame(min_max_scaler.fit_transform(df), columns=df.columns,
                 index=df.index)

    print(df)

    # x = df.values  # returns a numpy array
    #

    # x_scaled = min_max_scaler.fit_transform(x)
    # df = pd.DataFrame(x_scaled)

    formula = "MDS ~ 1 + weight + neg_risk_aversion + neg_distortion + neg_precision"
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

    family = sm.families.Gaussian()

    mod = smf.glm(formula=formula, data=df, family=family)
    r = mod.fit()

    r_squared = 1-(r.deviance/r.null_deviance)
    print(r.summary())
    print(f"R2={r_squared}")

    mod = smf.ols(formula=formula, data=df)

    res = mod.fit()

    print(res.summary())

    print(res.normalized_cov_params)

if __name__ == "__main__":
    main()
