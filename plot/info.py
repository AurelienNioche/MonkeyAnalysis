import matplotlib.pyplot as plt
import numpy as np

from plot.utils import save_fig

from stimuli.models import Stimuli


def write_pdf(info, monkey, pdf):

    fig, ax = plt.subplots()

    t = f"{monkey}\n\n" \
        f"N lottery pairs = {info.n_lotteries}\n" \
        f"N total trials = {info.n_trials}\n" \
        f"N trials per lottery pair = {info.n_per_lottery_mean:.2f} " \
        f"(+/- {info.n_per_lottery_std:.2f} STD)\n" \
        f"Choose right = {info.choose_right*100:.2f}%\n" \
        f"Choose the best option if it exists = {info.choose_best*100:.2f}%"

    ax.text(0.5, 0.5, t, fontsize=15, wrap=True, ha='center',
            va='center')

    ax.set_axis_off()
    save_fig(fig=fig, pdf=pdf, monkey=monkey, fig_type='info')
