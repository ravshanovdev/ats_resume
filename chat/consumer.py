import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import ChatUser, Message


class ChatConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.user_code = self.scope['url_route']['kwargs']['user_code']
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

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sender = 'admin' if self.scope['user'].is_staff else 'user'

        chat_user, _ = ChatUser.objects.get_or_create(
            user_code=self.user_code
        )

        Message.objects.create(
            chat_user=chat_user,
            sender=sender,
            message=message
        )

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                'sender': sender,

            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event['message'],
            "sender": event['sender']
        }))


