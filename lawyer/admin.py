from django.contrib import admin
from .models import Lawyer, Articles
from django.contrib.gis import admin as geoAdmin
from leaflet.admin import LeafletGeoAdmin

# admin.site.register(Category)
# admin.site.register(Law)

class LawyerAdmin(geoAdmin.OSMGeoAdmin):
    list_display = ('id', 'phone','date')
    search_fields = ['phone',]
    ordering = ['id']
    list_filter = ('id', 'phone')
    default_lon =  4099417.64331
    default_lat = -141960.53582
    default_zoom = 14
    map_info = True
    map_width = 700
    map_height = 500

admin.site.register(Lawyer, LawyerAdmin)
admin.site.register(Articles)