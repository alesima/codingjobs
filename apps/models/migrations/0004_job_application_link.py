# Generated by Django 4.1.3 on 2022-11-06 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_alter_job_is_worldwide'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='application_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]