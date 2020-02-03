from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ExperimentalData(models.Model):

    monkey = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    param_time_fixation_min = models.IntegerField(blank=True, null=True)
    param_time_fixation_max = models.IntegerField(blank=True, null=True)
    param_initial_stock = models.IntegerField(blank=True, null=True)
    param_time_inter_trial_min = models.IntegerField(blank=True, null=True)
    param_time_inter_trial_max = models.IntegerField(blank=True, null=True)
    param_time_response_max = models.IntegerField(blank=True, null=True)
    param_time_back_movement_max = models.IntegerField(blank=True, null=True)
    param_time_punishment = models.IntegerField(blank=True, null=True)
    param_time_result_display = models.IntegerField(blank=True, null=True)
    param_time_reward = models.IntegerField(blank=True, null=True)
    param_time_valve_opening = models.IntegerField(blank=True, null=True)
    param_proportion_control = models.IntegerField(blank=True, null=True)
    param_proportion_incongruent = models.IntegerField(blank=True, null=True)
    param_proportion_with_losses = models.IntegerField(blank=True, null=True)

    choice = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    stim_dice_output = models.IntegerField(blank=True, null=True)
    stim_left_beginning_angle = models.IntegerField(blank=True, null=True)
    stim_left_p = models.FloatField(blank=True, null=True)
    stim_left_x0 = models.IntegerField(blank=True, null=True)
    stim_right_beginning_angle = models.IntegerField(blank=True, null=True)
    stim_right_p = models.FloatField(blank=True, null=True)
    stim_right_x0 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_response = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(default=-1000)
    time_reaction = models.IntegerField(default=-1000)
    time_fixation = models.IntegerField(default=-1000)
    time_inter_trial = models.IntegerField(default=-1000)

    class Meta:
        db_table = 'experimental_data'


class Session20161201Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_01_Gladys'


class Session20161201Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_01_Havane'


class Session20161202Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_02_Gladys'


class Session20161202Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_02_Havane'


class Session20161205Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_05_Gladys'


class Session20161205Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_05_Havane'


class Session20161206Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_06_Gladys'


class Session20161206Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_06_Havane'


class Session20161207Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_07_Gladys'


class Session20161207Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_07_Havane'


class Session20161208Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_08_Gladys'


class Session20161208Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_08_Havane'


class Session20161209Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_09_Gladys'


class Session20161209Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_09_Havane'


class Session20161212Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_12_Gladys'


class Session20161212Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_12_Havane'


class Session20161213Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_13_Gladys'


class Session20161213Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_13_Havane'


class Session20161214Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_14_Gladys'


class Session20161214Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_14_Havane'


class Session20161215Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_15_Gladys'


class Session20161215Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_15_Havane'


class Session20161216Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_16_Gladys'


class Session20161216Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2016_12_16_Havane'


class Session20170105Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_05_Gladys'


class Session20170105Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_05_Havane'


class Session20170106Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_06_Gladys'


class Session20170106Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_06_Havane'


class Session20170109Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_09_Gladys'


class Session20170109Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_09_Havane'


class Session20170110Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_10_Gladys'


class Session20170110Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_10_Havane'


class Session20170111Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_11_Gladys'


class Session20170111Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_11_Havane'


class Session20170112Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_12_Gladys'


class Session20170112Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_12_Havane'


class Session20170113Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_13_Gladys'


class Session20170113Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_13_Havane'


class Session20170116Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_16_Gladys'


class Session20170116Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_16_Havane'


class Session20170117Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_17_Gladys'


class Session20170117Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_17_Havane'


class Session20170118Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_18_Gladys'


class Session20170118Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_18_Havane'


class Session20170119Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_19_Gladys'


class Session20170119Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_19_Havane'


class Session20170123Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_23_Gladys'


class Session20170124Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_24_Gladys'


class Session20170124Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_24_Havane'


class Session20170125Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_25_Gladys'


class Session20170125Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_25_Havane'


class Session20170126Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_26_Gladys'


class Session20170126Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_26_Havane'


class Session20170127Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_27_Gladys'


class Session20170127Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_27_Havane'


class Session20170130Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_30_Gladys'


class Session20170130Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_30_Havane'


class Session20170131Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_31_Gladys'


class Session20170131Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_01_31_Havane'


