from django.contrib.gis import admin
from .models import KelurahanBorder


class KelurahanBorderAdmin(admin.OSMGeoAdmin):
    """ OSMGeoAdmin = Open Street Map """

    list_display = ['gid_0', 'name_0', 'gid_1', 'name_1', 'gid_2', 'name_2', 'gid_3',
                    'name_3', 'gid_4', 'name_4', 'varname_4', 'type_4', 'engtype_4', 'cc_4']
    search_fields = ['name_1', 'name_2', 'name_3', 'name_4']

    list_filter = ['name_1']


admin.site.register(KelurahanBorder, KelurahanBorderAdmin)
# admin.site.register(IndonesiaBorder, admin.GeoModelAdmin)
