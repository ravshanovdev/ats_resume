from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts import get_object_or_404

from services.models.some_service_models2 import SuccessfullyDevelopment, ClientsOpinion, FrequentlyQuestion
from services.serializers.some_service_serializer2 import SuccessfullyDevelopmentSerializer, ClientOpinionSerializer, \
    FrequentlyQuestionSerializer



class GetSuccessfullyDevelopmentAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        data = get_object_or_404(SuccessfullyDevelopment, pk=pk)

        serializer = SuccessfullyDevelopmentSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetClientOpinionAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        data = get_object_or_404(ClientsOpinion, pk=pk)

        serializer = ClientOpinionSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetFrequentlyQuestionAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = FrequentlyQuestion.objects.all()

        serializer = FrequentlyQuestionSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
