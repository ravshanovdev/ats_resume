from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from services.serializers.user_message_serializers import TellUsAboutYourProjectSerializer


class TellUsAboutYourProjectAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=TellUsAboutYourProjectSerializer,
        responses={201: 'message sent.!'}
    )
    def post(self, request):
        serializer = TellUsAboutYourProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

