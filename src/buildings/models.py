from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from geodjango import typing as typ

from indonesia import utils as iu

COORDINATE = Point(0, 0)
JAKARTA = Point(-5.7759362, 106.1174984)
JAKARTA = 'POINT(-5.7773029 106.1175071)'

LONGITUDE_DIFF = 0.002200


class Buildings(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    coord_google = models.PointField(default=COORDINATE)  # for insert
    coord_osm = models.PointField(default=COORDINATE)

    class Meta:
        db_table = 'buildings'
        ordering = ['name']

    def set_coord_osm(self):
        lon_google = self.coord_google.x
        lat_google = self.coord_google.y

        lon_osm = lon_google + LONGITUDE_DIFF
        self.coord_osm = Point(lon_osm, lat_google)

    @property
    def coordinate(self):
        return self.coord_osm

    def save(self, *args, **kwargs):
        self.set_coord_osm()
        super().save(*args, **kwargs)

    @property
    def kelurahan(self) -> typ.KelurahanBorder:
        kelurahan = iu.get_kelurahan_by_coordinate(self.coord_osm)

        return kelurahan

    def __str__(self):
        return self.name
