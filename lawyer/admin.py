from django.contrib import admin
from .models import Lawyer
from django.contrib.gis import admin as geoAdmin
from leaflet.admin import LeafletGeoAdmin


class LawyerAdmin(geoAdmin.OSMGeoAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone','date')
    search_fields = ['first_name', 'phone']
    ordering = ['id']
    list_filter = ('id', 'phone')
    default_lon =  -0.561360
    default_lat = 37.050093
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500

admin.site.register(Lawyer, LawyerAdmin)