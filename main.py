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

from utils.utils import today, log

name = "Main"

monkeys = 'Havane', 'Gladys'
color_loss, color_gain = 'C1', 'C0'
fig_folder = 'fig'


def exemplary_case(d):

    n_rows, n_cols = 1, 2
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)
    fig = plt.figure(figsize=(12, 5), dpi=200)
    axes = [fig.add_subplot(gs[0, i]) for i in range(len(monkeys))]

    for i, monkey in enumerate(monkeys):

        log(f'Getting data for {monkey}...', name)

        ex_d = data.filter.get_exemplary_case(d[monkey])

        plot.exemplary_case.plot(
            results=ex_d,
            color_gain=color_gain,
            color_loss=color_loss,
            ax=axes[i])

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()
    ax.text(
        s='A', x=0, y=0, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s='B', x=0.5, y=0, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    gs.tight_layout(fig)
    fig.savefig(fname=f'{fig_folder}/exemplary.pdf')


def control(d):

    n_rows, n_cols = 2, 1
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(4.7, 5.4), dpi=200)
    axes = [fig.add_subplot(gs[i, 0]) for i in range(len(monkeys))]

    for i, monkey in enumerate(monkeys):

        log(f'Getting data for {monkey}', name)

        alternatives, control_types, hits = data.filter.get_control(d[monkey])
        control_d = data.filter.cluster_hit_by_control_cond(alternatives, control_types, hits)

        plot.control.plot(
            results=control_d,
            color_gain=color_gain,
            color_loss=color_loss,
            ax=axes[i])

    gs.tight_layout(fig)

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()

    ax.text(
        s='A', x=-0.1, y=0.5, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s='B', x=-0.1, y=-0.02, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    fig.savefig(fname=f'{fig_folder}/control.pdf')


def freq_risk_against_exp_value(d):

    n_rows, n_cols = 2, 2
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)
    fig = plt.figure(figsize=(12, 10), dpi=200)
    axes = [[] for i in range(n_cols)]
    for i in range(len(monkeys)):
        for j in range(2):
            axes[i].append(fig.add_subplot(gs[i, j]))

    for i, monkey in enumerate(monkeys):

        log(f'Getting data for {monkey}...', name)

        for j, gain_only in enumerate((1, 0)):

            expected_values_differences, risky_choice_means = \
                data.filter.get_choose_risky_loss_or_gain_only(d[monkey], gain_only=gain_only)

            color = (color_loss, color_gain)[gain_only]

            plot.freq_risk_against_exp_value.plot(
                expected_values_differences=expected_values_differences,
                risky_choice_means=risky_choice_means,
                color=color,
                ax=axes[i][j])

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()
    ax.text(
        s='A', x=-0.05, y=0.5, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s='B', x=-0.05, y=-0.1, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    gs.tight_layout(fig)
    fig.savefig(fname=f'{fig_folder}/freq_risk_against_exp_value.pdf')


def utility_multi(fit):

    n_rows, n_cols = 1, 2
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)
    fig = plt.figure(figsize=(12, 5), dpi=200)
    axes = [fig.add_subplot(gs[0, i]) for i in range(len(monkeys))]

    for i, monkey in enumerate(monkeys):

        pra = fit[monkey]['pos_risk_aversion']
        nra = fit[monkey]['neg_risk_aversion']

        for j in range(len(fit[monkey]['pos_risk_aversion'])):
            plot.utility.plot(
                pos_risk_aversion=pra[j],
                neg_risk_aversion=nra[j],
                ax=axes[i], linewidth=1, alpha=0.5)

        plot.utility.plot(
            pos_risk_aversion=np.mean(pra),
            neg_risk_aversion=np.mean(nra),
            ax=axes[i])

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()  # plt.axis('off')
    ax.text(
        s='A', x=0, y=0, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s='B', x=0.5, y=0, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    gs.tight_layout(fig)
    fig.savefig(fname=f'{fig_folder}/utility.pdf')


def distortion_multi(fit):

    n_rows, n_cols = 1, 2
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(12, 5), dpi=200)

    axes = [fig.add_subplot(gs[0, i]) for i in range(len(monkeys))]

    for i, monkey in enumerate(monkeys):

        pdi = fit[monkey]['pos_distortion']
        ndi = fit[monkey]['neg_distortion']

        for j in range(len(pdi)):

            plot.probability_distortion.plot(
                neg_distortion=ndi[j],
                pos_distortion=pdi[j],
                color_loss=color_loss,
                color_gain=color_gain,
                alpha=0.5,
                linewidth=1,
                ax=axes[i])

        plot.probability_distortion.plot(
            neg_distortion=np.mean(ndi),
            pos_distortion=np.mean(pdi),
            color_loss=color_loss,
            color_gain=color_gain,
            ax=axes[i])

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()

    ax.text(
        s='A', x=-0.05, y=-0.05, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s='B', x=0.5, y=-0.05, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    gs.tight_layout(fig)
    fig.savefig(fname=f'{fig_folder}/probability_distortion.pdf')


def precision_multi(fit):

    n_rows, n_cols = 1, 2
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(12, 5), dpi=200)

    axes = [fig.add_subplot(gs[0, i]) for i in range(len(monkeys))]

    for i, monkey in enumerate(monkeys):

        pra = fit[monkey]['pos_risk_aversion']
        nra = fit[monkey]['neg_risk_aversion']
        pdi = fit[monkey]['pos_distortion']
        ndi = fit[monkey]['neg_distortion']
        ppr = fit[monkey]['pos_precision']
        npr = fit[monkey]['neg_precision']

        for j in range(len(pra)):

            plot.precision.plot(
                neg_risk_aversion=nra[j],
                pos_risk_aversion=pra[j],
                neg_distortion=ndi[j],
                pos_distortion=pdi[j],
                neg_precision=npr[j],
                pos_precision=ppr[j],
                color_gain=color_gain,
                color_loss=color_loss,
                ax=axes[i],
                linewidth=1,
                alpha=0.5
            )

        plot.precision.plot(
            neg_risk_aversion=np.mean(nra),
            pos_risk_aversion=np.mean(pra),
            neg_distortion=np.mean(ndi),
            pos_distortion=np.mean(pdi),
            neg_precision=np.mean(npr),
            pos_precision=np.mean(ppr),
            color_gain=color_gain,
            color_loss=color_loss,
            ax=axes[i])

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()

    ax.text(
        s='A', x=-0.05, y=-0.1, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s='B', x=0.49, y=-0.1, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    gs.tight_layout(fig)
    fig.savefig(fname=f'{fig_folder}/precision.pdf')


def main(force_data_import=False, force_fit=False):

    # Create fig folder
    os.makedirs(fig_folder, exist_ok=True)

    # Get data
    d = dict()
    for monkey in monkeys:

        log(f'Getting data for {monkey}...', name)

        d[monkey] = data.get.run(
            monkey=monkey, starting_point='2017-03-01', end_point=today(),
            database_path='data/results.db', force=force_data_import)

        days = np.unique(d[monkey].session)
        n_trials_per_days = np.zeros(len(days))
        for i, day in enumerate(days):
            n_trials_per_days[i] = np.sum(d[monkey].session == day)
        log(f'N days: {len(days)}', name)
        log(f'N trials per day: {np.mean(n_trials_per_days)} +/- {np.std(n_trials_per_days)} SD', name)

    # Exemplary case
    exemplary_case(d)

    # Control
    control(d)

    # Freq risky choice against expected value
    freq_risk_against_exp_value(d)

    # Get fit
    fit = model.parameter_estimate.run_cross_validation(d, force_fit)

    # Utility function
    utility_multi(fit)

    # Distortion
    distortion_multi(fit)

    # Precision
    precision_multi(fit)


if __name__ == '__main__':
    main(False, False)
