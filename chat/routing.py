from django.urls import re_path
from . import consumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<user_code>[^/]+)/$", consumer.ChatConsumer.as_asgi()),
]
