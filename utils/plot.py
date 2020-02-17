import os
from parameters.parameters import FIG_FOLDER


def fig_name(fig_type, monkey):
    return os.path.join(FIG_FOLDER, f"{monkey}_{fig_type}.pdf")
