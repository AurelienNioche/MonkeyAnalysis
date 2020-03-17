import os
from datetime import datetime
import warnings

import numpy as np
import pandas as pd
import pytz
import xlsxwriter

from experimental_data.models import ExperimentalData
from stimuli.models import Stimuli

from parameters.parameters import DATA_FOLDER, XLS_NAME, DATE_FORMAT


def export_as_xlsx():

    col = [f.name for f in ExperimentalData._meta.get_fields()]
    os.makedirs(DATA_FOLDER, exist_ok=True)

    workbook = xlsxwriter.Workbook(os.path.join(DATA_FOLDER,
                                                XLS_NAME),
                                   {'remove_timezone': True})
    worksheet = workbook.add_worksheet()

    # Write title
    for j, c in enumerate(col):
        worksheet.write(0, j, c)

    data = ExperimentalData.objects.values_list(*col)

    for i, d in enumerate(data):
        for j in range(len(col)):

            if j == col.index('date'):
                entry = d[j].strftime(DATE_FORMAT)

            else:
                entry = d[j]

            worksheet.write(i + 1, j, entry)

    workbook.close()


def import_data_xlsx(data_file='data.xlsx'):

    ExperimentalData.objects.all().delete()

    print("Reading from xlsx...", end=" ", flush=True)
    df = pd.read_excel(os.path.join(DATA_FOLDER, data_file), )
    print("Done!")

    print("Preprocess the data...", end=" ", flush=True)
    entries = df.to_dict('records')

    filtered_entries = []

    for i, entry_dic in enumerate(entries):
        # if 'nan' in entry_dic.values():
        #     raise ValueError
        error = False
        for k, v in entry_dic.items():
            if str(v) == '':
                error = True
            elif type(v) in (float, int) and np.isnan(v):
                error = True

            if error:
                msg = f"I will ignore line {i+1} / id={entry_dic['id']} (missing data or wrong format for column '{k}')"
                warnings.warn(msg)
                break
        if error is False:
            date_string = entry_dic['date']
            date_string = date_string.replace('None', '')
            entry_dic['date'] = \
                datetime.strptime(date_string, DATE_FORMAT) \
                .astimezone(pytz.UTC)
            filtered_entries.append(entry_dic)
    print("Done!")
    print("Writing in db...", end=" ", flush=True)
    ExperimentalData.objects.bulk_create(
        ExperimentalData(**val) for val in filtered_entries)

    print("Done!")


def import_stimuli_xlsx(data_file='stimuli.xlsx'):

    Stimuli.objects.all().delete()

    print("Reading from xlsx...", end=" ", flush=True)
    df = pd.read_excel(os.path.join(DATA_FOLDER, data_file), )
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


# def get_table_class(table_name):
#     a = "".join([i.capitalize() for i in table_name.split("_")])
#     return eval(a)
#
#
# def convert_choice(choice):
#
#     if choice == 'None':
#         return -1
#     elif choice == "left":
#         return 0
#     elif choice == "right":
#         return 1
#     else:
#         raise ValueError
#
#
# def import_from_old_db():
#
#     print("Preparing the new entries...")
#
#     ExperimentalData.objects.all().delete()
#
#     summary_entries = Summary.objects.all().order_by("date", "monkey")
#
#     new_entries = []
#
#     for sm in tqdm(summary_entries):
#         if sm.fake == "False":
#
#             session = get_table_class(sm.session_table)
#
#             for trial in session.objects.all().order_by("id"):
#                 fixation_time = eval(sm.fixation_time)
#                 inter_trial_time = eval(sm.inter_trial_time)
#                 date = \
#                     datetime.strptime(sm.date, DATE_FORMAT)\
#                     .astimezone(pytz.UTC)
#                 choice = convert_choice(trial.choice)
#                 initial_stock = sm.initial_stock
#
#                 if hasattr(trial, "time_to_decide"):
#                     time_reaction = -1000
#                     time_movement = -1000
#                     time_response = trial.time_to_decide
#                     time_back_movement = trial.time_to_come_back_to_the_grip
#                     time_fixation = trial.fixation_time
#                     time_inter_trial = trial.inter_trial_time
#                 else:
#                     time_movement = trial.time_movement
#                     time_reaction = trial.time_reaction
#                     time_response = time_reaction + time_movement
#                     time_back_movement = trial.time_back_movement
#                     time_fixation = trial.time_fixation
#                     time_inter_trial = trial.time_inter_trial
#
#                 if not 0 < time_response < 2**63-1:
#                     time_response = -1000
#
#                 if not 0 < time_back_movement < 2**63-1:
#                     time_back_movement = -1000
#
#                 new_entries.append(ExperimentalData(
#                     monkey=sm.monkey,
#                     date=date,
#                     param_time_fixation_min=fixation_time[0],
#                     param_time_fixation_max=fixation_time[1],
#                     param_initial_stock=initial_stock,
#                     param_time_inter_trial_min=inter_trial_time[0],
#                     param_time_inter_trial_max=inter_trial_time[1],
#                     param_time_response_max=sm.max_decision_time,
#                     param_time_back_movement_max=sm.max_return_time,
#                     param_time_punishment=sm.punishment_time,
#                     param_time_result_display=sm.result_display_time,
#                     param_time_reward=sm.reward_time,
#                     param_time_valve_opening=sm.valve_opening_time,
#                     param_proportion_control=sm.control_trials_proportion,
#                     param_proportion_incongruent=sm.incongruent_proportion,
#                     param_proportion_with_losses=sm.with_losses_proportion,
#                     choice=choice,
#                     error=trial.error,
#                     stim_dice_output=trial.dice_output,
#                     stim_left_beginning_angle=trial.left_beginning_angle,
#                     stim_left_p=float(trial.left_p),
#                     stim_left_x0=int(trial.left_x0),
#                     stim_right_beginning_angle=int(trial.right_beginning_angle),
#                     stim_right_p=float(trial.right_p),
#                     stim_right_x0=int(trial.right_x0),
#                     time_response=time_response,
#                     time_reaction=time_reaction,
#                     time_movement=time_movement,
#                     time_back_movement=time_back_movement,
#                     time_fixation=time_fixation,
#                     time_inter_trial=time_inter_trial))
#
#     print("Creating new entries... It can take a while...")
#     ExperimentalData.objects.bulk_create(new_entries)
#     print("Done!")