class Session20170201Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_01_Gladys'


class Session20170201Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_01_Havane'


class Session20170202Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_02_Gladys'


class Session20170202Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_02_Havane'


class Session20170203Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_03_Gladys'


class Session20170203Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_03_Havane'


class Session20170206Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_06_Gladys'


class Session20170206Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_06_Havane'


class Session20170207Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_07_Gladys'


class Session20170207Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_07_Havane'


class Session20170208Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_08_Gladys'


class Session20170208Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_08_Havane'


class Session20170209Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_09_Gladys'


class Session20170209Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_09_Havane'


class Session20170210Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_10_Gladys'


class Session20170210Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_10_Havane'


class Session20170213Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_13_Gladys'


class Session20170213Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_13_Havane'


class Session20170214Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_14_Gladys'


class Session20170214Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_14_Havane'


class Session20170215Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_15_Gladys'


class Session20170215Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_15_Havane'


class Session20170220Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_20_Gladys'


class Session20170220Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_20_Havane'


class Session20170221Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_21_Gladys'


class Session20170221Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_21_Havane'


class Session20170222Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_22_Gladys'


class Session20170222Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_22_Havane'


class Session20170223Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_23_Gladys'


class Session20170223Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_23_Havane'


class Session20170224Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_24_Gladys'


class Session20170224Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_24_Havane'


class Session20170227Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_27_Gladys'


class Session20170227Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_27_Havane'


class Session20170228Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_28_Gladys'


class Session20170228Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_02_28_Havane'


class Session20170301Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_01_Gladys'


class Session20170301Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_01_Havane'


class Session20170302Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_02_Gladys'


class Session20170302Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_02_Havane'


class Session20170303Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_03_Gladys'


class Session20170303Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_03_Havane'


class Session20170306Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_06_Gladys'


class Session20170306Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_06_Havane'


class Session20170307Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_07_Gladys'


class Session20170307Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_07_Havane'


class Session20170308Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_08_Gladys'


class Session20170308Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_08_Havane'


class Session20170309Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_09_Gladys'


class Session20170309Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_09_Havane'


class Session20170310Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_10_Gladys'


class Session20170310Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_10_Havane'


class Session20170313Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_13_Gladys'


class Session20170313Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_13_Havane'


class Session20170314Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_14_Gladys'


class Session20170314Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_14_Havane'


class Session20170315Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_15_Gladys'


class Session20170315Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_15_Havane'


class Session20170316Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_16_Gladys'


class Session20170316Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_16_Havane'


class Session20170317Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_17_Gladys'


class Session20170317Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_17_Havane'


class Session20170320Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_20_Gladys'


class Session20170320Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_20_Havane'


class Session20170321Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_21_Gladys'


class Session20170321Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_21_Havane'


class Session20170322Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_22_Gladys'


class Session20170322Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_22_Havane'


class Session20170323Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_23_Gladys'


class Session20170323Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_23_Havane'


class Session20170324Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_24_Gladys'


class Session20170324Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_24_Havane'


class Session20170327Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_27_Gladys'


class Session20170327Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_27_Havane'


class Session20170328Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_28_Gladys'


class Session20170328Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_28_Havane'


class Session20170329Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_29_Gladys'


class Session20170329Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_29_Havane'


class Session20170330Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_30_Gladys'


class Session20170330Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_30_Havane'


class Session20170331Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_31_Gladys'


class Session20170331Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_03_31_Havane'


class Session20170403Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_03_Gladys'


class Session20170403Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_03_Havane'


class Session20170404Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_04_Gladys'


class Session20170404Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_04_Havane'


class Session20170405Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_05_Gladys'


class Session20170405Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_05_Havane'


class Session20170406Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_06_Gladys'


class Session20170406Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_06_Havane'


class Session20170407Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_07_Gladys'


class Session20170407Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_07_Havane'


class Session20170410Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_10_Gladys'


class Session20170410Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_10_Havane'


class Session20170411Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_11_Gladys'


class Session20170411Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_11_Havane'


class Session20170412Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_12_Gladys'


class Session20170412Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_12_Havane'


class Session20170414Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_14_Gladys'


class Session20170414Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_14_Havane'


class Session20170418Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_18_Gladys'


class Session20170418Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_18_Havane'


class Session20170419Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_19_Gladys'


class Session20170419Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_19_Havane'


class Session20170420Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_20_Gladys'


