import json

from django.views.decorators.http import require_http_methods
from django.db.models import Q
from django.http import JsonResponse

from .models import Job


@require_http_methods(["POST"])
def api_search(request):
    jobs_list = []
    data = json.loads(request.body)
    query = data['query']

    company_size = data['company_size']

    jobs = Job.objects.filter(Q(title__icontains=query) | Q(
        short_description__icontains=query) | Q(long_description__icontains=query) | Q(company_name__icontains=query) | Q(company_place__icontains=query))

    if company_size:
        jobs = jobs.filter(company_size=company_size)

    for job in jobs:
        obj = {
            'id': job.id,
            'title': job.title,
            'company_name': job.company_name,
            'url': '/jobs/%s' % job.id,
        }
        jobs_list.append(obj)

    return JsonResponse({'jobs': jobs_list})
