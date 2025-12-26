import uuid
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ChatUser, Message
from rest_framework.permissions import IsAdminUser


class StartChatView(APIView):
    def post(self, request):
        user_code = f"user-{uuid.uuid4().hex[:10]}"
        chat_user = ChatUser.objects.create(user_code=user_code)
        return Response({"user_code": chat_user.user_code})



class ChatUserListView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        users = ChatUser.objects.all().order_by("-created_at")
        data = [{"user_code": u.user_code} for u in users]
        return Response(data)


class MessageListView(APIView):
    def get(self, request, user_code):
        messages = Message.objects.filter(
            chat_user__user_code=user_code
        ).order_by("created_at")

        data = [
            {
                "sender": m.sender,
                "text": m.text,
                "created_at": m.created_at
            }
            for m in messages
        ]
        return Response(data)
