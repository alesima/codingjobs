from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from apps.models.Job import Job
from apps.models.UserProfile import UserProfile


def index(request):
    jobs = Job.objects.order_by('-created_at')[:3]
    return render(request, 'layouts/index.html', {'jobs': jobs})
