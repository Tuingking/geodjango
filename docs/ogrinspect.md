Ogrinspect
---
The ogrinspect command introspects a GDAL-supported vector data source (e.g., a shapefile) and generates a model definition and LayerMapping dictionary automatically.

Example from geodjango tutorial
---
source: [geodjango tutorial](https://docs.djangoproject.com/el/2.1/ref/contrib/gis/tutorial/)

```sh
python manage.py ogrinspect world/data/TM_WORLD_BORDERS-0.3.shp WorldBorder --srid=4326 --mapping --multi
```

result
```py
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class WorldBorder(models.Model):
    fips = models.CharField(max_length=2)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    un = models.IntegerField()
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.BigIntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)


# Auto-generated `LayerMapping` dictionary for WorldBorder model
worldborder_mapping = {
    'fips': 'FIPS',
    'iso2': 'ISO2',
    'iso3': 'ISO3',
    'un': 'UN',
    'name': 'NAME',
    'area': 'AREA',
    'pop2005': 'POP2005',
    'region': 'REGION',
    'subregion': 'SUBREGION',
    'lon': 'LON',
    'lat': 'LAT',
    'geom': 'MULTIPOLYGON',
}
```

Example #2 using INDONESIA KOTA SHP
---
Inspect .shp file using command below
```sh
python manage.py ogrinspect /Users/sky/Downloads/SHAPEFILE/SHP_Indonesia_Kota/IND_KOT_point.shp IndonesiaKota --srid=4326 --mapping --multi
```

result:
```py
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class IndonesiaKota(models.Model):
    nama = models.CharField(max_length=25)
    kode_unsur = models.BigIntegerField()
    geom = models.MultiPointField(srid=4326)


# Auto-generated `LayerMapping` dictionary for IndonesiaKota model
indonesiakota_mapping = {
    'nama': 'Nama',
    'kode_unsur': 'Kode_unsur',
    'geom': 'MULTIPOINT25D',
}
```

Example #3 Kecamatan Indonesia (PARTIAL)
python manage.py ogrinspect /Users/sky/Downloads/SHAPEFILE/mygeodata/Kecamatan-polygon.shp KecamatanBorder --srid=4326 --mapping --multi

Example #4 Indonesia Administrative Lv.4 (Kelurahan/Desa) (COMPLETE)
python manage.py ogrinspect gadm36_IDN_4.shp KelurahanBorder --srid=4326 --mapping --multi