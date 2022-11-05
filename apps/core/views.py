from django.shortcuts import render
from apps.models.Job import Job


def index(request):
    jobs = Job.objects.order_by('-created_at')[:3]
    return render(request, 'home/index.html', {'jobs': jobs})
