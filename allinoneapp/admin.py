from django.contrib import admin
from allinoneapp.models.step_models import CommonStep, Step
from allinoneapp.models.statistic_models import HelperStatistic, Statistic


class HelperStatisticInline(admin.StackedInline):
    model = HelperStatistic

class StepInline(admin.StackedInline):
    model = Step

@admin.register(Statistic)
class StatisticModelAdmin(admin.ModelAdmin):

    inlines = [
        HelperStatisticInline,

    ]


@admin.register(CommonStep)
class CommonStepModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'common_title']

    inlines = [
        StepInline,

    ]

