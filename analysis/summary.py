import os
import xlsxwriter
import numpy as np

from parameters.parameters import DATA_FOLDER

from parameters.parameters import MODEL_PARAMETERS, \
    CONTROL_CONDITIONS, CHOOSE_RIGHT, MONKEY_NAME, N_TRIALS, DOC, \
    CONTROL_SIG_PARAM, RISK_SIG_PARAM, \
    SIG_STEEP_SAME_P_GAIN_VS_LOSS, \
    SIG_STEEP_SAME_P_GAIN, \
    SIG_STEEP_SAME_P_LOSS, \
    SIG_STEEP_SAME_X0_GAIN, \
    SIG_STEEP_SAME_X0_LOSS, \
    SIG_MID_SAME_P_GAIN_VS_LOSS, \
    SIG_MID_SAME_P_GAIN, \
    SIG_MID_SAME_P_LOSS, \
    SIG_MID_SAME_X0_GAIN, \
    SIG_MID_SAME_X0_LOSS, \
    SAME_P_GAIN_VS_LOSS, \
    SAME_P_GAIN, \
    SAME_P_LOSS, \
    SAME_X0_GAIN, \
    SAME_X0_LOSS, \
    SIG_STEEP, \
    SIG_MID, \
    SIG_STEEP_RISK_GAIN, SIG_STEEP_RISK_LOSS, \
    SIG_MID_RISK_GAIN, SIG_MID_RISK_LOSS, \
    GAIN, LOSS


class Summary:

    def __init__(self):

        self.columns = self._get_columns()

        self.summary = {k: [] for k in self.columns}

    @staticmethod
    def _get_columns():

        col = [MONKEY_NAME, N_TRIALS, CHOOSE_RIGHT]

        for cat in (CONTROL_CONDITIONS, MODEL_PARAMETERS,
                    CONTROL_SIG_PARAM, RISK_SIG_PARAM):
            for cd in cat:
                col.append(cd)

        return col

    def __getitem__(self, item):
        return self.summary[item]

    def __setitem__(self, key, value):
        self.summary[key] = value

    def export_as_xlsx(self, xls_name="summary.xlsx"):
        os.makedirs(DATA_FOLDER, exist_ok=True)

        workbook = xlsxwriter.Workbook(os.path.join(DATA_FOLDER,
                                                    xls_name))

        # Write data
        worksheet = workbook.add_worksheet('data')
        for j, c in enumerate(self.columns):
            c_name = self._format_column_name(c)
            worksheet.write(0, j, c_name)

        for j, col_name in enumerate(self.columns):

            data_col = self[col_name]
            for i, d in enumerate(data_col):

                worksheet.write(i + 1, j, d)

        # Write doc
        worksheet = workbook.add_worksheet('doc')
        for j, c in enumerate(self.columns):
            c_name = self._format_column_name(c)
            worksheet.write(j, 0, c_name)
            worksheet.write(j, 1, DOC[c])

        workbook.close()

    @staticmethod
    def _format_column_name(c):
        return c.replace(" ", "_").replace("-", "")

    def append_performance_to_control(self, control_d):

        for cd in CONTROL_CONDITIONS:
            median = np.median(list(control_d[cd].values()))
            self[cd].append(median)

    def append_cpt_fit(self, cpt_fit):
        for pr in MODEL_PARAMETERS:
            mean = np.mean(cpt_fit[pr])
            self[pr].append(mean)

    def append_control_sig_fit(self, control_sig_fit):

        fit = control_sig_fit

        self[SIG_STEEP_SAME_P_GAIN_VS_LOSS].append(
            fit[SAME_P_GAIN_VS_LOSS][SIG_STEEP])
        self[SIG_MID_SAME_P_GAIN_VS_LOSS].append(
            fit[SAME_P_GAIN_VS_LOSS][SIG_MID])

        self[SIG_STEEP_SAME_P_GAIN].append(
            fit[SAME_P_GAIN][SIG_STEEP])
        self[SIG_MID_SAME_P_GAIN].append(
            fit[SAME_P_GAIN][SIG_MID])

        self[SIG_STEEP_SAME_P_LOSS].append(
            fit[SAME_P_LOSS][SIG_STEEP])
        self[SIG_MID_SAME_P_LOSS].append(
            fit[SAME_P_LOSS][SIG_MID])

        self[SIG_STEEP_SAME_X0_GAIN].append(
            fit[SAME_X0_GAIN][SIG_STEEP])
        self[SIG_MID_SAME_X0_GAIN].append(
            fit[SAME_X0_GAIN][SIG_MID])

        self[SIG_STEEP_SAME_X0_LOSS].append(
            fit[SAME_X0_LOSS][SIG_STEEP])
        self[SIG_MID_SAME_X0_LOSS].append(
            fit[SAME_X0_LOSS][SIG_MID])

    def append_risk_sig_fit(self, risk_sig_fit):
        fit = risk_sig_fit

        self[SIG_STEEP_RISK_GAIN].append(
            fit[GAIN][SIG_STEEP])
        self[SIG_MID_RISK_GAIN].append(
            fit[GAIN][SIG_MID])

        self[SIG_STEEP_RISK_LOSS].append(
            fit[LOSS][SIG_STEEP])
        self[SIG_MID_RISK_LOSS].append(
            fit[LOSS][SIG_MID])


def create(info_data, control_data,
           cpt_fit, control_sig_fit,
           risk_sig_fit):

    summary = Summary()
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
