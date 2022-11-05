from django.contrib.auth.models import User
from django.db import models
from .Application import Application

class ConversationMessage(models.Model):
    application = models.ForeignKey(
        Application, related_name='conversationmessages', on_delete=models.CASCADE)
    content = models.TextField()
    created_by = models.ForeignKey(
        User, related_name='conversationmessages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
