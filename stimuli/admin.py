from django.contrib import admin

# Register your models here.
from django.contrib import admin

from . models import Stimuli


# Register your models here.
class StimuliAdmin(admin.ModelAdmin):
    list_display = ["id", ] + [f.name for f in Stimuli._meta.get_fields()]


admin.site.register(Stimuli, StimuliAdmin)
