import numpy as np
import statsmodels.api as sm
import statsmodels.stats.api as sms
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import statsmodels.formula.api as smf
from scipy import stats
from matplotlib import pyplot as plt

import pandas as pd
from sklearn import preprocessing


def main():
    prestige = sm.datasets.get_rdataset("Duncan", "carData", cache=True).data
    print(prestige)
    prestige_model = smf.ols("prestige ~ income + education",
                             data=prestige).fit()

    fig, ax = plt.subplots(figsize=(12, 8))
    fig = sm.graphics.influence_plot(prestige_model, ax=ax, criterion="cooks")
    plt.show()

    fig, ax = plt.subplots(figsize=(12, 8))
    fig = sm.graphics.plot_partregress("prestige", "income",
                                       ["income", "education"], data=prestige,
                                       ax=ax)
    plt.show()

    fix, ax = plt.subplots(figsize=(12, 14))
    fig = sm.graphics.plot_partregress("prestige", "income", ["education"],
                                       data=prestige, ax=ax)
    plt.show()

    fig = plt.figure(figsize=(12, 8))
    fig = sm.graphics.plot_regress_exog(prestige_model, "education", fig=fig)
    plt.show()



if __name__ == "__main__":
    main()
