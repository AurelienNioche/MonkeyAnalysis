import os
import xlsxwriter
import numpy as np
import warnings

from parameters.parameters import DATA_FOLDER

from parameters.parameters import \
    CONTROL_CONDITIONS, CHOOSE_RIGHT, MONKEY_NAME, N_TRIALS, SIG_STEEP, \
    SIG_MID, SAME_P, SAME_X

from utils.log import log

NAME = 'analysis.summary'


class Summary:

    XLS_NAME = "summary.xlsx"

    def __init__(self, class_model):

        self.class_model = class_model

        self.content = {}

        self.doc = {
            MONKEY_NAME: "Name of the monkey",
            N_TRIALS: "Total number of trials",
            CHOOSE_RIGHT: "Frequency with which the monkey "
                          "chooses the target on the right side",
            "risk_aversion": "Best-fit parameter value "
                             "describing the risk aversion",
            "distortion": "Best-fit parameter value "
                          "describing the probability distortion",
            "precision": "Best-fit parameter value "
                         "describing the precision",
            SAME_P: "Median of the frequencies with which "
                         "the monkey chooses the best target "
                         "for a specific alternative "
                         "such that: "
                         "(i) a best option exists, "
                         "(ii) probabilities of non-zero outputs are the same, "
                         "(iii) the non-zero outputs are different "
                         "(iv) the possible outputs are only zero and positive rewards",
            SAME_X: "Median of the frequencies with which "
                          "the monkey chooses the best target "
                          "for a specific alternative "
                          "such that: "
                          "(i) a best option exists, "
                          "(ii) probabilities of non-zero outputs are different, "
                          "(iii) the non-zero outputs are the same "
                          "(iv) the possible outputs are only zero and positive rewards",
            SIG_STEEP: "Best-fit parameter value for the steepness of the curve for the 'same p - gain vs loss' control trials",
            SIG_MID: "Best-fit parameter value for the midpoint of the curve for the 'same p - gain vs loss'control trials",
        }

    def __getitem__(self, item):
        try:
            return self.content[item]
        except KeyError:
            self.content[item] = []
            return self.content[item]

    def __setitem__(self, key, value):
        self.content[key] = value

    def export_as_xlsx(self):

        os.makedirs(DATA_FOLDER, exist_ok=True)
        xls_path = os.path.join(DATA_FOLDER, self.XLS_NAME)
        workbook = xlsxwriter.Workbook(xls_path)

        columns = self.content.keys()

        # Write data
        worksheet = workbook.add_worksheet('data')
        for j, c in enumerate(columns):
            c_name = self._format_column_name(c)
            worksheet.write(0, j, c_name)

        for j, col_name in enumerate(columns):

            data_col = self[col_name]
            for i, d in enumerate(data_col):

                worksheet.write(i + 1, j, d)

        # Write doc
        worksheet = workbook.add_worksheet('doc')
        for j, c in enumerate(columns):
            c_name = self._format_column_name(c)
            worksheet.write(j, 0, c_name)
            try:
                worksheet.write(j, 1, self.doc[c])
            except KeyError:
                warnings.warn(f"Missing doc for '{c}'")

        workbook.close()

        log(f"Summary exported in the file '{xls_path}'\n", name=NAME)

    @staticmethod
    def _format_column_name(c):
        return c.replace(" ", "_").replace("-", "")

    def append_performance_to_control(self, control_d):

        for cd in CONTROL_CONDITIONS:
            median = np.median(list(control_d[cd].values()))
            self[cd].append(median)

    def append_cpt_fit(self, cpt_fit):
        for pr in self.class_model.param_labels:
            mean = np.mean(cpt_fit[pr])
            self[pr].append(mean)

    def append_control_sig_fit(self, control_sig_fit):

        fit = control_sig_fit
        for cd in CONTROL_CONDITIONS:
            for pr in (SIG_MID, SIG_STEEP):
                self[f"{cd}_{pr}"].append(fit[cd][pr])

    def append_risk_sig_fit(self, risk_sig_fit):
        for pr in (SIG_MID, SIG_STEEP):
            self[f"risk_{pr}"].append(risk_sig_fit[pr])


def create(info_data, control_data,
           cpt_fit, control_sig_fit,
           risk_sig_fit, class_model):

    summary = Summary(class_model=class_model)

    monkeys = sorted(info_data.keys())
    for m in monkeys:
        # Add monkey name
        summary[MONKEY_NAME].append(m)

        # Add number of trials
        summary[N_TRIALS].append(info_data[m].n_trials)

        # Add side bias
        summary[CHOOSE_RIGHT].append(info_data[m].choose_right)

        # Add median for each type of control
        summary.append_performance_to_control(control_data[m])

        # Add best-fit parameters
        summary.append_cpt_fit(cpt_fit[m])
        summary.append_control_sig_fit(control_sig_fit[m])
        summary.append_risk_sig_fit(risk_sig_fit[m])

    summary.export_as_xlsx()
