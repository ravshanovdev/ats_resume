from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import ChatUser, Message


class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.user_code = self.scope["url_route"]["kwargs"]["user_code"]
        self.room_group_name = f"chat_{self.user_code}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive_json(self, content):
        message = content["message"]

        user = self.scope.get("user")
        sender = "admin" if user and user.is_authenticated and user.is_staff else "user"

        chat_user, _ = await self.get_or_create_user(self.user_code)
        await self.create_message(chat_user, sender, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "sender": sender,
            }
        )

    async def chat_message(self, event):
        await self.send_json({
            "message": event["message"],
            "sender": event["sender"],
        })

    @sync_to_async
    def get_or_create_user(self, user_code):
        return ChatUser.objects.get_or_create(user_code=user_code)

    @sync_to_async
    def create_message(self, chat_user, sender, text):
        return Message.objects.create(
            chat_user=chat_user,
            sender=sender,
            text=text
        )
