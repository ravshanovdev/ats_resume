from django.urls import path
from allinoneapp.views.statistic_views import (GetStatisticAPIView, AddStatisticAPIView, UpdateStatisticAPIView,
                                               DeleteStatisticAPIView)
from allinoneapp.views.step_views import GetStepAPIView


urlpatterns = [
    path('get_statistic/<int:pk>/', GetStatisticAPIView.as_view(), ),
    path('get_common_step/<int:pk>/', GetStepAPIView.as_view(), ),

    # FOR ADMIN PANEL statistic
    path('add_statistic/', AddStatisticAPIView.as_view(), ),
    path('update_statistic/<int:pk>/', UpdateStatisticAPIView.as_view(), ),
    path('delete_statistic/<int:pk>/', DeleteStatisticAPIView.as_view(), ),

]

