import os
import pandas as pd

from . models import Stimuli

from parameters.parameters import EXPORT_FOLDER


def import_stimuli_xlsx(data_file='stimuli.xlsx'):

    Stimuli.objects.all().delete()

    print("Reading from xlsx...", end=" ", flush=True)
    df = pd.read_excel(os.path.join(EXPORT_FOLDER, data_file), )
    print("Done!")

    print("Writing in db...", end=" ", flush=True)
    xl_rows = df.to_dict('records')

    entries = []

    for i, row_dic in enumerate(xl_rows):

        entries.append(
            Stimuli(
                id=i+1,
                left_p=row_dic["left_p"],
                right_p=row_dic["right_p"],
                left_x0=row_dic["left_x0"],
                right_x0=row_dic["right_x0"],
                lottery_type=row_dic["lottery_type"],
                control="CONTROL" in row_dic["comment"],
                congruent="CONGRUENT" in row_dic["comment"],
                incongruent="INCONGRUENT" in row_dic["comment"],
                description=row_dic["comment"]
            )
        )

    Stimuli.objects.bulk_create(entries)

    print("Done!")
