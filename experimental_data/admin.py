from django.contrib import admin

from . models import ExperimentalData


# Register your models here.
class ExperimentalDataAdmin(admin.ModelAdmin):
    list_display = ("monkey", "date", "choice")


admin.site.register(ExperimentalData, ExperimentalDataAdmin)
