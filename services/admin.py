from django.contrib import admin
from .models.user_message_models import Industry, TellUsAboutYourProject
from .models.some_service_models2 import SuccessfullyDevelopment, ClientsOpinion, FrequentlyQuestion
from .models.some_service_models import FirstInfoAnyService, SpecialData, UsedTechnologyAndOthers

admin.site.register([Industry, TellUsAboutYourProject])
admin.site.register([SuccessfullyDevelopment, ClientsOpinion])
admin.site.register([SpecialData, UsedTechnologyAndOthers])


class FrequentlyQuestionInline(admin.StackedInline):
    model = FrequentlyQuestion

class UsedTechnologyAndOthersInline(admin.StackedInline):
    model = UsedTechnologyAndOthers

@admin.register(FirstInfoAnyService)
class FirstInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

    inlines = [
        FrequentlyQuestionInline,
        UsedTechnologyAndOthersInline,

    ]

