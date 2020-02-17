from django.db import models


# Create your models here.
class Stimuli(models.Model):

    left_p = models.FloatField(default=-1000)
    left_x0 = models.IntegerField(default=-1000)
    right_p = models.FloatField(default=-1000)
    right_x0 = models.IntegerField(default=-1000)
    lottery_type = models.IntegerField(default=-1000)
    control = models.BooleanField()
    congruent = models.BooleanField()
    incongruent = models.BooleanField()
    description = models.TextField()

    class Meta:
        db_table = 'stimuli'
