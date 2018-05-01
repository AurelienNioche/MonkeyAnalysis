import os
import numpy as np
import matplotlib.pyplot as plt


def u(m, max_m=100, w=0.5):
    return (m/max_m) ** w


def main(show='risky'):

    assert show in (-1, 0, 1, 2, 'raw', 'certainty', 'risky', 'both')

    x = np.linspace(0, 100, 1000)
    y = u(x)

    plt.plot(x, y, color='black', linewidth=3, zorder=-1)
    plt.xticks(np.arange(0, 101, 25))
    plt.yticks(np.arange(0, 1.1, 0.25))
    plt.xlabel('€')
    plt.ylabel('u')

    if show in (0, 2, 'risky', 'both'):
        plt.plot([0, 100], [0, 1], color='C0', linestyle=':')
        plt.axvline(x=100, linestyle='--', color='C0', ymax=0.95)

        plt.axhline(y=0.5, color='C0', xmax=0.5, linestyle='--')
        plt.scatter(x=(50,), y=(0.5,), color='C0')
        plt.scatter(x=(0, 100), y=(0, 1), color='C0', marker='s')

    if show in (1, 2, 'certainty', 'both'):
        plt.scatter(x=(50,), y=(u(50),), color='C1')
        plt.axhline(y=u(50), color='C1', xmax=0.5, linestyle='--')
        plt.axvline(x=50, linestyle='--', color='C1', ymax=u(50) - 0.03)

    plt.savefig(os.path.expanduser(f'~/Desktop/illustrationUtility_{show}.pdf'))
    plt.show()


if __name__ == "__main__":
    main(-1)
