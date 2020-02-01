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


def main():

    summary_entries = Summary.objects.all()

    for sm in summary_entries:
        if not sm.fake:
            session = get_table_class(sm.session_table)

            for trial in session.objects.all():

                new_trial = ExperimentalData(

                    monkey=sm.monkey,
                    date = datetime.strptime(string_time, '%Y-%m-%d %H:%M:%S.%f'),
                fixation_time_min = models.IntegerField(blank=True, null=True)
                fixation_time_max = models.IntegerField(blank=True, null=True)
                initial_stock = models.IntegerField(blank=True, null=True)
                inter_trial_time_min = models.IntegerField(blank=True,
                                                           null=True)
                inter_trial_time_max = models.IntegerField(blank=True,
                                                           null=True)
                max_decision_time = models.IntegerField(blank=True, null=True)
                max_return_time = models.IntegerField(blank=True, null=True)
                punishment_time = models.IntegerField(blank=True, null=True)
                result_display_time = models.IntegerField(blank=True,
                                                          null=True)
                reward_time = models.IntegerField(blank=True, null=True)
                trials_per_block = models.IntegerField(blank=True, null=True)
                valve_opening_time = models.IntegerField(blank=True, null=True)
                control_trials_proportion = models.IntegerField(blank=True,
                                                                null=True)
                incongruent_proportion = models.IntegerField(blank=True,
                                                             null=True)
                with_losses_proportion = models.IntegerField(blank=True,
                                                             null=True)

                choice = models.IntegerField(blank=True, null=True)
                dice_output = models.IntegerField(blank=True, null=True)
                error = models.TextField(blank=True, null=True)
                fixation_time = models.IntegerField(blank=True, null=True)
                gauge_level = models.IntegerField(blank=True, null=True)
                inter_trial_time = models.IntegerField(blank=True, null=True)
                left_beginning_angle = models.IntegerField(blank=True,
                                                           null=True)
                left_p = models.IntegerField(blank=True, null=True)
                left_x0 = models.IntegerField(blank=True, null=True)
                left_x1 = models.IntegerField(blank=True, null=True)
                n_block = models.IntegerField(blank=True, null=True)
                n_trial_inside_block = models.IntegerField(blank=True,
                                                           null=True)
                right_beginning_angle = models.IntegerField(blank=True,
                                                            null=True)
                right_p = models.IntegerField(blank=True, null=True)
                right_x0 = models.IntegerField(blank=True, null=True)
                right_x1 = models.IntegerField(blank=True, null=True)
                time_to_come_back_to_the_grip = models.IntegerField(blank=True,
                                                                    null=True)
                time_to_decide = models.IntegerField(blank=True, null=True)

                )




if __name__ == "__main__":

    main()
