# Generated by Django 3.0.6 on 2020-05-24 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0006_quiz_can_participate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='can_participate',
        ),
        migrations.AddField(
            model_name='quiz',
            name='every_one',
            field=models.BooleanField(default=True, help_text='tick for every one untic to choose members'),
        ),
    ]
