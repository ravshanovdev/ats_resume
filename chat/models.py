from django.db import models


class ChatUser(models.Model):
    user_code = models.CharField(max_length=155)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_code


class Message(models.Model):
    chat_user = models.ForeignKey(ChatUser, on_delete=models.CASCADE)
    sender = models.CharField(max_length=150)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.chat_user.user_code} -- {self.sender}"
