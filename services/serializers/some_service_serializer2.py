from rest_framework import serializers
from services.models.some_service_models2 import SuccessfullyDevelopment, ClientsOpinion, FrequentlyQuestion


class SuccessfullyDevelopmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessfullyDevelopment
        fields = ['id', 'category', 'common_title', 'title_1', 'description_1', 'image_1', 'title_2', 'description_2', 'image_2']


class ClientOpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientsOpinion
        fields = ['id', 'category', 'name', 'description', 'picture', 'grade']


class FrequentlyQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyQuestion
        fields = ['id', 'title', 'description']
        





