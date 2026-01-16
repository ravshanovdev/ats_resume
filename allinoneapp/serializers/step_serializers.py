from rest_framework import serializers
from allinoneapp.models.step_models import CommonStep, Step

class CommonStepSerializer(serializers.ModelSerializer):
    step = serializers.SerializerMethodField()

    class Meta:
        model = CommonStep
        fields = ['id', 'category', 'common_title', 'step']

    def get_step(self, obj):
        step = Step.objects.filter(steps=obj)
        serializer = StepSerializer(step, many=True)
        return serializer.data


class AddCommonStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonStep
        fields = ['id', 'category', 'common_title']


class StepSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)
    steps = serializers.PrimaryKeyRelatedField(
        queryset=CommonStep.objects.all(),
        required=False
    )

    class Meta:
        model = Step
        fields = ['id', 'title', 'description', 'icon_file', 'steps']

