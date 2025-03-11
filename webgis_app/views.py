from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'webgis_app/index.html')  # Kthe template 'index.html'
    
