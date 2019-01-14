from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


def now():
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")


def today():
    return datetime.now().strftime("%Y-%m-%d")


def log(msg="", name=""):
    print("[{}] [{}] {}".format(now(), name, msg))


def generate_colors(n, colormap='winter_r'):

    # To generate colors
    cmap = plt.get_cmap(colormap)
    return [cmap(i) for i in np.linspace(0, 0.9, n)]
