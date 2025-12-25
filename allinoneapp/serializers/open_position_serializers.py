from rest_framework import serializers
from allinoneapp.models.open_position_models import CommonOpenPosition, HelperOpenPosition


class HelperOpenPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelperOpenPosition
        fields = ['id', 'title', 'description', 'common_op']


class CommonOpenPositionSerializer(serializers.ModelSerializer):
    helper_position = serializers.SerializerMethodField()

    class Meta:
        model = CommonOpenPosition
        fields = ['id', 'title', 'helper_position']

    def get_helper_position(self, obj):
        return HelperOpenPositionSerializer(HelperOpenPosition.objects.filter(common_op=obj), many=True).data
