from django.db import models


class ExperimentalData(models.Model):

    monkey = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    param_time_fixation_min = models.IntegerField(default=-1000)
    param_time_fixation_max = models.IntegerField(default=-1000)
    param_initial_stock = models.IntegerField(default=-1000)
    param_time_inter_trial_min = models.IntegerField(default=-1000)
    param_time_inter_trial_max = models.IntegerField(default=-1000)
    param_time_response_max = models.IntegerField(default=-1000)
    param_time_back_movement_max = models.IntegerField(default=-1000)
    param_time_punishment = models.IntegerField(default=-1000)
    param_time_result_display = models.IntegerField(default=-1000)
    param_time_reward = models.IntegerField(default=-1000)
    param_time_valve_opening = models.IntegerField(default=-1000)
    param_proportion_control = models.IntegerField(default=-1000)
    param_proportion_incongruent = models.IntegerField(default=-1000)
    param_proportion_with_losses = models.IntegerField(default=-1000)

    choice = models.IntegerField(default=-1000)
    error = models.TextField(blank=True, null=True)
    stim_dice_output = models.IntegerField(default=-1000)
    stim_left_beginning_angle = models.IntegerField(default=-1000)
    stim_left_p = models.FloatField(default=-1000)
    stim_left_x0 = models.IntegerField(default=-1000)
    stim_right_beginning_angle = models.IntegerField(default=-1000)
    stim_right_p = models.FloatField(default=-1000)
    stim_right_x0 = models.IntegerField(default=-1000)
    time_back_movement = models.IntegerField(default=-1000)
    time_response = models.IntegerField(default=-1000)
    time_movement = models.IntegerField(default=-1000)
    time_reaction = models.IntegerField(default=-1000)
    time_fixation = models.IntegerField(default=-1000)
    time_inter_trial = models.IntegerField(default=-1000)

    class Meta:
        db_table = 'experimental_data'
