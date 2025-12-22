from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status
from django.shortcuts import get_object_or_404
from services.models.some_service_models import FirstInfoAnyService, SpecialData, UsedTechnologyAndOthers
from drf_yasg.utils import swagger_auto_schema
from services.serializers.some_service_serializers import FirstInfoAnyServiceSerializer, SpecialDataSerializer, \
    UsedTechnologyAndOthersSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class GetSpecialDateAPIView(APIView): # ADMIN PANEL Version DONE
    permission_classes = [AllowAny]

    def get(self, request, pk):
        special_data = get_object_or_404(SpecialData, pk=pk)

        serializer = SpecialDataSerializer(special_data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetUsedTechnologyAndOthersAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        data = get_object_or_404(UsedTechnologyAndOthers, pk=pk)

        serializer = UsedTechnologyAndOthersSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetFirstInfoAnyServiceAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        first_info = get_object_or_404(FirstInfoAnyService, pk=pk)

        serializer = FirstInfoAnyServiceSerializer(first_info)
        return Response(serializer.data, status=status.HTTP_200_OK)


# SPECIAL_DATA FOR ADMIN PANEL
class AddSpecialDateAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_special_data'],
        request_body=SpecialDataSerializer,
        responses={201: "special_data successfully created"}
    )
    def post(self, request):
        serializer = SpecialDataSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateSpecialDateAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_special_data'],
        request_body=SpecialDataSerializer,
        responses={200: "object successfully updated.!"}
    )
    def patch(self, request, pk):
        try:
            special_data = SpecialData.objects.get(pk=pk)

        except SpecialData.DoesNotExist:
            return Response({"message": "special data not found.!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SpecialDataSerializer(special_data, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteSpecialData(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_special_data']
    )
    def delete(self, request, pk):
        try:
            special_data = SpecialData.objects.get(pk=pk)
        except SpecialData.DoesNotExist:
            return Response({"message": "SpecialDate object Not Found.!"}, status=status.HTTP_404_NOT_FOUND)

        special_data.delete()

        return Response({"message": "SpecialData object successfully deleted.!"}, status=status.HTTP_200_OK)



# UsedTechnologyAndOthers ADMIN PANEL


class AddUsedTechnologyAndOthersAPIView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        tags=['admin_panel_used_technology'],
        request_body=UsedTechnologyAndOthersSerializer,
        responses={201: "object successfully created"}

    )
    def post(self, request):
        serializer = UsedTechnologyAndOthersSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateUsedTechnologyAndOthersAPIView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        tags=['admin_panel_used_technology'],
        request_body=UsedTechnologyAndOthersSerializer,
        responses={200: 'object successfully updated'}
    )
    def patch(self, request, pk):
        try:
            techno = UsedTechnologyAndOthers.objects.get(pk=pk)
        except UsedTechnologyAndOthers.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UsedTechnologyAndOthersSerializer(techno, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteUsedTechnologyAndOthersAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_used_technology'],

    )
    def delete(self, request, pk):
        try:
            techno = UsedTechnologyAndOthers.objects.get(pk=pk)
        except UsedTechnologyAndOthers.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        techno.delete()

        return Response({"message": "object successfully deleted.!"}, status=status.HTTP_200_OK)














