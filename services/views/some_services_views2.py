from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from services.models.some_service_models2 import SuccessfullyDevelopment, ClientsOpinion
from services.serializers.some_service_serializer2 import SuccessfullyDevelopmentSerializer, ClientOpinionSerializer
from rest_framework.parsers import MultiPartParser, FormParser



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


# FOR ADMIN PANEL SuccessfullyDevelopment

class AddSuccessfullyDevelopmentAPIView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        tags=['admin_panel_SuccessfullyDevelopment'],
        request_body = SuccessfullyDevelopmentSerializer,
        responses={201: f"{SuccessfullyDevelopment}"}
    )
    def post(self, request):
        serializer = SuccessfullyDevelopmentSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateSuccessfullyDevelopmentAPIView(APIView):
    permission_classes = [IsAdminUser]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
        tags=['admin_panel_SuccessfullyDevelopment'],
        request_body=SuccessfullyDevelopmentSerializer,
        responses={201: f"{SuccessfullyDevelopmentSerializer}"}
    )
    def patch(self, request, pk):
        try:
            success_dev = SuccessfullyDevelopment.objects.get(pk=pk)
        except SuccessfullyDevelopment.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SuccessfullyDevelopmentSerializer(success_dev, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteSuccessfullyDevelopmentAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_SuccessfullyDevelopment'],
    )
    def delete(self, request, pk):
        try:
            success_dev = SuccessfullyDevelopment.objects.get(pk=pk)
        except SuccessfullyDevelopment.DoesNotExist:
            return Response({"message": "object not found.!"}, status=status.HTTP_404_NOT_FOUND)

        success_dev.delete()

        return Response({"message": "object successfully deleted.!"}, status=status.HTTP_200_OK)



# FOR ADMIN PANEL ClientOption

class AddClientOpinionAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_client_option'],
        request_body=ClientOpinionSerializer,
        responses={201: f"{ClientOpinionSerializer}"}
    )
    def post(self, request):
        serializer = ClientOpinionSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UpdateClientOptionAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_client_option'],
        request_body=ClientOpinionSerializer,
        responses={200: f"{ClientOpinionSerializer}"}
    )
    def patch(self, request, pk):
        try:
            client_option = ClientsOpinion.objects.get(pk=pk)

        except ClientsOpinion.DoesNotExist:
            return Response({"message": "special data not found.!"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClientOpinionSerializer(client_option, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DeleteClientOpinionAPIView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        tags=['admin_panel_client_option']
    )
    def delete(self, request, pk):
        try:
            client_option = ClientsOpinion.objects.get(pk=pk)

        except ClientsOpinion.DoesNotExist:
            return Response({"message": "special data not found.!"}, status=status.HTTP_404_NOT_FOUND)

        client_option.delete()

        return Response({"message": "SpecialData object successfully deleted.!"}, status=status.HTTP_200_OK)







