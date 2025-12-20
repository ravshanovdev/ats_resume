from django.urls import path
from allinoneapp.views.statistic_views import GetStatisticAPIView
from allinoneapp.views.step_views import GetStepAPIView


urlpatterns = [
    path('get_statistic/<int:pk>/', GetStatisticAPIView.as_view(), ),
    path('get_common_step/<int:pk>/', GetStepAPIView.as_view(), ),

]

