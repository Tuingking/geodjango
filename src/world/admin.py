from django.contrib.gis import admin
from .models import WorldBorder


class WorldBorderAdmin(admin.OSMGeoAdmin):

    list_display = ['name', 'area', 'pop2005', 'fips', 'iso2',
                    'iso3', 'un', 'region', 'subregion', 'lon', 'lat']
    search_fields = ['name']

    # admin.site.register(WorldBorder, admin.GeoModelAdmin)
admin.site.register(WorldBorder, WorldBorderAdmin)
