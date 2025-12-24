from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from allinoneapp.serializers.step_serializers import StepSerializer, CommonStepSerializer, AddCommonStepSerializer
from allinoneapp.models.step_models import Step, CommonStep
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser, FormParser


class GetStepAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        step = get_object_or_404(CommonStep, pk=pk)

        serializer = CommonStepSerializer(step)

        return Response(serializer.data, status=status.HTTP_200_OK)


# FOR ADMIN PANEL Step

class AddCommonStepAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_common_step'],
        request_body=AddCommonStepSerializer,
        responses={201: f"{AddCommonStepSerializer}"}
    )
    def post(self, request):
        serializer = AddCommonStepSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateCommonStepAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_common_step'],
        request_body=AddCommonStepSerializer(partial=True),
        responses={201: f"{AddCommonStepSerializer}"}
    )
    def patch(self, request, pk):
        try:
            step = CommonStep.objects.get(pk=pk)
        except CommonStep.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AddCommonStepSerializer(step, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCommonStepAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_common_step']
    )
    def delete(self, request, pk):
        try:
            step = CommonStep.objects.get(pk=pk)
        except CommonStep.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        step.delete()

        return Response({'message': "object successfully deleted!"}, status=status.HTTP_200_OK)



# FOR ADMIN PANEL Step

class AddStepAPIView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        tags=['admin_panel_step'],
        request_body=StepSerializer,
        responses={201: f"{StepSerializer}"}
    )
    def post(self, request):
        serializer = StepSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateStepAPIView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        tags=['admin_panel_step'],
        request_body=StepSerializer(partial=True),
        responses={201: f"{StepSerializer}"}
    )
    def patch(self, request, pk):
        try:
            step = Step.objects.get(pk=pk)
        except Step.DoesNotExist:
            return Response({"message": "object not found.!"},status=status.HTTP_404_NOT_FOUND)

        serializer = StepSerializer(step, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







