# Generated by Django 2.1.3 on 2019-04-18 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0007_assignment_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='check',
        ),
        migrations.AddField(
            model_name='studentdoassignment',
            name='check',
            field=models.BooleanField(default=False),
        ),
    ]
