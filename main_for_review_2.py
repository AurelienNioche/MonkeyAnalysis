import os

import matplotlib.gridspec
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score
import statsmodels.api as sm
import statsmodels.stats.multitest

from utils.utils import log

import model.parameter_estimate
import data.filter

from main import utility, distortion, precision, exemplary_case, control, get_data

from main_for_review import stats_comparison_best_values

NAME = "Supp"

MONKEYS = 'Havane', 'Gladys'
COLOR_LOSS, COLOR_GAIN = 'C1', 'C0'
FIG_FOLDER = 'fig'

N_CHUNK = 20

FIG_BEST_PARAM_HISTORY = f'{FIG_FOLDER}/supplementary_history_{N_CHUNK}_chunk.pdf'


PARAMETERS = [
    'pos_risk_aversion',
    'neg_risk_aversion',
    'pos_distortion',
    'neg_distortion',
    'pos_precision',
    'neg_precision'
]


def display_table_content(fit):

    print("[LATEX TABLE CONTENT]")
    for monkey in MONKEYS:

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
        log(f"Line for {monkey} for table displaying best parameter values", name=NAME)
        print(dsp)
    print("[LATEX TABLE CONTENT]")


def control_history_sort_data(alternatives, control_types, hits, n_chunk):
    """
    Called by 'control history'
    :param alternatives:
    :param control_types:
    :param hits:
    :param n_chunk:
    :return:
    """
    control_conditions = data.filter.control_conditions

    # Pre-sort data
    sorted_data = {i: {} for i in control_conditions}

    for alt, ct, hit in zip(alternatives, control_types, hits):

        if alt not in sorted_data[ct].keys():
            sorted_data[ct][alt] = []

        sorted_data[ct][alt].append(hit)

    # Prepare container for output
    results = {i: [{} for _ in range(n_chunk)] for i in control_conditions}

    for cond in sorted_data.keys():

        log(f'Condition "{cond}"', NAME)

        d = sorted_data[cond]
        alternatives = sorted(list(d.keys()))

        for i, alt in enumerate(alternatives):

            n_trials = len(d[alt])

            reminder = n_trials % n_chunk

            idx = np.arange(n_trials)
            if reminder > 0:
                idx = idx[:-reminder]

            split = np.split(np.asarray(d[alt])[idx], n_chunk)

            for j, sp in enumerate(split):
                results[cond][j][alt] = np.mean(sp)

    return results


def control_history_plot(results, color, ax, last=False, ylabel="Success rate", title="Title", fontsize=5):
    """
    Called by 'control history'
    """

    n = len(results)  # results is a list (n=number of boxplot) of list (n=number of datapoints)

    tick_labels = [f"{i + 1}" for i in range(n)]

    # colors = ["black", color_gain, color_loss, color_gain, color_loss]
    positions = list(range(n))

    x_scatter = []
    y_scatter = []

    values_box_plot = []

    for i, res in enumerate(results):
        values_box_plot.append([])

        for v in results[i].values():

            # For box plot
            values_box_plot[-1].append(v)

            # For scatter
            y_scatter.append(v)
            x_scatter.append(i)

    assert len(x_scatter) == len(y_scatter)
    ax.scatter(x_scatter, y_scatter, c=color, s=10, alpha=0.5, linewidth=0.0, zorder=1)

    ax.axhline(0.5, linestyle='--', color='0.3', zorder=-10, linewidth=0.5)

    ax.set_yticks(np.arange(0.0, 1.1, 0.5))

    ax.tick_params(axis='both', labelsize=fontsize)

    # ax.set_xlabel("Type of control\nMonkey {}.".format(monkey), fontsize=fontsize)
    # ax.set_xlabel("Control type", fontsize=fontsize)

    ax.set_ylabel(ylabel, fontsize=fontsize)

    ax.set_ylim(-0.02, 1.02)

    # Boxplot
    bp = ax.boxplot(values_box_plot, positions=positions, labels=tick_labels, showfliers=False, zorder=2)

    for e in ['boxes', 'caps', 'whiskers', 'medians']:  # Warning: only one box, but several whiskers by plot
        for b in bp[e]:
            b.set(color='black')
            # b.set_alpha(1)

    if not last:
        ax.tick_params(
            axis='x',  # changes apply to the x-axis
            which='both',  # both major and minor ticks are affected
            bottom=False,  # ticks along the bottom edge are off
            top=False,  # ticks along the top edge are off
            labelbottom=False)  # labels along the bottom edge are off

    else:
        ax.set_xlabel('Chunk', fontsize=fontsize)
    ax.set_title(title, fontsize=fontsize+1)


