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

SAME_P = 'same p'
SAME_X = 'same x'

LABELS_CONTROL = {
    SAME_P: "Diff. $x$, same $p$",
    SAME_X: "Diff. $p$, same $x$"
}

CONTROL_CONDITIONS = SAME_P, SAME_X

LEFT = 'left'
RIGHT = 'right'

CHOOSE_RIGHT = 'choose_right'
MONKEY_NAME = 'monkey'
N_TRIALS = 'n_trials'

SIG_STEEP = 'sig_steep'
SIG_MID = 'sig_mid'
