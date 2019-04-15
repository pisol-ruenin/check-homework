# Generated by Django 2.1.3 on 2019-04-14 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20190414_1740'),
        ('assignment', '0002_auto_20190414_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMatchingScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_no', models.IntegerField()),
                ('score', models.FloatField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentOpenEndedScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Question')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.Student')),
            ],
        ),
        migrations.RenameModel(
            old_name='StudentScore',
            new_name='StudentChoiceScore',
        ),
        migrations.AlterUniqueTogether(
            name='studentopenendedscore',
            unique_together={('student', 'question')},
        ),
        migrations.AlterUniqueTogether(
            name='studentmatchingscore',
            unique_together={('student', 'question', 'item_no')},
        ),
    ]
