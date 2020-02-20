import os

import matplotlib.pyplot as plt


from parameters.parameters import FIG_FOLDER
from utils.log import log


NAME = "plot.utils"


def fig_name(fig_type, monkey):
    return os.path.join(FIG_FOLDER, f"{monkey}_{fig_type}.pdf")


def save_fig(fig, fig_type, monkey, pdf):

    log(f"Creating '{fig_type}' for monkey '{monkey}'...", name=NAME)
    plt.tight_layout()

    if pdf is None:
        plt.savefig(fig_name(fig_type=fig_type,
                             monkey=monkey))
    else:
        pdf.savefig(fig)

    log(f"Creating '{fig_type}' for monkey '{monkey}'...", name=NAME)
