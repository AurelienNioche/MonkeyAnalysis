import matplotlib.pyplot as plt
import numpy as np

from plot.utils import save_fig


def write_pdf(d, monkey, pdf):


    n_trials= len(d.choice)

    lotteries = {}
    for i in range(n_trials):
        lt = (d.p.left[i],
              d.x.left[i],
              d.p.right[i],
              d.x.right[i])
        if lt in lotteries:
            lotteries[lt] += 1
        else:
            lt_r = (d.p.right[i],
                    d.x.right[i],
                    d.p.left[i],
                    d.x.left[i])
            if lt_r in lotteries:
                lotteries[lt_r] += 1
            else:
                if d.p.left[i] <= d.p.right[i]:
                    lotteries[lt] = 1
                else:
                    lotteries[lt_r] = 1

    counts = list(lotteries.values())
    n_per_lottery_mean = np.mean(counts)
    n_per_lottery_std = np.std(counts)

    n_control = 0
    success = 0

    for i in range(n_trials):
        if d.p.right[i] > d.p.left[i] and d.x.right[i] > d.x.left[i]:
            n_control += 1
            success += d.choice[i] == 1

        elif d.p.right[i] < d.p.left[i] and d.x.right[i] < d.x.left[i]:
            n_control += 1
            success += d.choice[i] == 0

        elif d.p.right[i] == d.p.left[i]:
            if d.x.right[i] > d.x.left[i]:
                n_control += 1
                success += d.choice[i] == 1

            elif d.x.right[i] < d.x.left[i]:
                n_control += 1
                success += d.choice[i] == 0

            else:
                pass
        elif d.x.right[i] == d.x.left[i]:
            if d.p.right[i] > d.p.left[i]:
                n_control += 1
                success += d.choice[i] == 1

            elif d.p.right[i] < d.p.left[i]:
                n_control += 1
                success += d.choice[i] == 0

            else:
                pass

    fo_st_dominance = success / n_control

    choice_right = (np.sum(d.choice) / n_trials)*100

    fig, ax = plt.subplots()

    t = f"{monkey}\n\n" \
        f"N trials = {n_trials}\n" \
        f"N per lottery = {n_per_lottery_mean:.2f} " \
        f"(+/- {n_per_lottery_std:.2f} STD)\n" \
        f"Choose right = {choice_right:.2f}%\n" \
        f"Respect of first-order stochastic dominance = {fo_st_dominance:.2f}%"

    ax.text(0.5, 0.5, t, fontsize=15, wrap=True, ha='center',
            va='center')

    ax.set_axis_off()
    save_fig(fig=fig, pdf=pdf, monkey=monkey, fig_type='INFO')
