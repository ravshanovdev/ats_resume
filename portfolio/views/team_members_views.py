from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from portfolio.serializers.team_members_serializers import TeamMembersSerializer
from portfolio.models.blog import TeamMembers
from rest_framework.permissions import AllowAny


class GetAllTeamMembersAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        members = TeamMembers.objects.all()

        serializer = TeamMembersSerializer(members, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)






