import os

DATE_FORMAT = '%Y-%m-%d'

FIG_FOLDER = 'fig'
BACKUP_FOLDER = os.path.join('data', 'pickle')

# Create folders
for folder in FIG_FOLDER, BACKUP_FOLDER:
    os.makedirs(folder, exist_ok=True)


N_CHUNK = 20

FIG_PRECISION = \
    os.path.join(FIG_FOLDER, "precision.pdf")

FIG_PROBABILITY_DISTORTION = \
    os.path.join(FIG_FOLDER, "probability_distortion.pdf")

FIG_UTILITY = \
    os.path.join(FIG_FOLDER, "utility.pdf")

FIG_CONTROL = \
    os.path.join(FIG_FOLDER, "control.pdf")

FIG_FREQ_RISK_AGAINST_EXP_VALUE = \
    os.path.join(FIG_FOLDER, "freq_risk_against_exp_value.pdf")

FIG_EXEMPLARY_CASE = \
    os.path.join(FIG_FOLDER, "exemplary.pdf")

FIG_HISTORY_CONTROL = \
    os.path.join(FIG_FOLDER, "supplementary_history_control.pdf")

FIG_HISTORY_BEST_PARAM = \
    os.path.join(FIG_FOLDER, f"supplementary_history_best_param.pdf")


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
