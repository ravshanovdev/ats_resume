from django.contrib import admin
from .models.location_models import Location, HelperLocation
from .models.product_models import Category, UserOpinionAboutProduct, Product
from .models.blog import Blog, TeamMembers


admin.site.register(Blog)
admin.site.register(TeamMembers)

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']



class UserOpinionAboutProductInline(admin.StackedInline):
    model = UserOpinionAboutProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']

    inlines = [
        UserOpinionAboutProductInline,

    ]

class HelperLocationInline(admin.StackedInline):
    model = HelperLocation



@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'zone']

    inlines = [
        HelperLocationInline,

    ]