class Session20170420Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_20_Havane'


class Session20170421Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_21_Gladys'


class Session20170424Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_24_Gladys'


class Session20170425Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_25_Gladys'


class Session20170425Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_25_Havane'


class Session20170426Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_26_Gladys'


class Session20170426Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_26_Havane'


class Session20170427Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_27_Gladys'


class Session20170427Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_27_Havane'


class Session20170428Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_28_Gladys'


class Session20170428Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_04_28_Havane'


class Session20170502Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_02_Gladys'


class Session20170502Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_02_Havane'


class Session20170503Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_03_Gladys'


class Session20170503Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_03_Havane'


class Session20170504Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_04_Gladys'


class Session20170504Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_04_Havane'


class Session20170505Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_05_Gladys'


class Session20170505Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_05_Havane'


class Session20170508Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_08_Gladys'


class Session20170508Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_08_Havane'


class Session20170509Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_09_Gladys'


class Session20170509Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_09_Havane'


class Session20170510Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_10_Gladys'


class Session20170510Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_10_Havane'


class Session20170511Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_11_Gladys'


class Session20170511Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_11_Havane'


class Session20170512Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_12_Gladys'


class Session20170512Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_12_Havane'


class Session20170522Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_22_Gladys'


class Session20170522Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_22_Havane'


class Session20170523Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_23_Gladys'


class Session20170523Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_23_Havane'


class Session20170524Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_24_Gladys'


class Session20170524Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_24_Havane'


class Session20170529Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_29_Gladys'


class Session20170529Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_29_Havane'


class Session20170530Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_30_Gladys'


class Session20170530Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_30_Havane'


class Session20170531Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_31_Gladys'


class Session20170531Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_05_31_Havane'


class Session20170601Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_01_Gladys'


class Session20170601Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_01_Havane'


class Session20170602Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_02_Gladys'


class Session20170602Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_02_Havane'


class Session20170606Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_06_Gladys'


class Session20170606Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_06_Havane'


class Session20170607Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_07_Gladys'


class Session20170607Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_07_Havane'


class Session20170608Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_08_Gladys'


class Session20170608Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_08_Havane'


class Session20170609Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_09_Gladys'


class Session20170609Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_09_Havane'


class Session20170612Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_12_Gladys'


class Session20170612Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_12_Havane'


class Session20170613Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_13_Gladys'


class Session20170613Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_13_Havane'


class Session20170614Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_14_Gladys'


class Session20170614Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_14_Havane'


class Session20170615Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_15_Gladys'


class Session20170615Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_15_Havane'


class Session20170616Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_16_Gladys'


class Session20170616Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_16_Havane'


class Session20170619Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_19_Gladys'


class Session20170619Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_19_Havane'


class Session20170620Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_20_Gladys'


class Session20170620Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_20_Havane'


class Session20170621Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_21_Gladys'


class Session20170621Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_21_Havane'


class Session20170622Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_22_Gladys'


class Session20170622Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_22_Havane'


class Session20170623Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_23_Gladys'


class Session20170623Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_23_Havane'


class Session20170626Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_26_Gladys'


class Session20170626Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_26_Havane'


class Session20170627Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_27_Gladys'


class Session20170627Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_27_Havane'


class Session20170628Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_28_Gladys'


class Session20170628Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_28_Havane'


class Session20170629Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_29_Gladys'


class Session20170629Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_29_Havane'


class Session20170630Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_30_Gladys'


class Session20170630Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_06_30_Havane'


class Session20170703Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_03_Gladys'


class Session20170703Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_03_Havane'


class Session20170704Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_04_Gladys'


class Session20170704Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_04_Havane'


class Session20170705Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_05_Gladys'


class Session20170705Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_05_Havane'


class Session20170706Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_06_Gladys'


class Session20170706Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_06_Havane'


class Session20170707Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_07_Gladys'


class Session20170707Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_07_Havane'


class Session20170710Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_10_Gladys'


class Session20170710Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_10_Havane'


class Session20170711Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_11_Gladys'


class Session20170711Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_11_Havane'


class Session20170712Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_12_Gladys'


class Session20170712Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_12_Havane'


class Session20170713Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_13_Gladys'


class Session20170713Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_13_Havane'


class Session20170718Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_18_Gladys'


class Session20170718Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_18_Havane'


class Session20170719Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_19_Gladys'


