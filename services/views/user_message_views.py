from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from services.serializers.user_message_serializers import TellUsAboutYourProjectSerializer
import requests
from bot.bot_config import BOT_TOKEN


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
            text = (
                "📝 <b>Yangi so‘rov</b>\n\n"
                f"👤 <b>Ism:</b> {serializer.validated_data['name']}\n"
                f"📞 <b>Telefon:</b> {serializer.validated_data['phone']}\n"
                f"📧 <b>Email:</b> {serializer.validated_data['email']}\n"
                f"💬 <b>Xabar:</b> {serializer.validated_data['message']}\n"
                f"🏭 <b>Soha:</b> {serializer.validated_data['industry']}\n"
                f"💰 <b>Byudjet:</b> {serializer.validated_data['budget']}"
            )

            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            payload = {
                "chat_id": -1003418801315,
                "text": text,
                "parse_mode": "HTML"
            }

            requests.post(url, json=payload)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

