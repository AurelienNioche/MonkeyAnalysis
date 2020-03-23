import os
import xlsxwriter

from parameters.parameters import DATA_FOLDER

from parameters.parameters import FIG_FOLDER, MODEL_PARAMETERS, \
    CONTROL_CONDITIONS, CHOOSE_RIGHT, MONKEY_NAME


class Summary:

    def __init__(self):

        self.columns = self._get_columns()

        self.summary = {k: [] for k in self.columns}

    @staticmethod
    def _get_columns():

        col = [MONKEY_NAME, CHOOSE_RIGHT]
        for cd in CONTROL_CONDITIONS:
            col.append(cd)

        for pr in MODEL_PARAMETERS:
            col.append(pr)

        return col

    def __getitem__(self, item):
        return self.summary[item]

    def __setitem__(self, key, value):
        self.summary[key] = value


def create():

    return Summary()


def export_as_xlsx(summary, xls_name="summary.xlsx"):

    col = summary.columns
    os.makedirs(DATA_FOLDER, exist_ok=True)

    workbook = xlsxwriter.Workbook(os.path.join(DATA_FOLDER,
                                                xls_name))
    worksheet = workbook.add_worksheet()

    # Write title
    for j, c in enumerate(col):
        worksheet.write(0, j, c)

    for j, col_name in enumerate(col):

        data_col = summary[col_name]
        for i, d in enumerate(data_col):

            worksheet.write(i + 1, j, d)

    workbook.close()
