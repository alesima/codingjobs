# Generated by Django 4.1.2 on 2022-10-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_job_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('archived', 'Archived'), ('active', 'Active'), ('employed', 'Employed')], default='active', max_length=20),
        ),
    ]
