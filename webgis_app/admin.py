from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin as gis_admin
from .models import Location
from leaflet.admin import LeafletGeoAdmin

class MyLocationAdmin(LeafletGeoAdmin):
    list_display = ('name', 'point')

admin.site.register(Location, MyLocationAdmin)