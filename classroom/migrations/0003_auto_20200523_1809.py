# Generated by Django 3.0.6 on 2020-05-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_user_can_participate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChurchGroups',
            new_name='ChurchGroup',
        ),
        migrations.AlterField(
            model_name='subject',
            name='color',
            field=models.CharField(default='#007bff', editable=False, max_length=7),
        ),
    ]
