# Generated by Django 2.2.10 on 2020-06-12 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0017_auto_20200609_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='every_one',
        ),
    ]
