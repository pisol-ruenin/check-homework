# Generated by Django 2.1.3 on 2019-04-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0003_auto_20190415_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='check',
            field=models.BooleanField(default=False),
        ),
    ]
