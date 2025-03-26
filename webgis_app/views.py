from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index_view(request):
    return render(request, 'webgis_app/index.html')  # Kthe template 'index.html'



def geojson_view(request):
    return render(request, 'webgis_app/geojson-layer.html')  # Kthe template 'index.html'

    
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Location
from django.views.decorators.csrf import csrf_exempt
import json

    

def locations_geojson(request):
    #locations = Location.objects.all()
    locations = Location.objects.filter(user=request.user)  # Filtrim sipas userit
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
                    point=f'POINT({longitude} {latitude})',
                    user=request.user,
                    user_name=request.user.username,  # Ruaj emrin e user-it
                )
                return JsonResponse({"status": "success", "id": location.id}, status=201)

            return JsonResponse({"status": "error", "message": "Invalid data"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    
    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)


from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    messages.success(request, "U çregjistruat me sukses!")
    logout(request)
    return redirect('index_view')
    

from django.http import JsonResponse
from .models import Location
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def location_by_name(request, location_name):
    if request.method == 'GET':  # Sigurohuni që po pranon vetëm GET
        try:
            # Gjejmë pikën me emrin e dhënë
            location = Location.objects.get(name=location_name)
            
            # Krijojmë të dhënat GeoJSON për këtë pikë
            geojson_data = {
                "type": "FeatureCollection",
                "features": [{
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
                }]
            }
            return JsonResponse(geojson_data, safe=False)
        
        except Location.DoesNotExist:
            return JsonResponse({"error": "Pika me emrin e dhënë nuk u gjet"}, status=404)
    
   
    elif request.method == 'DELETE':
        print(f"Po përpiqemi të fshijmë pikën me emrin: {location_name}")  # Mesazh debug
        try:
            location = Location.objects.get(name=location_name)
            location.delete()
            print(f"Pika me emrin {location_name} u fshi me sukses.")  # Mesazh për sukses
            return JsonResponse({"message": "Pika u fshi me sukses"}, status=200)
        except Location.DoesNotExist:
            print(f"Pika me emrin {location_name} nuk u gjet.")  # Mesazh për gabim
            return JsonResponse({"error": "Pika me emrin e dhënë nuk u gjet"}, status=404)
        except Exception as e:
            print(f"Gabim gjatë fshirjes: {e}")  # Mesazh për çdo gabim të mundshëm
            return JsonResponse({"error": f"Gabim gjatë fshirjes: {e}"}, status=500)
    
    return JsonResponse({"error": "Metoda jo e lejuar"}, status=405)



