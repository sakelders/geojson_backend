# Generated by Django 5.1.7 on 2025-03-22 13:06

import os, geojson
import django.contrib.gis.db.models.fields
from django.db import migrations, models
from django.conf import settings
from django.contrib.gis.geos import Polygon, MultiPolygon


def _create_polygon_from_data(polygon_data):
    return Polygon([(lon, lat) for lon, lat in polygon_data])

def load_initial_data(apps, schema_editor):
    Municipality = apps.get_model('rest_api', 'Municipality')

    initial_data_fname = os.path.join(settings.BASE_DIR, 'data', 'municipalities_nl.geojson')
    with open(initial_data_fname, 'r') as f:
        initial_data = geojson.load(f)

    municipalities = []
    for feature in initial_data.features:
        name = feature.properties['name']
        polygons = [_create_polygon_from_data(polygon_data) for polygon_data in feature.geometry.coordinates[0]]
        multi_polygon = MultiPolygon(polygons)

        municipalities.append(Municipality(name=name, polygons=multi_polygon))

    Municipality.objects.bulk_create(municipalities)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('polygons', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.RunPython(load_initial_data)
    ]
