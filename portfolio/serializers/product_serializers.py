from rest_framework import serializers
from portfolio.models.product_models import Category, Product, UserOpinionAboutProduct


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance



class UserOpinionAboutProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOpinionAboutProduct
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user_opinion = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description', 'image', 'play_market_url', 'app_store_url', 'user_opinion']

    def get_user_opinion(self, obj):
        data =  UserOpinionAboutProduct.objects.filter(product=obj)
        serializer = UserOpinionAboutProductSerializer(data, many=True)
        return serializer.data

class AddProductSerializer(serializers.ModelSerializer):
    user_opinion = serializers.SerializerMethodField()
    name = serializers.CharField(required=False, allow_blank=True)
    category = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)
    play_market_url = serializers.CharField(required=False, allow_blank=True)
    app_store_url = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description', 'image', 'play_market_url', 'app_store_url', 'user_opinion']

    def get_user_opinion(self, obj):
        return UserOpinionAboutProduct.objects.filter(product=obj)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.description = validated_data.get('description', instance.description)
        if 'image' in validated_data:
            instance.image = validated_data['image']
        instance.play_market_url = validated_data.get('play_market_url', instance.play_market_url)
        instance.app_store_url = validated_data.get('app_store_url', instance.app_store_url)
        instance.save()
        return instance