# Generated by Django 4.1.2 on 2022-10-16 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_alter_job_company_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('archived', 'Archived'), ('employed', 'Employed')], default='active', max_length=20),
        ),
    ]
