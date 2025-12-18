from rest_framework import serializers
from services.models.user_message_models import TellUsAboutYourProject


class TellUsAboutYourProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TellUsAboutYourProject
        fields = ['id', 'name', 'phone', 'email', 'message', 'industry', 'budget']


