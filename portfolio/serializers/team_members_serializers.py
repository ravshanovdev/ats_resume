from rest_framework import serializers
from portfolio.models.blog import TeamMembers


class TeamMembersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = TeamMembers
        fields = ['id', 'name', 'description', 'picture']


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        if 'picture' in validated_data:
            instance.picture = validated_data['picture']
        instance.save()
        return instance

