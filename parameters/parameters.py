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
FIG_CONTROL_SIGMOID = "fig_control_sigmoid"

FIG_FREQ_RISK_AGAINST_EXP_VALUE = "freq_risk_against_exp_value"

FIG_EXEMPLARY_CASE = "exemplary"

FIG_HISTORY_CONTROL = "supplementary_history_control"

FIG_HISTORY_BEST_PARAM = "supplementary_history_best_param"

XLS_NAME = "data.xlsx"

POS_RISK_AVERSION = 'pos_risk_aversion'
NEG_RISK_AVERSION = 'neg_risk_aversion'
POS_DISTORTION = 'pos_distortion'
NEG_DISTORTION = 'neg_distortion'
POS_PRECISION = 'pos_precision'
NEG_PRECISION = 'neg_precision'

MODEL_PARAMETERS = [
    POS_RISK_AVERSION,
    NEG_RISK_AVERSION,
    POS_DISTORTION,
    NEG_DISTORTION,
    POS_PRECISION,
    NEG_PRECISION
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


DOC = {
    MONKEY_NAME: "Name of the monkey",
    N_TRIALS: "Total number of trials",
    CHOOSE_RIGHT: "Frequency with which the monkey chooses the target on the right side",
    POS_RISK_AVERSION: "Best-fit parameter value "
                       "describing the risk aversion in gains",
    NEG_RISK_AVERSION: "Best-fit parameter value "
                       "describing the risk aversion in losses",
    POS_DISTORTION: "Best-fit parameter value "
                    "describing the probability distortion in gains",
    NEG_DISTORTION: "Best-fit parameter value "
                    "describing the probability distortion in losses",
    POS_PRECISION: "Best-fit parameter value "
                   "describing the precision in gains",
    NEG_PRECISION: "Best-fit parameter value "
                   "describing the precision in losses",
    SAME_P_GAIN_VS_LOSS: "Median of the frequencies with which "
                         "the monkey chooses the best target "
                         "for a specific alternative such that: "
                         "(i) a best option exists, "
                         "(ii) one target contains a gain and the other a loss",
    SAME_P_GAIN: "Median of the frequencies with which "
                 "the monkey chooses the best target "
                 "for a specific alternative "
                 "such that: "
                 "(i) a best option exists, "
                 "(ii) probabilities of non-zero outputs are the same, "
                 "(iii) the non-zero outputs are different "
                 "(iv) the possible outputs are only zero and positive rewards",
    SAME_P_LOSS: "Median of the frequencies with which "
                 "the monkey chooses the best target "
                 "for a specific alternative "
                 "such that: "
                 "(i) a best option exists, "
                 "(ii) probabilities of non-zero outputs are the same, "
                 "(iii) the non-zero outputs are different "
                 "(iv) the possible outputs are only zero and negative rewards",
    SAME_X0_GAIN: "Median of the frequencies with which "
                 "the monkey chooses the best target "
                 "for a specific alternative "
                 "such that: "
                 "(i) a best option exists, "
                 "(ii) probabilities of non-zero outputs are different, "
                 "(iii) the non-zero outputs are the same "
                 "(iv) the possible outputs are only zero and positive rewards",
    SAME_X0_LOSS: "Median of the frequencies with which "
                 "the monkey chooses the best target "
                 "for a specific alternative "
                 "such that: "
                 "(i) a best option exists, "
                 "(ii) probabilities of non-zero outputs are different, "
                 "(iii) the non-zero outputs are the same "
                 "(iv) the possible outputs are only zero and negative rewards",
}
