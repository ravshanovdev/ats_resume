from rest_framework import serializers
from allinoneapp.models.step_models import CommonStep, Step


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id', 'title', 'description', 'icon_file']


class CommonStepSerializer(serializers.ModelSerializer):
    step = serializers.SerializerMethodField()

    class Meta:
        model = CommonStep
        fields = ['id', 'common_title', 'step']

    def get_step(self, obj):
        step = Step.objects.filter(steps=obj)
        serializer = StepSerializer(step, many=True)
        return serializer.data