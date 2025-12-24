from rest_framework import serializers
from portfolio.models.location_models import HelperLocation, Location


class HelperLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = HelperLocation
        fields = ['id', 'country', 'description', 'location_url']


class LocationSerializer(serializers.ModelSerializer):
    helper_location = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = ['id', 'zone', 'helper_location']

    def get_helper_location(self, obj):
        helper_location = HelperLocation.objects.filter(location=obj)
        return HelperLocationSerializer(helper_location, many=True).data


# FOR ADMIN PANEL

class AddLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'zone']

    def update(self, instance, validated_data):
        instance.zone = validated_data.get('zone', instance.zone)
        instance.save()
        return instance


class AddHelperLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelperLocation
        fields = ['id', 'country', 'description', 'location_url', 'location']

    def update(self, instance, validated_data):
        instance.country = validated_data.get('country', instance.country)
        instance.description = validated_data.get('description', instance.description)
        instance.location_url = validated_data.get('location_url', instance.location_url)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance
