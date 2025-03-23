from django.db import models

# Create your models here.
from django.contrib.gis.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)  # Fusha për qytetin
    branch = models.CharField(max_length=100, blank=True, null=True)  # Fusha për degën
    point = models.PointField()  # Kjo është një fushë gjeometrike për pikën


from django.contrib.auth.models import AbstractUser, User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    branch = models.IntegerField()