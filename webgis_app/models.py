from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    point = models.PointField()  # Kjo është një fushë gjeometrike për pikën