class Session20170719Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_19_Havane'


class Session20170720Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_20_Gladys'


class Session20170720Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_20_Havane'


class Session20170721Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_21_Gladys'


class Session20170721Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_21_Havane'


class Session20170724Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_24_Gladys'


class Session20170724Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_24_Havane'


class Session20170725Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_25_Gladys'


class Session20170725Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_25_Havane'


class Session20170726Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_26_Gladys'


class Session20170726Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_26_Havane'


class Session20170727Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_27_Gladys'


class Session20170727Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_27_Havane'


class Session20170728Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_28_Gladys'


class Session20170728Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_07_28_Havane'


class Session20170828Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_08_28_Gladys'


class Session20170828Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_08_28_Havane'


class Session20170829Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_08_29_Gladys'


class Session20170829Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_08_29_Havane'


class Session20170830Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_08_30_Gladys'


class Session20170830Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_08_30_Havane'


class Session20170831Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_08_31_Gladys'


class Session20170831Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_08_31_Havane'


class Session20170901Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_01_Gladys'


class Session20170901Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_01_Havane'


class Session20170904Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_04_Gladys'


class Session20170904Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_04_Havane'


class Session20170905Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_05_Gladys'


class Session20170905Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_05_Havane'


class Session20170906Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_06_Gladys'


class Session20170906Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_06_Havane'


class Session20170907Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_07_Gladys'


class Session20170907Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_07_Havane'


class Session20170908Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_08_Gladys'


class Session20170908Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_08_Havane'


class Session20170911Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_11_Gladys'


class Session20170911Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_11_Havane'


class Session20170912Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_12_Gladys'


class Session20170912Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_12_Havane'


class Session20170913Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_13_Gladys'


class Session20170913Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_13_Havane'


class Session20170915Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_15_Gladys'


class Session20170915Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_15_Havane'


class Session20170918Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_18_Gladys'


class Session20170918Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_18_Havane'


class Session20170919Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_19_Gladys'


class Session20170919Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_19_Havane'


class Session20170920Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_20_Gladys'


class Session20170920Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_20_Havane'


class Session20170921Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_21_Gladys'


class Session20170921Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_21_Havane'


class Session20170922Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_22_Gladys'


class Session20170922Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_22_Havane'


class Session20170925Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_25_Gladys'


class Session20170925Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_25_Havane'


class Session20170926Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_26_Gladys'


class Session20170926Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_26_Havane'


class Session20170927Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_27_Gladys'


class Session20170927Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_27_Havane'


class Session20170928Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_28_Gladys'


class Session20170928Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_28_Havane'


class Session20170929Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_29_Gladys'


class Session20170929Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_09_29_Havane'


class Session20171127Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_11_27_Gladys'


class Session20171127Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_11_27_Havane'


class Session20171128Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_11_28_Gladys'


class Session20171128Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_11_28_Havane'


class Session20171129Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_11_29_Gladys'


class Session20171129Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_11_29_Havane'


class Session20171130Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_11_30_Gladys'


class Session20171130Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_11_30_Havane'


class Session20171201Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_12_01_Gladys'


class Session20171201Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_12_01_Havane'


class Session20171218Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_12_18_Gladys'


class Session20171218Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_12_18_Havane'


class Session20171219Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_12_19_Gladys'


class Session20171220Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_12_20_Gladys'


class Session20171220Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_12_20_Havane'


class Session20171221Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_12_21_Gladys'


class Session20171221Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_12_21_Havane'


class Session20171227Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_12_27_Gladys'


class Session20171227Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_12_27_Havane'


class Session20171228Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_12_28_Gladys'


class Session20171228Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2017_12_28_Havane'


class Session20180102Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_02_Gladys'


class Session20180102Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_02_Havane'


class Session20180103Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_03_Gladys'


class Session20180103Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_03_Havane'


class Session20180104Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_04_Gladys'


class Session20180104Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_04_Havane'


class Session20180105Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_05_Gladys'


class Session20180105Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_05_Havane'


class Session20180108Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_08_Gladys'


class Session20180108Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_08_Havane'


class Session20180110Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_10_Gladys'


class Session20180110Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_10_Havane'


class Session20180111Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_11_Gladys'


class Session20180111Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_11_Havane'


class Session20180112Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_12_Gladys'


