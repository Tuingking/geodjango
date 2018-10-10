from django.contrib.gis.geos import Point
from indonesia.models import KelurahanBorder

# QUERY SPATIAL TO FIND POINT IN BOUNDARIES

# Point(lon, lat)
x = 'POINT(96.0996003 4.1845603)'

106.796126
-6.1908949

WISMA_76 = Point(106.796126, -6.1908949)   # kemanggisan
WISMA_77 = Point(106.797167, -6.19045)
MENARA_SUPRA = Point(106.79834, -6.19093)  # slipi
BAKSO_KUMIS = Point(106.799477, -6.1907734)
SMK = Point(106.7977742, -6.1913169)
CITICON = Point(106.7956465, -6.1926838)

point_wkt = CITICON
qs = KelurahanBorder.objects.filter(geom__contains=point_wkt)
"""
spatial lookups:
<geom>__contains
<geom>__intersects

For more about spatial queries go to
https://docs.djangoproject.com/en/2.1/ref/contrib/gis/geoquerysets/#spatial-lookups

lon = 106.796126 # kemanggisan
lon = 106.797126 # slipi
beda +0.002200 longitude 
"""

print(qs.query)

# OPEN JSON AND BULK INSERT-----------
import json

json_data = open('indonesia/data/testing/kelurahan_jakarta.json')
json_load = json.load(json_data)
kelurahan_jakarta = json_load['jakarta']

kelurahan_bulk = []
for kelurahan in kelurahan_jakarta:
    kelurahan_bulk.append(
        KelurahanBorder(
            gid_0=kelurahan['gid_0'],
            name_0=kelurahan['name_0'],
            gid_1=kelurahan['gid_1'],
            name_1=kelurahan['name_1'],
            gid_2=kelurahan['gid_2'],
            name_2=kelurahan['name_2'],
            gid_3=kelurahan['gid_3'],
            name_3=kelurahan['name_3'],
            gid_4=kelurahan['gid_4'],
            name_4=kelurahan['name_4'],
            varname_4=kelurahan['varname_4'],
            type_4=kelurahan['type_4'],
            engtype_4=kelurahan['engtype_4'],
            cc_4=kelurahan['cc_4'],
            geom=kelurahan['geom'],
        )
    )

KelurahanBorder.objects.bulk_create(kelurahan_bulk)
