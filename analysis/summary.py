import os
import xlsxwriter

from parameters.parameters import DATA_FOLDER

from parameters.parameters import MODEL_PARAMETERS, \
    CONTROL_CONDITIONS, CHOOSE_RIGHT, MONKEY_NAME, N_TRIALS, DOC


class Summary:

    def __init__(self):

        self.columns = self._get_columns()

        self.summary = {k: [] for k in self.columns}

    @staticmethod
    def _get_columns():

        col = [MONKEY_NAME, N_TRIALS, CHOOSE_RIGHT]
        for cd in CONTROL_CONDITIONS:
            col.append(cd)

        for pr in MODEL_PARAMETERS:
            col.append(pr)

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


def create():
    return Summary()
