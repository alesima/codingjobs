# Generated by Django 4.1.3 on 2022-11-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_alter_job_is_worldwide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='is_worldwide',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No')], default='y', max_length=1),
        ),
    ]
