from django.contrib.auth.models import User
from django.db import models
from .Job import Job


class Application(models.Model):
    job = models.ForeignKey(
        Job, related_name='applications', on_delete=models.CASCADE)
    content = models.TextField()
    experience = models.TextField()

    created_by = models.ForeignKey(
        User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "Job: %s - Cadidate: %s" % (self.job, self.created_by)
