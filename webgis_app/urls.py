# webgis_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import locations_geojson
from .views import add_location
from .views import custom_logout
from .views import geojson_view

urlpatterns = [
    path('', views.index_view, name='index_view'),  # URL për faqen kryesore
    path('geojson/', views.geojson_view, name='geojson_view'),  # URL për faqen GeoJSON
    path('api/locations/', locations_geojson, name='locations_geojson'),
    path('api/add_location/', add_location, name='add_location'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Faqja e login-it
    #path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout
    #path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('logout/', custom_logout, name='logout'),
    path('api/locations/<str:location_name>/', views.location_by_name, name='location_by_name'),
    

   
]