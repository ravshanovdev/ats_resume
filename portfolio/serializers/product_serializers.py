from rest_framework import serializers
from portfolio.models.product_models import Category, Product, UserOpinionAboutProduct


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user_opinion = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description', 'image', 'play_market_url', 'app_store_url', 'user_opinion']

    def get_user_opinion(self, obj):
        return UserOpinionAboutProduct.objects.filter(product=obj)
