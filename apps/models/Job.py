from django.contrib.auth.models import User
from django.db import models
from .enums import StatusEnum, BooleanEnums, CategoryEnum, JobTypeEnum


class Job(models.Model):

    status = models.CharField(
        max_length=20, choices=StatusEnum.choices(), default=StatusEnum.get_value('ACTIVE'))
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=50, choices=CategoryEnum.choices())
    skills = models.TextField(blank=True, null=True)
    is_worldwide = models.CharField(
        max_length=1, choices=BooleanEnums.choices(), default=BooleanEnums.get_value('YES'))
    job_type = models.CharField(max_length=20, choices=JobTypeEnum.choices())
    application_link = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255)
    company_hq = models.CharField(max_length=255)
    company_website = models.CharField(max_length=255)
    company_logo = models.FileField(upload_to='logos/')
    company_email = models.EmailField(max_length=255)
    company_description = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(
        User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "{} | {}".format(self.title, self.company_name)
