from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts import get_object_or_404
from services.models.some_service_models import FirstInfoAnyService, SpecialData, UsedTechnologyAndOthers

from services.serializers.some_service_serializers import FirstInfoAnyServiceSerializer, SpecialDataSerializer, \
    UsedTechnologyAndOthersSerializer


class GetSpecialDateAPIView(APIView):
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












