from django import forms
from django_summernote.widgets import SummernoteWidget
from apps.models.Job import Job
from apps.models.Application import Application


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'input',
                    'v-model': 'form.title'
                }
            ),
            'description': SummernoteWidget(attrs={
                'v-model': 'form.description'
            })
        }
        fields = ('title', 'description', 'category', 'skills', 'is_worldwide',
                  'job_type', 'company_name', 'company_hq', 'company_website', 'company_logo', 'company_email', 'company_description')


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience']
