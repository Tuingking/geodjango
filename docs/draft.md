
## Postgres
---
docker run --name docker-postgres -e POSTGRES_PASSWORD=password -d xwork

docker run --name postgis -e POSTGRES_PASSWORD=password -d mdillon/postgis

docker run -it --link postgis:postgres --rm postgres \
    sh -c 'exec psql -h "$POSTGRES_PORT_5432_TCP_ADDR" -p "$POSTGRES_PORT_5432_TCP_PORT" -U postgres'

docker run -it --link postgis:postgres --rm postgres \
    sh -c 'exec psql -h postgres -p 5432 -U root'
---
Ini yang jalan

docker run -p 5432:5432 --name postgis -e POSTGRES_PASSWORD=password \
  -e POSTGRES_USER=root -e POSTGRES_DB=geodjango2 -d mdillon/postgis

docker exec -it postgis bash -l 

psql -h localhost -p 5432 -U root -d geodjango2

Comand:
---
\l              : show databases
\c <database>   : use database
\d              : show tables

Query:
---
CREATE DATABASE xwork;

## ESRI Shapefile
---
The **shapefile** format is a popular geospatial vector data format for geographic information system (GIS) software.

Example shapefile:
```sh
wget http://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip
```

The world borders ZIP file contains a set of data files collectively known as an ESRI Shapefile, one of the most popular geospatial data formats. When unzipped, the world borders dataset includes files with the following extensions:

- .shp: Holds the vector data for the world borders geometries.
- .shx: Spatial index file for geometries stored in the .shp.
- .dbf: Database file for holding non-geometric attribute data (e.g., integer and character fields).
- .prj: Contains the spatial reference information for the geographic data stored in the shapefile.

## GDAL
---
Install GDAL on Mac
```sh
brew install gdal --HEAD
```

The GDAL **ogrinfo** utility allows examining the metadata of shapefiles or other vector data sources:
```sh
$ ogrinfo TM_WORLD_BORDERS-0.3.shp
```

convert .shp to JSON
```sh
$ ogr2ogr -f GeoJSON -t_srs crs:84 output.geojson TM_WORLD_BORDERS-0.3.shp
```

**ogrinfo** tells us that the shapefile has one layer, and that this layer contains polygon data. To find out more, we'll specify the layer name and use the -so option to get only the important summary information:
```sh
$ ogrinfo -so world/data/TM_WORLD_BORDERS-0.3.shp TM_WORLD_BORDERS-0.3
INFO: Open of `world/data/TM_WORLD_BORDERS-0.3.shp'
      using driver `ESRI Shapefile' successful.

Layer name: TM_WORLD_BORDERS-0.3                                    =>  lyr = ds[0]
Geometry: Polygon                                                   =>  lyr.geom_type
Feature Count: 246                                                  =>  len(lyr)
Extent: (-180.000000, -90.000000) - (180.000000, 83.623596)         =>  lyr.extent
Layer SRS WKT:                                                      =>  lyr.srs
GEOGCS["GCS_WGS_1984",
    DATUM["WGS_1984",
        SPHEROID["WGS_1984",6378137.0,298.257223563]],
    PRIMEM["Greenwich",0.0],
    UNIT["Degree",0.0174532925199433]]
FIPS: String (2.0)                       =>  lyr.fields / lyr.field_types
ISO2: String (2.0)
ISO3: String (3.0)
UN: Integer (3.0)
NAME: String (50.0)
AREA: Integer (7.0)
POP2005: Integer (10.0)
REGION: Integer (3.0)
SUBREGION: Integer (3.0)
LON: Real (8.3)
LAT: Real (7.3)
```
This detailed summary information tells us the number of features in the layer (246), the geographic bounds of the data, the spatial reference system ("SRS WKT"), as well as type information for each attribute field
**FIPS**: String (2.0) indicates that the FIPS character field has a maximum length of 2. Similarly
**LON**: Real (8.3) is a floating-point field that holds a maximum of 8 digits up to three decimal places.

Ogrinspect
---
The ogrinspect command introspects a GDAL-supported vector data source (e.g., a shapefile) and generates a model definition and LayerMapping dictionary automatically.

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


A few notes about the command-line options given above:

The --srid=4326 option sets the SRID for the geographic field.
The --mapping option tells ogrinspect to also generate a mapping dictionary for use with LayerMapping.
The --multi option is specified so that the geographic field is a MultiPolygonField instead of just a PolygonField.

References:
https://docs.djangoproject.com/id/2.1/ref/contrib/gis/tutorial/
https://docs.djangoproject.com/en/2.1/ref/contrib/gis/geos/