from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from portfolio.serializers.location_serializers import (LocationSerializer, HelperLocationSerializer, AddLocationSerializer,
                                                        AddHelperLocationSerializer)
from portfolio.models.location_models import Location, HelperLocation
from rest_framework.permissions import AllowAny, IsAdminUser
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


class GetLocationAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        location = get_object_or_404(Location, pk=pk)
        serializer = LocationSerializer(location)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetHelperLocationAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        helper_locations = HelperLocation.objects.all()

        serializer = HelperLocationSerializer(helper_locations, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


# FOR ADMIN PANEL Location

class AddLocationAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_location'],
        request_body=AddLocationSerializer,
        responses={201: f"{AddLocationSerializer}"}
    )
    def post(self, request):
        serializer = AddLocationSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpdateLocationAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_location'],
        request_body=AddLocationSerializer,
        responses={200: f"{AddLocationSerializer}"}
    )
    def patch(self, request, pk):
        try:
            location = Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AddLocationSerializer(location, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteLocationAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_location'],
    )
    def delete(self, request, pk):
        try:
            location = Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        location.delete()

        return Response({"message": "object successfully deleted.!"}, status=status.HTTP_200_OK)


# FOR ADMIN PANEL HelperLocation


class AddHelperLocationAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_helper_location'],
        request_body=AddHelperLocationSerializer,
        responses={201: f"{AddHelperLocationSerializer}"}
    )
    def post(self, request):
        serializer = AddHelperLocationSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpdateHelperLocationAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_helper_location'],
        request_body=AddHelperLocationSerializer,
        responses={200: f"{AddHelperLocationSerializer}"}
    )
    def patch(self, request, pk):
        try:
            location = HelperLocation.objects.get(pk=pk)
        except HelperLocation.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AddHelperLocationSerializer(location, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteHelperLocationAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_helper_location'],
    )
    def delete(self, request, pk):
        try:
            helper_location = HelperLocation.objects.get(pk=pk)
        except HelperLocation.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        helper_location.delete()

        return Response({"message": "object successfully deleted.!"}, status=status.HTTP_200_OK)























