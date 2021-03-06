# Generated by Django 3.0.6 on 2020-05-23 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20200523_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='interests',
            field=models.ManyToManyField(help_text='available topics', related_name='interested_students', to='classroom.Subject', verbose_name='available topic(s)'),
        ),
    ]
