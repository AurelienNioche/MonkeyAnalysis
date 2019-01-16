import os
import matplotlib.gridspec
import matplotlib.pyplot as plt
import numpy as np

import model.parameter_estimate

import plot.utility
import plot.precision
import plot.probability_distortion
import plot.control
import plot.exemplary_case
import plot.freq_risk_against_exp_value

import data.get
import data.filter

import statsmodels.stats.multitest
import scipy.stats

from utils.utils import today, log

import main

name = "Supp"

monkeys = 'Havane', 'Gladys'
color_loss, color_gain = 'C1', 'C0'
fig_folder = 'fig'


def plot_history(
        pos_param, neg_param, ax, y_lim, param_name, show_mid_line=False,
        axis_label_font_size=20,
        ticks_label_font_size=14,
        point_size=100):

    x_data = np.arange(len(pos_param)) + 1
    y_data_gain = pos_param
    y_data_loss = neg_param

    ax.scatter(x_data, y_data_gain, color=color_gain, alpha=0.5, s=point_size)
    ax.scatter(x_data, y_data_loss, color=color_loss, alpha=0.5, s=point_size)

    if show_mid_line:
        ax.axhline(0, alpha=0.5, linewidth=1, color='black', linestyle='--', zorder=-10)
    # ax.axvline(0, alpha=0.5, linewidth=1, color='black', linestyle='--', zorder=-10)

    ax.set_xlim((0.5, 10.5))
    ax.set_ylim(y_lim)
    ax.set_xticks((1, 5, 10))

    # Axis labels
    ax.set_xlabel(
        "time",
        fontsize=axis_label_font_size)
    ax.set_ylabel(
        param_name,
        fontsize=axis_label_font_size)

    # Remove top and right borders
    # ax.spines['right'].set_color('none')
    # ax.xaxis.set_ticks_position('bottom')
    # ax.yaxis.set_ticks_position('left')
    # ax.spines['bottom'].set_position(('data', 0))
    # ax.spines['top'].set_color('none')

    ax.tick_params(axis='both', which='major', labelsize=ticks_label_font_size)
    ax.tick_params(axis='both', which='minor', labelsize=ticks_label_font_size)


def fig_history(fit):

    n_rows, n_cols = 2, 3
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(15, 10), dpi=200)

    axes = [[] for _ in range(n_cols)]
    for i in range(len(monkeys)):
        for j in range(3):
            axes[i].append(fig.add_subplot(gs[i, j]))

    for i, monkey in enumerate(monkeys):

        pra = fit[monkey]['pos_risk_aversion']
        nra = fit[monkey]['neg_risk_aversion']
        pdi = fit[monkey]['pos_distortion']
        ndi = fit[monkey]['neg_distortion']
        ppr = fit[monkey]['pos_precision']
        npr = fit[monkey]['neg_precision']

        log(f'Getting data for {monkey}...', name)

        for j, (pos_param, neg_param, y_lim, show_mid_line, param_name) in enumerate((
                (pra, nra, (-1, 1), True, r"$\omega$"),
                (pdi, ndi, (0, 1), False, r"$\alpha$"),
                (ppr, npr, (0, 5), False, r"$\lambda$")
        )):

            plot_history(
                ax=axes[i][j],
                pos_param=pos_param,
                neg_param=neg_param,
                y_lim=y_lim,
                show_mid_line=show_mid_line,
                param_name=param_name
            )

        # if show_average:
        #     plot.precision.plot(
        #         neg_risk_aversion=np.mean(nra),
        #         pos_risk_aversion=np.mean(pra),
        #         neg_distortion=np.mean(ndi),
        #         pos_distortion=np.mean(pdi),
        #         neg_precision=np.mean(npr),
        #         pos_precision=np.mean(ppr),
        #         color_gain=color_gain,
        #         color_loss=color_loss,
        #         ax=axes[i])

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()

    ax.text(
        s='A', x=-0.05, y=0.5, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s='B', x=-0.05, y=-0.1, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    gs.tight_layout(fig)
    fig.savefig(fname=f'{fig_folder}/supplementary_history.pdf')


def stats(fit):

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
        statsmodels.stats.multitest.multipletests(pvals=ps, alpha=0.01, method="b")

    for param, u, p, p_c in zip(("H: risk aversion", "H: distortion", "H: precision",
                                 "G: risk aversion", "G: distortion", "G: precision"), us, ps, p_corr):
        log(f'Comparision for {param} parameter values: u = {u}, p = {p:.3f}, p_c = {p_c:.3f}', name=name)


def main_for_review(force_data_import=False, force_fit=False):

    # Create fig folder
    os.makedirs(fig_folder, exist_ok=True)

    # Get data
    d = main.get_data(force_data_import)

    # Get fit
    fit = model.parameter_estimate.run_cross_validation(d, force_fit, randomize=False)

    # History
    fig_history(fit)

    # Stats for comparison of best parameter values
    stats(fit)

    # Freq risky choice against expected value
    main.freq_risk_against_exp_value(d)  # , f=plot.freq_risk_against_exp_value.sigmoid_one_param)

    # Utility
    # utility_multi(fit=fit, fig_name='utility_not_random_order', ordered_chunks=True, show_average=False)


if __name__ == '__main__':
    main_for_review(False, False)
