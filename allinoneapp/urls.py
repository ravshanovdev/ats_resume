from django.urls import path
from allinoneapp.views.statistic_views import GetStatisticAPIView, AddStatisticAPIView, ChangeStatisticAPIView, \
            DeleteStatisticAPIView, AddHelperStatisticAPIView, UpdateHelperStatisticAPIView, DeleteHelperStatisticAPIView
from allinoneapp.views.step_views import GetStepAPIView, AddCommonStepAPIView, UpdateCommonStepAPIView, \
            DeleteCommonStepAPIView, AddStepAPIView, UpdateStepAPIView, DeleteStepAPIView


urlpatterns = [
    path('get_statistic/<int:pk>/', GetStatisticAPIView.as_view(), ),
    path('get_common_step/<int:pk>/', GetStepAPIView.as_view(), ),

    # FOR ADMIN PANEL statistic
    path('add_statistic/', AddStatisticAPIView.as_view(), ),
    path('update_statistic/<int:pk>/', ChangeStatisticAPIView.as_view(), ),
    path('delete_statistic/<int:pk>/', DeleteStatisticAPIView.as_view(), ),

    # FOR ADMIN PANEL HelperStatistic
    path('add_helper_statistic/', AddHelperStatisticAPIView.as_view(), ),
    path('update_helper_statistic/<int:pk>/', UpdateHelperStatisticAPIView.as_view(), ),
    path('delete_helper_statistic/<int:pk>/', DeleteHelperStatisticAPIView.as_view(), ),


    # FOR ADMIN PANEL CommonStep
    path('add_common_step/', AddCommonStepAPIView.as_view(), ),
    path('update_common_step/<int:pk>/', UpdateCommonStepAPIView.as_view(), ),
    path('delete_common_step/<int:pk>/', DeleteCommonStepAPIView.as_view(), ),

    # FOR ADMIN PANEL Step
    path('add_step/', AddStepAPIView.as_view(), ),
    path('update_step/<int:pk>/', UpdateStepAPIView.as_view(), ),
    path('delete_step/<int:pk>/', DeleteStepAPIView.as_view(), ),

]

