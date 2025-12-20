from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from portfolio.serializers.location_serializers import LocationSerializer
from portfolio.models.location_models import Location
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404


class GetLocationAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        location = get_object_or_404(Location, pk=pk)
        serializer = LocationSerializer(location)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

