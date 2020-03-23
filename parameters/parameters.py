import os
from utils.log import log

NAME = "parameters.parameters"

DATE_FORMAT = '%Y-%m-%d'

DATA_FOLDER = 'data'
log(f"The data folder is: {os.path.abspath(DATA_FOLDER)}\n",
    NAME)

FIG_FOLDER = 'fig'
log(f"The figure folder is: {os.path.abspath(FIG_FOLDER)}\n",
    NAME)

BACKUP_FOLDER = os.path.join(DATA_FOLDER, 'pickle')

# Create folders
for folder in FIG_FOLDER, DATA_FOLDER, BACKUP_FOLDER:
    os.makedirs(folder, exist_ok=True)

FIG_PRECISION = "precision"

FIG_PROBABILITY_DISTORTION = "probability_distortion"

FIG_UTILITY = "utility"

FIG_CONTROL = "control"

FIG_FREQ_RISK_AGAINST_EXP_VALUE = "freq_risk_against_exp_value"

FIG_EXEMPLARY_CASE = "exemplary"

FIG_HISTORY_CONTROL = "supplementary_history_control"

FIG_HISTORY_BEST_PARAM = "supplementary_history_best_param"

XLS_NAME = "data.xlsx"

MODEL_PARAMETERS = [
    'pos_risk_aversion',
    'neg_risk_aversion',
    'pos_distortion',
    'neg_distortion',
    'pos_precision',
    'neg_precision'
]

COLOR_LOSS = 'C1'
COLOR_GAIN = 'C0'

SAME_P_GAIN_VS_LOSS = 'same p - gain vs loss'
SAME_P_GAIN = 'same p - gain'
SAME_P_LOSS = 'same p - loss'
SAME_X0_GAIN = 'same x0 - gain'
SAME_X0_LOSS = 'same x0 - loss'

GAIN = 'gain'
LOSS = 'loss'

CONTROL_CONDITIONS = SAME_P_GAIN_VS_LOSS, \
                     SAME_P_GAIN, SAME_P_LOSS, \
                     SAME_X0_GAIN, SAME_X0_LOSS
LEFT = 'left'
RIGHT = 'right'

CHOOSE_RIGHT = 'choose_right'
MONKEY_NAME = 'monkey_name'
N_TRIALS = 'n_trials'