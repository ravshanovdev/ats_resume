from django.urls import path
from portfolio.views.product_views import (GetAllCategoryAPIView, GetProductsByCategoryAPIView,
                                           GetALlProductsAPIView)
from portfolio.views.location_views import GetLocationAPIView
from portfolio.views.team_members_views import GetAllTeamMembersAPIView


urlpatterns = [
    path('get_all_categorys/', GetAllCategoryAPIView.as_view(), ),
    path('get_product_by_category/<int:pk>/', GetProductsByCategoryAPIView.as_view(), ),
    path('get_all_products/', GetALlProductsAPIView.as_view(), ),

    path('get_location/<int:pk>/', GetLocationAPIView.as_view(), ),
    path('get_all_members/', GetAllTeamMembersAPIView.as_view(), ),


]