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


class AddHelperStatisticSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()

    class Meta:
        model = HelperStatistic
        fields = ['id', 'count', 'description']



class AddStatisticSerializer(serializers.ModelSerializer):
    helper_statistic = AddHelperStatisticSerializer(
        many=True,
        required=True,
        source='helperstatistic'
    )

    class Meta:
        model = Statistic
        fields = ['id', 'created_at', 'helper_statistic']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        helper_stats = validated_data.pop('helperstatistic', [])

        statistic = Statistic.objects.create(**validated_data)

        for helper_stat in helper_stats:
            HelperStatistic.objects.create(
                statistic=statistic,
                **helper_stat
            )
        return statistic

    def update(self, instance, validated_data):
        helpers_data = validated_data.pop('helperstatistic')

        existing_helpers = {
            helper.id: helper
            for helper in instance.helperstatistic.all()
        }

        sent_ids = []

        for helper_data in helpers_data:
            helper_id = helper_data.get('id')

            if helper_id and helper_id in existing_helpers:

                helper = existing_helpers[helper_id]
                helper.count = helper_data.get('count', helper.count)
                helper.description = helper_data.get('description', helper.description)
                helper.save()
                sent_ids.append(helper_id)
            else:

                HelperStatistic.objects.create(
                    statistic=instance,
                    **helper_data
                )

        for helper_id, helper in existing_helpers.items():
            if helper_id not in sent_ids:
                helper.delete()

        return instance
