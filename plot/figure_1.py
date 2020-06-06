import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


from .subplot import history_control
from .subplot import precision
from .subplot import probability_distortion
from .subplot import utility
from .subplot import control
from .subplot import freq_risk
from .subplot import control_sigmoid
from .subplot import info
from .subplot import best_param_distrib
from .subplot import LLS_BIC_distrib

from plot.tools.tools import add_letter

from analysis.model.stats import stats_regression_best_values
from analysis.model.model import AgentSideAdditive
# DMSciReports, AgentSoftmax, AgentSide

from parameters.parameters import CONTROL_CONDITIONS, \
    FIG_FOLDER, BACKUP_FOLDER, EXPORT_FOLDER, GAIN, LOSS
from analysis.data_preprocessing \
    import get_control_data, get_control_sigmoid_data, \
    get_freq_risk_data, get_info_data, get_control_history_data, \
    get_control_stats

from analysis.model.parameter_estimate import get_parameter_estimate


def figure_1(a):

    nrows, ncols = 2, 3
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols,
                             figsize=(6*ncols, 6*nrows))

    colors = ['C0', 'C1']

    linestyles = ['--' if i in ('Havane', 'Gladys') else ':'
                  for i in a.monkeys]

    for i, cond in enumerate((GAIN, LOSS)):
        # Fig: Utility function
        data = {'class_model': a.class_model,
                'cond': cond}
        for param in ("risk_aversion", "distortion",
                      "precision", "side_bias"):
            data[param] = [np.mean(a.cpt_fit[cond][m][param])
                           for m in a.monkeys]

        utility.plot(ax=axes[i, 0], data=data, color=colors[i],
                     linestyles=linestyles)
        add_letter(axes[i, 0], i=i*3)
        probability_distortion.plot(
            ax=axes[i, 1], data=data,
            color=colors[i],
            linestyles=linestyles)
        add_letter(axes[i, 1], i=i*3+1)
        precision.plot(ax=axes[i, 2], data=data, color=colors[i],
                       linestyles=linestyles)
        add_letter(axes[i, 2], i=i * 3 + 2)

    fig_path = os.path.join(FIG_FOLDER, "figure_1.pdf")
    plt.tight_layout()
    plt.savefig(fig_path)
    print(f"Figure {fig_path} created!")