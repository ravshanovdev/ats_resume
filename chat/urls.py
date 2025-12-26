from django.urls import path
from .views import StartChatView, ChatUserListView, MessageListView


urlpatterns = [
    path('start-chat/', StartChatView.as_view(), ),
    path('chat-user/', ChatUserListView.as_view(), ),
    path('message-list/<str:user_code>/', MessageListView.as_view(), ),
]

# user-7db9a24e22
# user-d4749899e4