from django.contrib.auth.models import User
from django.db import models
from .enums import NotificationTypeEnum


class Notification(models.Model):
    to_user = models.ForeignKey(
        User, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(
        max_length=20, choices=NotificationTypeEnum.choices())
    is_read = models.BooleanField(default=False)
    extra_id = models.IntegerField(null=True, blank=True)
    created_by = models.ForeignKey(
        User, related_name='createnotifications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
