from django.contrib import admin

from . models import ExperimentalData


# Register your models here.
class ExperimentalDataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ExperimentalData._meta.get_fields()]


admin.site.register(ExperimentalData, ExperimentalDataAdmin)
