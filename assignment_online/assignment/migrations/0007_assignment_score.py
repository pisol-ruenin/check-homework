# Generated by Django 2.1.3 on 2019-04-15 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0006_auto_20190415_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='score',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]