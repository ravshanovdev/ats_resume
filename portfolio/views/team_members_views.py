from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from portfolio.serializers.team_members_serializers import TeamMembersSerializer
from portfolio.models.blog import TeamMembers
from rest_framework.permissions import AllowAny, IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser


class GetAllTeamMembersAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        members = TeamMembers.objects.all()

        serializer = TeamMembersSerializer(members, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# FOR ADMIN PANEL TeamMembers

class AddTeamMemberAPIView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        tags=['admin_panel_team_members'],
        request_body=TeamMembersSerializer,
        responses={201: f"{TeamMembersSerializer}"}
    )
    def post(self, request):
        serializer = TeamMembersSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateTeamMemberAPIView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        tags=['admin_panel_team_members'],
        request_body=TeamMembersSerializer(partial=True),
        responses={201: f"{TeamMembersSerializer}"}
    )
    def patch(self, request, pk):
        try:
            team_member = TeamMembers.objects.get(pk=pk)
        except TeamMembers.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeamMembersSerializer(team_member, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteTeamMemberAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_team_members']
    )
    def delete(self, request, pk):
        try:
            team_member = TeamMembers.objects.get(pk=pk)
        except TeamMembers.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        team_member.delete()

        return Response({"message": "object successfully deleted.!"}, status=status.HTTP_200_OK)