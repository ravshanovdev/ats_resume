from rest_framework import serializers
from portfolio.models.blog import TeamMembers


class TeamMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembers
        fields = ['id', 'name', 'description', 'picture']