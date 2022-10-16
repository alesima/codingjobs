from django.urls import path

from .views import dashboard, view_dashboard_job, view_application

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('job/<int:job_id>', view_dashboard_job, name='view_dashboard_job'),
    path('application/<int:application_id>/',
         view_application, name='view_application'),
]
