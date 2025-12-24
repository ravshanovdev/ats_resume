from rest_framework import serializers
from services.models.some_service_models import FirstInfoAnyService, SpecialData, UsedTechnologyAndOthers


class SpecialDataSerializer(serializers.ModelSerializer):
    title_1 = serializers.CharField(required=False, allow_blank=True)
    description_1 = serializers.CharField(required=False, allow_blank=True)
    title_2 = serializers.CharField(required=False, allow_blank=True)
    description_2 = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = SpecialData
        fields = ['id', 'title_1', 'description_1', 'title_2', 'description_2', 'image']

    def update(self, instance, validated_data):
        instance.title_1 = validated_data.get('title_1', instance.title_1)
        instance.description_1 = validated_data.get('description_1', instance.description_1)
        instance.title_2 = validated_data.get('title_2', instance.title_2)
        instance.description_2 = validated_data.get('description_2', instance.description_2)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance


class UsedTechnologyAndOthersSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)
    first_info = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = UsedTechnologyAndOthers
        fields = ['id', 'title', 'description', 'first_info', 'image']

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.first_info = validated_data.get('first_info', instance.first_info)
    #     if 'image' in validated_data:
    #         instance.image = validated_data.get('image', instance.image)
    #     instance.save()
    #     return instance


class AddUsedTechnologyAndOthersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsedTechnologyAndOthers
        fields = ['id', 'title', 'description', 'first_info', 'image']


class FirstInfoAnyServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstInfoAnyService
        fields = ['id', 'title', 'description', 'image']




