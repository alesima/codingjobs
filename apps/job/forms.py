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
            }),
            'category': forms.Select(attrs={
                'v-model': 'form.category'
            }),
            'application_link': forms.TextInput(
                attrs={
                    'class': 'input',
                    'v-model': 'form.application_link'
                }
            ),
            'company_name': forms.TextInput(
                attrs={
                    'class': 'input',
                    'v-model': 'form.company_name'
                }
            ),
            'company_hq': forms.TextInput(
                attrs={
                    'class': 'input',
                    'v-model': 'form.company_hq'
                }
            ),
            'company_logo': forms.FileInput(attrs={
                'class': 'is-hidden',
                'style': 'cursor: pointer'
            }),
            'company_website': forms.TextInput(
                attrs={
                    'class': 'input',
                    'v-model': 'form.company_website'
                }
            ),
            'company_email': forms.TextInput(
                attrs={
                    'class': 'input',
                    'v-model': 'form.company_email'
                }
            ),
            'company_description': SummernoteWidget(attrs={
                'v-model': 'form.company_description'
            }),
        }
        fields = ('title', 'description', 'category', 'skills', 'is_worldwide',
                  'job_type', 'application_link', 'company_name', 'company_hq', 'company_website', 'company_logo', 'company_email', 'company_description')


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience']
