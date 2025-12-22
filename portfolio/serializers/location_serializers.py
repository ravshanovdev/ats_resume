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


class AddHelperLocationSerializer(serializers.ModelSerializer):
    # location = AddLocationSerializer(required=True)

    class Meta:
        model = HelperLocation
        fields = ['id', 'country', 'description', 'location_url', 'location']

