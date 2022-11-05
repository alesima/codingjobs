from django.contrib import admin

from apps.models.Job import Job
from apps.models.Application import Application

admin.site.register(Job)
admin.site.register(Application)