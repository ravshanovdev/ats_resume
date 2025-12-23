from django.urls import path
from portfolio.views.product_views import GetAllCategoryAPIView, GetProductsByCategoryAPIView, \
            GetALlProductsAPIView, AddCategoryAPIView, UpdateCategoryAPIView, DeleteCategoryAPIView, \
            AddProductAPIView, UpdateProductAPIView, DeleteProductAPIView, AddUserOpinionAboutProductAPIView, \
            UpdateUserOpinionAboutProductAPIView, DeleteUserOpinionAboutProductAPIView, GetAllUserOpinionAboutProductAPIView

from portfolio.views.location_views import GetLocationAPIView, AddLocationAPIView, UpdateLocationAPIView, \
            DeleteLocationAPIView, AddHelperLocationAPIView, UpdateHelperLocationAPIView, DeleteHelperLocationAPIView, \
            GetHelperLocationAPIView
from portfolio.views.team_members_views import GetAllTeamMembersAPIView


urlpatterns = [
    path('get_all_categorys/', GetAllCategoryAPIView.as_view(), ),
    path('get_product_by_category/<int:pk>/', GetProductsByCategoryAPIView.as_view(), ),
    path('get_all_products/', GetALlProductsAPIView.as_view(), ),
    path('get_all_user_opinion/', GetAllUserOpinionAboutProductAPIView.as_view(), ),

    path('get_location/<int:pk>/', GetLocationAPIView.as_view(), ),
    path('get_helper_location/', GetHelperLocationAPIView.as_view(), ),
    path('get_all_members/', GetAllTeamMembersAPIView.as_view(), ),


    # FOR ADMIN PANEL Location
    path('add_location/', AddLocationAPIView.as_view(), ),
    path('update_location/<int:pk>/', UpdateLocationAPIView.as_view(), ),
    path('delete_location/<int:pk>/', DeleteLocationAPIView.as_view(), ),

    # FOR ADMIN PANEL HelperLocation
    path("add_helper_location/", AddHelperLocationAPIView.as_view(), ),
    path("update_helper_location/<int:pk>/", UpdateHelperLocationAPIView.as_view(), ),
    path("delete_helper_location/<int:pk>/", DeleteHelperLocationAPIView.as_view(), ),

    # FOR ADMIN PANEL Category
    path("add_category/", AddCategoryAPIView.as_view(), ),
    path("update_category/<int:pk>/", UpdateCategoryAPIView.as_view(), ),
    path("delete_category/<int:pk>/", DeleteCategoryAPIView.as_view(), ),

    # FOR ADMIN PANEL Product
    path("add_product/", AddProductAPIView.as_view(), ),
    path("update_product/<int:pk>/", UpdateProductAPIView.as_view(), ),
    path("delete_product/<int:pk>/", DeleteProductAPIView.as_view(), ),

    # FOR ADMIN PANEL UserOpinionAboutProduct
    path('add_user_opinion/', AddUserOpinionAboutProductAPIView.as_view(), ),
    path('update_user_opinion/<int:pk>/', UpdateUserOpinionAboutProductAPIView.as_view(), ),
    path('delete_user_opinion/<int:pk>/', DeleteUserOpinionAboutProductAPIView.as_view(), ),




]