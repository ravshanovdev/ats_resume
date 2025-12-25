from allinoneapp.serializers.open_position_serializers import CommonOpenPositionSerializer, HelperOpenPositionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from allinoneapp.models.open_position_models import CommonOpenPosition, HelperOpenPosition
from drf_yasg.utils import swagger_auto_schema


class GetAllCommonOpenPositionAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        positions = CommonOpenPosition.objects.all()

        serializer = CommonOpenPositionSerializer(positions, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# FOR ADMIN PANEL CommonOpenPosition

class AddCommonOpenPositionAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_common_position'],
        request_body=CommonOpenPositionSerializer,
        responses={201: f"{CommonOpenPositionSerializer}"}
    )
    def post(self, request):
        serializer = CommonOpenPositionSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCommonOpenPositionAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_common_position'],
        request_body=CommonOpenPositionSerializer,
        responses={201: f"{CommonOpenPositionSerializer}"}
    )
    def patch(self, request, pk):
        try:
            position = CommonOpenPosition.objects.get(pk=pk)
        except CommonOpenPosition.DoesNotExist:
            return Response({"message": "Object Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CommonOpenPositionSerializer(position, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCommonOpenPositionAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_common_position'],

    )

    def delete(self, request, pk):
        try:
            position = CommonOpenPosition.objects.get(pk=pk)
        except CommonOpenPosition.DoesNotExist:
            return Response({"message": "Object Not Found"}, status=status.HTTP_404_NOT_FOUND)

        position.delete()

        return Response({"message": "object successfully deleted.!"}, status=status.HTTP_200_OK)


# FOR ADMIN PANEL HelperPosition

class AddHelperPositionAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_helper_position'],
        request_body=HelperOpenPositionSerializer,
        responses={201: f"{HelperOpenPositionSerializer}"}
    )
    def post(self, request):
        serializer = HelperOpenPositionSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateHelperPositionAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_helper_position'],
        request_body=HelperOpenPositionSerializer,
        responses={201: f"{HelperOpenPositionSerializer}"}
    )
    def patch(self, request, pk):
        try:
            helper_position = HelperOpenPosition.objects.get(pk=pk)
        except HelperOpenPosition.DoesNotExist:
            return Response({"message": "Object Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = HelperOpenPositionSerializer(helper_position, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteHelperPositionAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_helper_position']
    )
    def delete(self, request, pk):
        try:
            helper_position = HelperOpenPosition.objects.get(pk=pk)
        except HelperOpenPosition.DoesNotExist:
            return Response({"message": "Object Not Found"}, status=status.HTTP_404_NOT_FOUND)

        helper_position.delete()

        return Response({"message": "object successfully deleted.!"}, status=status.HTTP_200_OK)