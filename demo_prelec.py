import numpy as np
import matplotlib.pyplot as plt


p = np.linspace(0.001, 1, 100)

alpha = np.array([0.5, 1, 1.5, 3, 50, 100000])

fig, ax = plt.subplots()

for a in alpha:
    y = np.exp(-(-np.log(p)) ** a)
    ax.plot(p, y, label=f'alpha={a}')

ax.legend()
ax.set_xlabel("p")
ax.set_ylabel("subjective p")
plt.tight_layout()
plt.savefig("fig/prelec.pdf")
plt.savefig("fig/prelec.png", dpi=60)