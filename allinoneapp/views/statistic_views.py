from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from allinoneapp.serializers.statistic_serializers import StatisticSerializer, AddStatisticSerializer, AddHelperStatisticSerializer
from allinoneapp.models.statistic_models import Statistic, HelperStatistic
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser


class GetStatisticAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        statistic = get_object_or_404(Statistic, pk=pk)

        serializer = StatisticSerializer(statistic)

        return Response(serializer.data, status=status.HTTP_200_OK)


# FOR ADMIN PANEL Statistic

class AddStatisticAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_statistic'],
        request_body=AddStatisticSerializer,
        responses={201: f"{AddStatisticSerializer}"}
    )
    def post(self, request):
        serializer = AddStatisticSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangeStatisticAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_statistic'],
        request_body=AddStatisticSerializer(partial=True),
        responses={200: f"{AddStatisticSerializer}"}
    )
    def patch(self, request, pk):
        try:
            statistic = Statistic.objects.get(pk=pk)
        except Statistic.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AddStatisticSerializer(statistic, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteStatisticAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_statistic']
    )
    def delete(self, request, pk):
        try:
            statistic = Statistic.objects.get(pk=pk)
        except Statistic.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        statistic.delete()

        return Response({"message": "object successfully deleted.!"}, status=status.HTTP_200_OK)


# FOR ADMIN PANEL HelperStatistic

class AddHelperStatisticAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_helper_statistic'],
        request_body=AddHelperStatisticSerializer,
        responses={201: f"{AddHelperStatisticSerializer}"}
    )
    def post(self, request):
        serializer = AddHelperStatisticSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateHelperStatisticAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_helper_statistic'],
        request_body=AddHelperStatisticSerializer(partial=True),
        responses={200: f"{AddHelperStatisticSerializer}"}
    )
    def patch(self, request, pk):
        try:
            statistic = HelperStatistic.objects.get(pk=pk)
        except HelperStatistic.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AddHelperStatisticSerializer(statistic, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteHelperStatisticAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_helper_statistic']
    )
    def delete(self, request, pk):
        try:
            statistic = HelperStatistic.objects.get(pk=pk)
        except HelperStatistic.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        statistic.delete()

        return Response({"message": "object successfully deleted.!"}, status=status.HTTP_200_OK)
