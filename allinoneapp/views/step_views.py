from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from allinoneapp.serializers.step_serializers import StepSerializer, CommonStepSerializer
from allinoneapp.models.step_models import Step, CommonStep
from django.shortcuts import get_object_or_404


class GetStepAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        step = get_object_or_404(CommonStep, pk=pk)

        serializer = CommonStepSerializer(step)

        return Response(serializer.data, status=status.HTTP_200_OK)



