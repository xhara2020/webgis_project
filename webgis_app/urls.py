# webgis_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import locations_geojson
from .views import add_location

urlpatterns = [
    path('', views.index_view, name='index_view'),  # URL për faqen kryesore
    path('api/locations/', locations_geojson, name='locations_geojson'),
    path('api/add_location/', add_location, name='add_location'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Faqja e login-it
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout
   
]