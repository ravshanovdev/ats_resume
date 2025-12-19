from django.urls import path
from portfolio.views.product_views import (GetAllCategoryAPIView, GetProductsByCategoryAPIView,
                                           GetALlProductsAPIView)


urlpatterns = [
    path('get_all_categorys/', GetAllCategoryAPIView.as_view(), ),
    path('get_product_by_category/<int:pk>/', GetProductsByCategoryAPIView.as_view(), ),
    path('get_all_products/', GetALlProductsAPIView.as_view(), ),


]