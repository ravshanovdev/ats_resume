from rest_framework import serializers
from allinoneapp.models.statistic_models import HelperStatistic, Statistic


class HelperStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelperStatistic
        fields = ['id', 'count', 'description']


class StatisticSerializer(serializers.ModelSerializer):
    helper_statistic = serializers.SerializerMethodField()

    class Meta:
        model = Statistic
        fields = ['id', 'helper_statistic', 'created_at']


    def get_helper_statistic(self, obj):
        helper = HelperStatistic.objects.filter(statistic=obj)
        return HelperStatisticSerializer(helper, many=True).data
