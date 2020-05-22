import numpy as np
import matplotlib.pyplot as plt


def plot_scatter_metric(data, ax, y_label, x_tick_label, title,
                        color='C0', dot_size=20):

    # For scatter
    x_scatter = np.random.uniform(-0.05, 0.05, size=len(data))

    # Plot the scatter
    ax.scatter(x_scatter, data, c=color, s=dot_size,
               alpha=0.2, linewidth=0.0, zorder=1)

    # Plot the boxplot
    bp = ax.boxplot(data, positions=[0, ],
                    labels=[x_tick_label, ], showfliers=False, zorder=2)

    # Set the color of the boxplot
    for e in ['boxes', 'caps', 'whiskers', 'medians']:
        for b in bp[e]:
            b.set(color='black')

    # Set the label of the y axis
    ax.set_ylabel(y_label)

    # Set the title
    ax.set_title(title)


def plot(fit, param_labels, fig_path):

    n_param = len(param_labels)

    # Colors
    colors = [f"C{i}" for i in range(n_param)]

    fig, axes = plt.subplots(nrows=n_param, figsize=(4, 3*n_param))

    for i in range(n_param):

        ax = axes[i]
        param_name = param_labels[i]
        title = f"Distribution of best-fit values for {param_name}"
        data = [np.mean(fit[k][param_name])
                for k in fit.keys()]

        plot_scatter_metric(ax=ax, data=data,
                            title=title,
                            y_label="Value",
                            x_tick_label=param_name,
                            color=colors[i],
                            dot_size=40)
    plt.tight_layout()
    plt.savefig(fig_path)


def demo():
    fit = {"mike": {"alpha": np.random.random(10), "epsilon": np.random.random(10)},
           "brian": {"alpha": np.random.random(10), "epsilon": np.random.random(10)},}
    plot(fit=fit)


if __name__ == "__main__":
    demo()