def control_history(d, n_chunk,
                    labels=("Loss vs gains", "Diff. $x +$, same $p$", "Diff. $x -$, same $p$",
                            "Diff. $p$, same $x +$", "Diff. $p$, same $x -$"),
                    colors=("black", COLOR_GAIN, COLOR_LOSS, COLOR_GAIN, COLOR_LOSS)):

    n = len(MONKEYS) * len(data.filter.control_conditions)

    n_rows, n_cols = n, 1
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(5, 8), dpi=200)
    axes = [fig.add_subplot(gs[i, 0]) for i in range(n)]

    i = 0
    for monkey in MONKEYS:

        log(f"Creating fig 'control_history' for {monkey}", NAME)
        alternatives, control_types, hits = data.filter.get_control(d[monkey])

        control_d = control_history_sort_data(alternatives, control_types, hits, n_chunk=n_chunk)

        for cond, color, title in zip(data.filter.control_conditions, colors, labels):

            last = i == n-1

            control_history_plot(
                results=control_d[cond],
                color=color,
                ax=axes[i],
                last=last,
                title=title
            )

            i += 1

    gs.tight_layout(fig)

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()

    ax.text(
        s='  A', x=-0.1, y=0.5, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=15)
    ax.text(
        s='  B', x=-0.1, y=-0.02, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=15)

    fig.savefig(fname=f'{FIG_FOLDER}/control_history_{n_chunk}_chunks.pdf')


