from django.contrib import admin
from django.contrib.gis import admin as gis_admin
from .models import Location
from leaflet.admin import LeafletGeoAdmin


from .models import Branches

# Përdorni LeafletGeoAdmin për shfaqjen në hartë
@admin.register(Branches)
class BranchesAdmin(LeafletGeoAdmin):
    list_display = ('name', 'city', 'user', 'point')  # Të shfaqen disa fusha
    search_fields = ('name', 'city')  # Mund të kërkoni për emër dhe qytet



class MyLocationAdmin(LeafletGeoAdmin):
    list_display = ('name', 'point')
    search_fields = ('name', 'city', 'branch')  # Lejo kërkimin për emrin, qytetin dhe degën
    list_filter = ('city', 'branch')  # Filtrim sipas qytetit dhe degës

    # Kufizo rezultatet në admin sipas përdoruesit të loguar
    # def get_queryset(self, request):
        # queryset = super().get_queryset(request)
        #Kontrollo nëse përdoruesi është superuser
        # if request.user.is_superuser:
            # return queryset  # Përdoruesi superuser sheh të dhënat e të gjithë përdoruesve
        # else:
            #Përdoruesit e tjerë shohin vetëm të dhënat që janë të lidhura me ta
            # return queryset.filter(user=request.user)

admin.site.register(Location, MyLocationAdmin)


