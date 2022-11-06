from django.db.models import Q
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import JobSerializer
from apps.models.Job import Job


class JobsAPIView(ListAPIView):
    serializer_class = JobSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Job.objects.all()

        query = self.request.GET.get('query', None)
        company_size = self.request.GET.get('company_size', None)

        if query is not None:
            queryset = queryset.filter(Q(title__icontains=query) | Q(
                short_description__icontains=query) | Q(long_description__icontains=query) | Q(company_name__icontains=query) | Q(company_place__icontains=query))

        if company_size is not None:
            queryset = queryset.filter(company_size=company_size)

        return queryset
