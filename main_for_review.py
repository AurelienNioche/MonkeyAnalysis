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


def stats_comparison_best_values(fit):

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


def control_history_sort_data(alternatives, control_types, hits, n_chuncks):

    control_conditions = data.filter.control_conditions

    # Pre-sort data
    sorted_data = {i: {} for i in control_conditions}

    for alt, ct, hit in zip(alternatives, control_types, hits):

        if alt not in sorted_data[ct].keys():
            sorted_data[ct][alt] = []

        sorted_data[ct][alt].append(hit)

    # Prepare container for output
    results = {i: [{} for _ in range(n_chuncks)] for i in control_conditions}

    for cond in sorted_data.keys():

        log(f'Condition "{cond}"', name)

        d = sorted_data[cond]

        alternatives = sorted(list(d.keys()))

        n_trials = []
        means = []

        for i, alt in enumerate(alternatives):

            split = np.split(np.asarray(d[alt]), n_chuncks)

            n = len(d[alt])
            mean = np.mean(d[alt])
            n_trials.append(n)

            for j in split:

                results[cond][j][alt] = mean

            means.append(mean)

            log(f'{i} {alt}: mean {mean:.2f}, n {n}', name)

    return results


def control_history_plot(results, color, ax):

    n = len(results)  # results is a list (n=number of boxplot) of list (n=number of datapoints)

    tick_labels = [f"{i + 1}" for i in range(n)]

    # colors = ["black", color_gain, color_loss, color_gain, color_loss]
    positions = list(range(n))

    x_scatter = []
    y_scatter = []

    values_box_plot = []

    for i, cond in enumerate(results):
        values_box_plot.append([])

        for v in results[i]:

            # For box plot
            values_box_plot[-1].append(v)

            # For scatter
            y_scatter.append(v)
            x_scatter.append(i)

    fontsize = 10

    ax.scatter(x_scatter, y_scatter, c=color, s=30, alpha=0.5, linewidth=0.0, zorder=1)

    ax.axhline(0.5, linestyle='--', color='0.3', zorder=-10, linewidth=0.5)

    ax.set_yticks(np.arange(0.4, 1.1, 0.2))

    ax.tick_params(axis='both', labelsize=fontsize)

    # ax.set_xlabel("Type of control\nMonkey {}.".format(monkey), fontsize=fontsize)
    # ax.set_xlabel("Control type", fontsize=fontsize)
    ax.set_ylabel("Success rate", fontsize=fontsize)

    ax.set_ylim(0.35, 1.02)

    # Boxplot
    bp = ax.boxplot(values_box_plot, positions=positions, labels=tick_labels, showfliers=False, zorder=2)

    for e in ['boxes', 'caps', 'whiskers', 'medians']:  # Warning: only one box, but several whiskers by plot
        for b in bp[e]:
            b.set(color='black')
            # b.set_alpha(1)

    ax.set_aspect(3)


def control_history(d):

    n_rows, n_cols = 10, 1
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(4.7, 5.4), dpi=200)
    axes = [fig.add_subplot(gs[i, 0]) for i in range(len(monkeys) * len(data.filter.control_conditions))]

    i = 0
    for monkey in monkeys:

        log(f'Getting data for {monkey}', name)
        alternatives, control_types, hits = data.filter.get_control(d[monkey])

        control_d = control_history_sort_data(alternatives, control_types, hits)

        for cond, color in zip(data.filter.control_conditions,
                               ("black", color_gain, color_loss, color_gain, color_loss)):

            control_history_plot(
                results=control_d[cond],
                color_gain=color,
                ax=axes[i])

            i += 1

    gs.tight_layout(fig)

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()

    ax.text(
        s='A', x=-0.1, y=0.5, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=15)
    ax.text(
        s='B', x=-0.1, y=-0.02, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=15)

    fig.savefig(fname=f'{fig_folder}/control_history.pdf')


def main_for_review(force_data_import=False, force_fit=False):

    # Create fig folder
    os.makedirs(fig_folder, exist_ok=True)

    # Get data
    d = main.get_data(force_data_import)

    # Control history
    control_history(d)

    # Get fit
    fit = model.parameter_estimate.run_cross_validation(d, force_fit, randomize=False)

    # History
    fig_history(fit)

    # Stats for comparison of best parameter values
    stats_comparison_best_values(fit)

    # Freq risky choice against expected value
    main.freq_risk_against_exp_value(d)  # , f=plot.freq_risk_against_exp_value.sigmoid_one_param)

    # Utility
    # utility_multi(fit=fit, fig_name='utility_not_random_order', ordered_chunks=True, show_average=False)


if __name__ == '__main__':
    main_for_review(False, False)
