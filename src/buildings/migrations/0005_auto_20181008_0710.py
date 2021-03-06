# Generated by Django 2.1.1 on 2018-10-08 07:10

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0004_auto_20181008_0625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buildings',
            old_name='coordinate',
            new_name='coord_google',
        ),
        migrations.AddField(
            model_name='buildings',
            name='coord_osm',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0, 0), srid=4326),
        ),
    ]