def plot_history(
        pos_param, neg_param, ax, y_lim, param_name, show_mid_line=False,
        axis_label_font_size=20,
        ticks_label_font_size=14,
        point_size=100):

    x_data = np.arange(len(pos_param)) + 1
    y_data_gain = pos_param
    y_data_loss = neg_param

    ax.scatter(x_data, y_data_gain, color=COLOR_GAIN, alpha=0.5, s=point_size)
    ax.scatter(x_data, y_data_loss, color=COLOR_LOSS, alpha=0.5, s=point_size)

    if show_mid_line:
        ax.axhline(0, alpha=0.5, linewidth=1, color='black', linestyle='--', zorder=-10)
    # ax.axvline(0, alpha=0.5, linewidth=1, color='black', linestyle='--', zorder=-10)

    ax.set_xlim((0.5, 10.5))
    ax.set_ylim(y_lim)
    ax.set_xticks((1, len(x_data)//2, len(x_data)))

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


def fig_history(fit, regression_param=None):

    n_rows, n_cols = 2, 3
    gs = matplotlib.gridspec.GridSpec(nrows=n_rows, ncols=n_cols)

    fig = plt.figure(figsize=(15, 10), dpi=200)

    axes = [[] for _ in range(n_cols)]
    for i in range(len(MONKEYS)):
        for j in range(3):
            axes[i].append(fig.add_subplot(gs[i, j]))

    for i, monkey in enumerate(MONKEYS):

        log(f"Creating 'fig_history' for {monkey}...", NAME)

        for j, (pos_param, neg_param, y_lim, show_mid_line, param_name) in enumerate((
                ('pos_risk_aversion', 'neg_risk_aversion', (-1, 1), True, r"$\omega$"),
                ('pos_distortion', 'neg_distortion', (0, 1), False, r"$\alpha$"),
                ('pos_precision', 'neg_precision', (0, 5), False, r"$\lambda$")
        )):

            plot_history(
                ax=axes[i][j],
                pos_param=fit[monkey][pos_param],
                neg_param=fit[monkey][neg_param],
                y_lim=y_lim,
                show_mid_line=show_mid_line,
                param_name=param_name
            )

            if regression_param:

                for param, color in zip((pos_param, neg_param), (COLOR_GAIN, COLOR_LOSS)):

                    alpha, beta, relevant = regression_param[monkey][param]

                    n = len(fit[monkey][param])
                    x = np.arange(1, n)
                    y = alpha + beta * x

                    print(alpha, beta, relevant)
                    if relevant:
                        line_style = "-"
                        alpha = 1
                    else:
                        line_style = ":"
                        alpha = 0.4
                    axes[i][j].plot(x, y, color=color, linestyle=line_style, alpha=alpha)

    ax = fig.add_subplot(gs[:, :])
    ax.set_axis_off()

    ax.text(
        s='A', x=-0.05, y=0.5, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)
    ax.text(
        s='B', x=-0.05, y=-0.1, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
        fontsize=30)

    gs.tight_layout(fig)
    fig.savefig(fname=FIG_BEST_PARAM_HISTORY)


def regression(x, y):

    reg = LinearRegression()
    reg.fit(np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1))
    # print("The linear model is: Y = {:.5} + {:.5}X".format(reg.intercept_[0], reg.coef_[0][0]))
    # predictions = reg.predict(np.array(x).reshape(-1, 1))

    alpha, beta = reg.intercept_[0], reg.coef_[0][0]

    x_2 = sm.add_constant(x)
    est = sm.OLS(y, x_2).fit()   # print(est.summary())
    f, p = est.fvalue, est.f_pvalue   # print(f"F={est.fvalue:.3f}, p={est.f_pvalue:.3f}, n={len(y)}")
    n = len(y)
    return f, p, n, alpha, beta


def stats_regression_best_values(fit):

    fs, ps, ns, alphas, betas = [], [], [], [], []

    for i, monkey in enumerate(MONKEYS):

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
        statsmodels.stats.multitest.multipletests(pvals=ps, alpha=0.01, method="b")

    rgr_line_param = {m: {} for m in MONKEYS}
    i = 0
    for monkey in MONKEYS:
        for param in PARAMETERS:
            rgr_line_param[monkey][param] = alphas[i], betas[i], p_corr[i] < 0.01
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
        log(f'Linear regression stats for {param} parameter values: F = {f:.3f}, p = {p:.3f}, p_c = {p_c:.3f}, n={n}'
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
        print(f"{monkey} & ${param}$ &" + r'$2\times' + f"{n}$ & ${alpha:.2f}$ & ${beta:.2f}$ & " +
              f"{fstat:.2f} & ${p_str}$ & ${p_c_str}$" + r"\\")
    print("[LATEX TABLE CONTENT]")

    return rgr_line_param


def main_for_review_2(force_data_import=False, force_fit=False):

    # Create fig folder
    os.makedirs(FIG_FOLDER, exist_ok=True)

    # Get data
    d = get_data(force_data_import)

    # Control history figure
    control_history(d, n_chunk=N_CHUNK)

    # Get fit
    fit = model.parameter_estimate.run_cross_validation(d, force=force_fit, n_chunk=N_CHUNK, randomize=False)

    # Print line for latex table
    display_table_content(fit)

    # Stats for comparison of best parameter values
    stats_comparison_best_values(fit)

    # Stats for comparison of best parameter values
    rgr_param = stats_regression_best_values(fit)

    # Create fig
    fig_history(fit, regression_param=rgr_param)

    # Utility function
    utility(fit)

    # Distortion function
    distortion(fit)

    # Precision
    precision(fit)

    # Exemplary case
    exemplary_case(d)

    # Control
    control(d)


if __name__ == '__main__':
    main_for_review_2(False, False)
