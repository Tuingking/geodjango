from django.contrib.gis import admin
from .models import Buildings


class BuildingAdmin(admin.OSMGeoAdmin):
    """ OSMGeoAdmin = Open Street Map """

    list_display = ['name', 'address', 'coord_google', 'coord_osm']
    search_fields = ['name', 'address']

    list_filter = ['name']


admin.site.register(Buildings, BuildingAdmin)
# admin.site.register(IndonesiaBorder, admin.GeoModelAdmin)
