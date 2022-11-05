from django import forms

from apps.models.Job import Job
from apps.models.Application import Application


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'short_description', 'long_description', 'company_name',
                  'company_address', 'company_zipcode', 'company_place', 'company_country', 'company_size']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience']
