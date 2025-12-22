from django.urls import path
from services.views.some_services_views import GetFirstInfoAnyServiceAPIView, GetSpecialDateAPIView, \
        GetUsedTechnologyAndOthersAPIView, AddSpecialDateAPIView, UpdateSpecialDateAPIView, DeleteSpecialData, \
        AddUsedTechnologyAndOthersAPIView, UpdateUsedTechnologyAndOthersAPIView, DeleteUsedTechnologyAndOthersAPIView

from services.views.some_services_views2 import (GetClientOpinionAPIView, GetFrequentlyQuestionAPIView,
                                                 GetSuccessfullyDevelopmentAPIView)

from services.views.user_message_views import TellUsAboutYourProjectAPIView

urlpatterns = [
    path('get_first_info/<int:pk>/', GetFirstInfoAnyServiceAPIView.as_view(), ),
    path('get_spacial_date/<int:pk>/', GetSpecialDateAPIView.as_view(), ),
    path('get_used_techno/<int:pk>/', GetUsedTechnologyAndOthersAPIView.as_view(), ),

    path('get_client_opinion/<int:pk>/', GetClientOpinionAPIView.as_view(), ),
    # path("get_frequently_question/", GetFrequentlyQuestionAPIView.as_view(), ),
    path("get_success_dev/<int:pk>/", GetSuccessfullyDevelopmentAPIView.as_view(), ),
    path("tell_us_about_your_project/", TellUsAboutYourProjectAPIView.as_view(), ),


    # FOR ADMIN PANEL SpecialData
    path('add_special_data/', AddSpecialDateAPIView.as_view(), ),
    path('update_special_data/<int:pk>/', UpdateSpecialDateAPIView.as_view(), ),
    path('delete_special_data/<int:pk>/', DeleteSpecialData.as_view(), ),

    # FOR ADMIN PANEL UsedTechnology
    path('add_used_technology/', AddUsedTechnologyAndOthersAPIView.as_view(), ),
    path('update_used_technology/<int:pk>/', UpdateUsedTechnologyAndOthersAPIView.as_view(), ),
    path('delete_used_technology/<int:pk>/', DeleteUsedTechnologyAndOthersAPIView.as_view(), ),





]