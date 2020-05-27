import os
import xlsxwriter
import numpy as np

from parameters.parameters import EXPORT_FOLDER, \
    CONTROL_CONDITIONS, SIG_STEEP, \
    SIG_MID

from . doc import DOC


class Summary:

    XLS_NAME = "summary.xlsx"
    MONKEY_NAME = "monkey"

    def __init__(self, class_model):

        self.class_model = class_model

        self.content = {}

    def __getitem__(self, item):
        try:
            return self.content[item]
        except KeyError:
            self.content[item] = []
            return self.content[item]

    def __setitem__(self, key, value):
        self.content[key] = value

    def export_as_xlsx(self):

        xls_path = os.path.join(EXPORT_FOLDER, self.XLS_NAME)
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
        for j, c in enumerate(DOC.keys()):
            c_name = self._format_column_name(c)
            worksheet.write(j, 0, c_name)
            worksheet.write(j, 1, DOC[c])

        workbook.close()

        print(f"Summary exported in the file '{xls_path}'\n")

    @staticmethod
    def _format_column_name(c):
        return c.replace(" ", "_").replace("-", "")

    def append_performance_to_control(self, control_d):

        for cd in CONTROL_CONDITIONS:
            median = np.median(control_d[cd])
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
        summary[Summary.MONKEY_NAME].append(m)

        # Add median for each type of control
        summary.append_performance_to_control(control_data[m])

        # Add best-fit parameters
        summary.append_cpt_fit(cpt_fit[m])
        summary.append_control_sig_fit(control_sig_fit[m])
        summary.append_risk_sig_fit(risk_sig_fit[m])

    summary.export_as_xlsx()
