import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "MonkeyAnalysis.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from datetime import datetime
from experimental_data.models import *


def get_table_class(table_name):
    a = "".join([i.capitalize() for i in table_name.split("_")])
    return eval(a)


def convert_choice(choice):

    if choice == 'None':
        return -1
    elif choice == "left":
        return 0
    elif choice == "right":
        return 1
    else:
        raise ValueError


def main():

    summary_entries = Summary.objects.all()

    for sm in summary_entries:
        if not sm.fake:
            session = get_table_class(sm.session_table)

            for trial in session.objects.all():
                fixation_time = eval(sm.fixation_time)
                inter_trial_time = eval(sm.inter_trial_time)
                choice = convert_choice(trial.choice)
                ExperimentalData.objects.create(
                    monkey=sm.monkey,
                    date=datetime.strptime(trial.date, '%Y-%m-%d'),
                    fixation_time_min=fixation_time[0],
                    fixation_time_max=fixation_time[1],
                    initial_stock=session.initial_stock,
                    inter_trial_time_min=inter_trial_time[0],
                    inter_trial_time_max=inter_trial_time[1],
                    max_decision_time=sm.max_decision_time,
                    max_return_time=sm.max_return_time,
                    punishment_time=sm.punishment_time,
                    result_display_time=sm.result_display_time,
                    reward_time=sm.reward_time,
                    valve_opening_time=sm.valve_opening_time,
                    control_proportion=sm.control_trial_proportion,
                    incongruent_proportion=sm.incongruent_proportion,
                    with_losses_proportion=sm.with_losses_proportion,
                    choice=choice,
                    dice_output=trial.dice_output,
                    error=trial.error,
                    fixation_time=trial.fixation_time,
                    inter_trial_time=trial.inter_trial_time,
                    left_beginning_angle=trial.left_beginning_angle,
                    left_p=int(trial.left_p),
                    left_x0=int(trial.left_x0),
                    right_beginning_angle=int(trial.right_beginning_angle),
                    right_p=int(trial.right_p),
                    right_x0=int(trial.right_x0),
                    time_to_come_back_to_the_grip=
                    trial.time_to_come_back_to_the_grip,
                    time_to_decide=trial.time_to_decide)


if __name__ == "__main__":

    main()
