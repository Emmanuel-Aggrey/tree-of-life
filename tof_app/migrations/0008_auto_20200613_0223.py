# Generated by Django 2.2.10 on 2020-06-13 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tof_app', '0007_article_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%d-%m-%Y/images'),
        ),
    ]
