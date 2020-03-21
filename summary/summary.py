import os
from datetime import datetime
import warnings

import numpy as np
import pandas as pd
import pytz
import xlsxwriter

from stimuli.models import Stimuli

from parameters.parameters import DATA_FOLDER


def export_as_xlsx(summary, xls_name="summary.xlsx"):

    col = sorted(summary.keys())
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
