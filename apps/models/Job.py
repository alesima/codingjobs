from django.contrib.auth.models import User
from django.db import models


class Job(models.Model):
    ACTIVE = 'active'
    EMPLOYED = 'employed'
    ARCHIVED = 'archived'

    CHOICES_STATUS = {
        (ACTIVE, 'Active'),
        (EMPLOYED, 'Employed'),
        (ARCHIVED, 'Archived'),
    }

    CHOICES_CATEGORY = {
        ('design', 'Design'),
        ('full-stack', 'Full-Stack Programming'),
        ('front-end', 'Front-end Programming'),
        ('back-end', 'Back-end Programming'),
        ('customer-support', 'Customer Support'),
        ('devops-sysadmin', 'DevOps and SysAdmin'),
        ('sales-marketing', 'Sales and Marketing'),
        ('management-finance', 'Management and Finance'),
        ('product', 'Product'),
        ('other', 'All Other Remote'),
    }

    YES = 'y'
    NO = 'n'

    CHOICES_YES_NO = {
        (YES, 'Yes'),
        (NO, 'No')
    }

    CHOICES_JOB_TYPE = {
        ('full-time', 'Full-Time'),
        ('contract', 'Contract'),
    }

    status = models.CharField(
        max_length=20, choices=CHOICES_STATUS, default=ACTIVE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=50, choices=CHOICES_CATEGORY)
    skills = models.TextField(blank=True, null=True)
    is_worldwide = models.CharField(
        max_length=1, choices=CHOICES_YES_NO, default=YES)
    job_type = models.CharField(max_length=20, choices=CHOICES_JOB_TYPE)
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
        return self.title
