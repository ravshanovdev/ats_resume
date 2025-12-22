from rest_framework import serializers
from services.models.some_service_models import FirstInfoAnyService, SpecialData, UsedTechnologyAndOthers


class SpecialDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialData
        fields = ['id', 'title_1', 'description_1', 'title_2', 'description_2', 'image']


class UsedTechnologyAndOthersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsedTechnologyAndOthers
        fields = ['id', 'title', 'description', 'first_info']


class FirstInfoAnyServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstInfoAnyService
        fields = ['id', 'title', 'description', 'image']




