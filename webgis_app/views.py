from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index_view(request):
    return render(request, 'webgis_app/index.html')  # Kthe template 'index.html'
    
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Location
from django.views.decorators.csrf import csrf_exempt
import json

    

def locations_geojson(request):
    locations = Location.objects.all()
    geojson_data = {
        "type": "FeatureCollection",
        "features": []
    }

    for location in locations:
        geojson_data["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [location.point.x, location.point.y]
            },
            "properties": {
                "name": location.name,
                "city": location.city,
                "branch": location.branch
            }
        })

    return JsonResponse(geojson_data)
    
    
@csrf_exempt
def add_location(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            city = data.get('city', '')  # Merr qytetin, ose '' nëse mungon
            branch = data.get('branch', '')  # Merr degën, ose '' nëse mungon
            longitude = data.get('longitude')
            latitude = data.get('latitude')

            if name and longitude and latitude:
                location = Location.objects.create(
                    name=name,
                    city=city,
                    branch=branch,
                    point=f'POINT({longitude} {latitude})'
                )
                return JsonResponse({"status": "success", "id": location.id}, status=201)

            return JsonResponse({"status": "error", "message": "Invalid data"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)