class Session20180112Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    fixation_time = models.IntegerField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    inter_trial_time = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_to_come_back_to_the_grip = models.IntegerField(blank=True, null=True)
    time_to_decide = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_12_Havane'


class Session20180123Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_23_Gladys'


class Session20180123Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_23_Havane'


class Session20180124Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_24_Gladys'


class Session20180124Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_24_Havane'


class Session20180126Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_26_Gladys'


class Session20180126Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_26_Havane'


class Session20180130Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_30_Gladys'


class Session20180130Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_01_30_Havane'


class Session20180201Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_01_Gladys'


class Session20180201Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_01_Havane'


class Session20180202Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_02_Gladys'


class Session20180202Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_02_Havane'


class Session20180206Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_06_Gladys'


class Session20180206Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_06_Havane'


class Session20180207Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_07_Gladys'


class Session20180207Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_07_Havane'


class Session20180208Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_08_Gladys'


class Session20180208Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_08_Havane'


class Session20180213Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_13_Gladys'


class Session20180213Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_13_Havane'


class Session20180214Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_14_Gladys'


class Session20180214Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_14_Havane'


class Session20180215Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_15_Gladys'


class Session20180215Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_15_Havane'


class Session20180219Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_19_Gladys'


class Session20180219Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_19_Havane'


class Session20180220Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_20_Gladys'


class Session20180221Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_21_Gladys'


class Session20180221Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_21_Havane'


class Session20180222Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_22_Gladys'


class Session20180222Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_22_Havane'


class Session20180223Gladys(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.IntegerField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_23_Gladys'


class Session20180223Havane(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    choice = models.TextField(blank=True, null=True)
    dice_output = models.IntegerField(blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    gauge_level = models.TextField(blank=True, null=True)
    left_beginning_angle = models.IntegerField(blank=True, null=True)
    left_p = models.TextField(blank=True, null=True)
    left_x0 = models.TextField(blank=True, null=True)
    left_x1 = models.IntegerField(blank=True, null=True)
    n_block = models.IntegerField(blank=True, null=True)
    n_trial_inside_block = models.IntegerField(blank=True, null=True)
    right_beginning_angle = models.IntegerField(blank=True, null=True)
    right_p = models.TextField(blank=True, null=True)
    right_x0 = models.TextField(blank=True, null=True)
    right_x1 = models.IntegerField(blank=True, null=True)
    time_back_movement = models.IntegerField(blank=True, null=True)
    time_fixation = models.IntegerField(blank=True, null=True)
    time_inter_block = models.IntegerField(blank=True, null=True)
    time_inter_trial = models.IntegerField(blank=True, null=True)
    time_movement = models.IntegerField(blank=True, null=True)
    time_reaction = models.IntegerField(blank=True, null=True)
    time_stamp_cue_contact = models.IntegerField(blank=True, null=True)
    time_stamp_cue_onset = models.IntegerField(blank=True, null=True)
    time_stamp_grip_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_block_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_inter_trial_interval_onset = models.IntegerField(blank=True, null=True)
    time_stamp_release_grip = models.IntegerField(blank=True, null=True)
    time_stamp_result_period_onset = models.IntegerField(blank=True, null=True)
    time_stamp_reward_period_onset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session_2018_02_23_Havane'


class Summary(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.TextField(blank=True, null=True)
    session_table = models.TextField(blank=True, null=True)
    fake = models.TextField(blank=True, null=True)
    fixation_time = models.TextField(blank=True, null=True)
    initial_stock = models.IntegerField(blank=True, null=True)
    inter_trial_time = models.TextField(blank=True, null=True)
    max_decision_time = models.IntegerField(blank=True, null=True)
    max_return_time = models.IntegerField(blank=True, null=True)
    monkey = models.TextField(blank=True, null=True)
    punishment_time = models.IntegerField(blank=True, null=True)
    result_display_time = models.IntegerField(blank=True, null=True)
    reward_time = models.IntegerField(blank=True, null=True)
    trials_per_block = models.IntegerField(blank=True, null=True)
    valve_opening_time = models.IntegerField(blank=True, null=True)
    control_trials_proportion = models.IntegerField(blank=True, null=True)
    incongruent_proportion = models.IntegerField(blank=True, null=True)
    with_losses_proportion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'summary'
