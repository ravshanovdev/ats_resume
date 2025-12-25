from django.contrib import admin
from allinoneapp.models.step_models import CommonStep, Step
from allinoneapp.models.statistic_models import HelperStatistic, Statistic
from allinoneapp.models.open_position_models import CommonOpenPosition, HelperOpenPosition


class HelperOpenPositionInline(admin.StackedInline):
    model = HelperOpenPosition


@admin.register(CommonOpenPosition)
class CommonOpenPositionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

    inlines = [
        HelperOpenPositionInline
    ]

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

