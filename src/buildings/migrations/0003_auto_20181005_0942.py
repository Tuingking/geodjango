# Generated by Django 2.1.1 on 2018-10-05 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0002_buildings_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buildings',
            old_name='location',
            new_name='coordinate',
        ),
    ]
