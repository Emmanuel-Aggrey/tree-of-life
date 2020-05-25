# Generated by Django 3.0.6 on 2020-05-25 00:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0012_auto_20200525_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
