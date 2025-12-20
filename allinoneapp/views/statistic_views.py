from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from allinoneapp.serializers.statistic_serializers import StatisticSerializer
from allinoneapp.models.statistic_models import Statistic
from django.shortcuts import get_object_or_404

class GetStatisticAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        statistic = get_object_or_404(Statistic, pk=pk)

        serializer = StatisticSerializer(statistic)

        return Response(serializer.data, status=status.HTTP_200_OK)



