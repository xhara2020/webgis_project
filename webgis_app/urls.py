# webgis_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index_view'),  # URL për faqen kryesore
   
]