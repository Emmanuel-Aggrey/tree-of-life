# Generated by Django 3.0.6 on 2020-05-24 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0007_auto_20200524_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='every_one',
        ),
        migrations.RemoveField(
            model_name='user',
            name='can_participate',
        ),
    ]
