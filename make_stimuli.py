import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "MonkeyAnalysis.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import itertools as it

import numpy as np
import xlsxwriter

from stimuli.import_export import import_stimuli_xlsx


class StimuliGenerator:

    XLS_NAME = "stimuli.xlsx"
    XLS_FOLDER = "data"

    GAUGE_MAX = 6
    X_MAX = 3

    P = [0.25, 0.5, 0.75, 1]
    X_POS = np.arange(1, 4)
    X_NEG = np.arange(-3, 0)

    SIDES = ["left", "right"]

    def __init__(self):

        self.workbook, self.worksheet = self._create_xls()
        self.xls_row = 0

    @classmethod
    def _create_xls(cls):

        # Create a workbook and add a worksheet.
        os.makedirs(cls.XLS_FOLDER, exist_ok=True)
        workbook = xlsxwriter.Workbook(os.path.join(cls.XLS_FOLDER,
                                                    cls.XLS_NAME))
        worksheet = workbook.add_worksheet()

        return workbook, worksheet

    def _write(self, left_p, right_p, left_x, right_x, lottery_type,
               comment):

        col_value = [
            ('left_p', left_p),
            ('left_x0', left_x),
            ('right_p', right_p),
            ('right_x0', right_x),
            ('lottery_type', lottery_type),
            ('comment', comment),
        ]

        col = [i[0] for i in col_value]

        if self.xls_row == 0:
            for col_idx, title in enumerate(col):
                self.worksheet.write(0, col_idx, title)

            self.xls_row += 1

        for i, (k, v) in enumerate(col_value):
            self.worksheet.write(self.xls_row, i, v)

        print(f"[{self.xls_row}] p0 = ({left_p}, {right_p}); "
              f"x0 = ({left_x}, {right_x}), type={lottery_type}")
        self.xls_row += 1

    def _type_01(self):

        comment = "CONTROL; p fixed / x varies, x0 negative vs positive"
        print(comment)

        x0 = list(it.product(self.X_NEG, self.X_POS))

        for i, j in list(it.product(self.P, x0)):
            self._write(left_p=i, right_p=i, left_x=j[0], right_x=j[1],
                        lottery_type=1, comment=comment)

    def _type_02(self):

        comment = "CONTROL; p fixed / x varies; x0 positive"
        print(comment)

        x0 = list(it.combinations(self.X_POS, 2))

        for i, j in list(it.product(self.P, x0)):
            self._write(left_p=i, right_p=i, left_x=j[0], right_x=j[1],
                        lottery_type=2,
                        comment=comment)

    def _type_03(self):

        comment = "CONTROL; p fixed / x varies; x0 negative"
        print(comment)

        x0 = list(it.combinations(self.X_NEG, 2))

        for i, j in list(it.product(self.P, x0)):
            self._write(left_p=i, right_p=i, left_x=j[0], right_x=j[1],
                        lottery_type=3, comment=comment)

    def _type_04(self):

        comment = "CONTROL; p varies / x fixed; x0 positive"
        print(comment)

        p = list(it.combinations(self.P, 2))

        for i, j in list(it.product(p, self.X_POS)):
            self._write(left_p=i[0], right_p=i[1], left_x=j, right_x=j,
                        lottery_type=4, comment=comment)

    def _type_05(self):

        comment = "CONTROL; p varies / x fixed; x0 negative"
        print(comment)

        p = list(it.combinations(self.P, 2))

        for i, j in list(it.product(p, self.X_NEG)):
            self._write(left_p=i[0], right_p=i[1], left_x=j, right_x=j,
                        lottery_type=5, comment=comment)

    def _type_06(self):

        comment = "INCONGRUENT POS; p varies / x varies; x0 positive"
        print(comment)

        x0 = list(it.combinations(self.X_POS[::-1], 2))
        p = list(it.combinations(self.P, 2))

        for i, j in list(it.product(p, x0)):
            self._write(left_p=i[0], right_p=i[1], left_x=j[0], right_x=j[1],
                        lottery_type=6, comment=comment)

    def _type_07(self):

        comment = "INCONGRUENT NEG; p varies / x varies; x0 negative"
        print(comment)

        x0 = list(it.combinations(self.X_NEG, 2))
        p = list(it.combinations(self.P, 2))

        for i, j in list(it.product(p, x0)):
            self._write(left_p=i[0], right_p=i[1], left_x=j[0], right_x=j[1],
                        lottery_type=7, comment=comment)

    def _type_08(self):

        comment = "CONGRUENT POS; p varies / x varies; x0 positive."
        print(comment)

        x0 = list(it.combinations(self.X_POS, 2))
        p = list(it.combinations(self.P, 2))

        for i, j in list(it.product(p, x0)):
            self._write(left_p=i[0], right_p=i[1], left_x=j[0], right_x=j[1],
                        lottery_type=8, comment=comment)

    def _type_09(self):

        comment = "CONGRUENT NEG; p varies / x varies; x0 negative"
        print(comment)

        x0 = list(it.combinations(self.X_NEG[::-1], 2))
        p = list(it.combinations(self.P, 2))

        for i, j in list(it.product(p, x0)):
            self._write(left_p=i[0], right_p=i[1], left_x=j[0], right_x=j[1],
                        lottery_type=9, comment=comment)

    def _type_10(self):

        comment = "CONTROL; p varies / x varies, x0 negative vs positive"
        print(comment)

        x0 = list(it.product(self.X_NEG, self.X_POS))
        p = list(it.permutations(self.P, 2))

        for i, j in list(it.product(p, x0)):
            self._write(left_p=i[0], right_p=i[1], left_x=j[0], right_x=j[1],
                        lottery_type=10, comment=comment)

    def _type_11(self):

        comment = "CONTROL; p varies or is 1 / x varies, x0 negative vs 0"
        print(comment)

        x0 = self.X_NEG
        p = self.P

        for i, j in list(it.product(p, x0)):
            self._write(left_p=i, right_p=1, left_x=j, right_x=0,
                        lottery_type=11, comment=comment)

    def _type_12(self):

        comment = "CONTROL; p varies or is 1 / x varies, x0 positive vs 0"
        print(comment)

        x0 = self.X_POS
        p = self.P

        for i, j in list(it.product(p, x0)):
            self._write(left_p=i, right_p=1, left_x=j, right_x=0,
                        lottery_type=12, comment=comment)

    def make_xlsx(self):

        attr_list = sorted(dir(self))
        for attr in attr_list:
            if attr.startswith('_type_'):
                getattr(self, attr)()

        self.workbook.close()


def main():

    sf = StimuliGenerator()
    sf.make_xlsx()

    import_stimuli_xlsx()


if __name__ == "__main__":
    main()
