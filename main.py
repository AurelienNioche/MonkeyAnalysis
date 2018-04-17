import os
import matplotlib.gridspec
import matplotlib.pyplot as plt

import model.parameter_estimate

import plot.utility
import plot.precision
import plot.probability_distortion
import plot.control
import plot.exemplary_case
import plot.freq_risk_against_exp_value

import data.manager
import data.filter

from utils import utils


def main(force=False):

    monkeys = "Havane", "Gladys"

    d = dict()

    for monkey in monkeys:
        d[monkey] = data.manager.import_data(
            monkey=monkey, starting_point="2017-04-01", end_point=utils.today(),
            database_path="data/results.db", force=force)

    # ---------------------------- #

    fig_folder = "fig"
    os.makedirs(fig_folder, exist_ok=True)

    # ----------------------- #

    color_loss, color_gain = 'C1', 'C0'

    # ------- EXEMPLARY CASE ------------------ #

    n_rows, n_cols = 1, 2
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(12, 5), dpi=200)

    for i, monkey in enumerate(monkeys):

        ex_d = data.filter.get_exemplary_case(d[monkey])

        plot.exemplary_case.plot(
            results=ex_d,
            color_gain=color_gain,
            color_loss=color_loss,
            subplot_spec=gs[0, i], fig=fig)

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()
    ax.text(
        s="A", x=0, y=0, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s="B", x=0.5, y=0, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    gs.tight_layout(fig)
    fig.savefig(fname=f"{fig_folder}/exemplary.pdf")

    # ------------- CONTROL ------------------ #

    n_rows, n_cols = 2, 1
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(4.7, 5.4), dpi=200)

    for i, monkey in enumerate(monkeys):

        control_d = data.filter.get_control(d[monkey])

        plot.control.plot(
            results=control_d,
            color_gain=color_gain,
            color_loss=color_loss,
            subplot_spec=gs[i, 0], fig=fig)

    gs.tight_layout(fig)

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()

    ax.text(
        s="A", x=-0.1, y=0.5, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s="B", x=-0.1, y=-0.02, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    fig.savefig(fname=f"{fig_folder}/control.pdf")

    # ---------- FREQ RISKY VS EXP VALUE ----------- #

    n_rows, n_cols = 2, 2
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(12, 10), dpi=200)

    for i, monkey in enumerate(monkeys):
        for j, gain_only in enumerate((1, 0)):

            expected_values_differences, risky_choice_means = \
                data.filter.get_choose_risky_loss_or_gain_only(d[monkey], gain_only=gain_only)

            color = (color_loss, color_gain)[gain_only]

            plot.freq_risk_against_exp_value.plot(
                expected_values_differences=expected_values_differences,
                risky_choice_means=risky_choice_means,
                color=color,
                subplot_spec=gs[i, j], fig=fig)

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()
    ax.text(
        s="A", x=-0.05, y=0.5, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s="B", x=-0.05, y=-0.1, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    gs.tight_layout(fig)
    fig.savefig(fname=f"{fig_folder}/freq_risk_against_exp_value.pdf")

    # -----------  Get estimate ------------------- #

    r = model.parameter_estimate.run(d)

    # -------------- UTILITY ----------------- #

    n_rows, n_cols = 1, 2
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(12, 5), dpi=200)

    for i, monkey in enumerate(monkeys):

        plot.utility.plot(
            pos_risk_aversion=r[monkey]["pos_risk_aversion"],
            neg_risk_aversion=r[monkey]["neg_risk_aversion"],
            subplot_spec=gs[0, i], fig=fig)

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()  # plt.axis('off')
    ax.text(
        s="A", x=0, y=0, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s="B", x=0.5, y=0, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    gs.tight_layout(fig)
    fig.savefig(fname=f"{fig_folder}/utility.pdf")

    # -------------- DISTORTION ------------ #

    n_rows, n_cols = 1, 2
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(12, 5), dpi=200)

    for i, monkey in enumerate(monkeys):

        plot.probability_distortion.plot(
            neg_distortion=r[monkey]["neg_distortion"],
            pos_distortion=r[monkey]["pos_distortion"],
            color_loss=color_loss,
            color_gain=color_gain,
            subplot_spec=gs[0, i], fig=fig)

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()

    ax.text(
        s="A", x=-0.05, y=-0.05, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s="B", x=0.5, y=-0.05, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    gs.tight_layout(fig)
    fig.savefig(fname=f"{fig_folder}/probability_distortion.pdf")

    # --------------- PRECISION ----------------- #

    n_rows, n_cols = 1, 2
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(12, 5), dpi=200)

    for i, monkey in enumerate(monkeys):

        plot.precision.plot(
            neg_risk_aversion=r[monkey]["neg_risk_aversion"],
            pos_risk_aversion=r[monkey]["pos_risk_aversion"],
            neg_distortion=r[monkey]["neg_distortion"],
            pos_distortion=r[monkey]["pos_distortion"],
            neg_precision=r[monkey]["neg_precision"],
            pos_precision=r[monkey]["pos_precision"],
            color_gain=color_gain,
            color_loss=color_loss,
            subplot_spec=gs[0, i], fig=fig)

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()

    ax.text(
        s="A", x=-0.05, y=-0.1, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s="B", x=0.49, y=-0.1, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    gs.tight_layout(fig)
    fig.savefig(fname=f"{fig_folder}/precision.pdf")


if __name__ == "__main__":
    main()
