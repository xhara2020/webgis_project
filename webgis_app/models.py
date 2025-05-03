from django.db import models

# Create your models here.
from django.contrib.gis.db import models

from django.contrib.auth.models import User
from django.contrib.gis.db import models



class Branches(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Fusha name tani është unik
    city = models.CharField(max_length=100, blank=True, null=True)  # Qyteti
    point = models.PointField()  # Koordinatat
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Lidhja me user-in
    user_name = models.CharField(max_length=150, blank=True, null=True)  # Ruaj emrin e user-it si tekst
    def __str__(self):
        return f"{self.name} - {self.city} )"


class Location(models.Model):
    TYPE_CLIENT_CHOICES = [
        ('biznes', 'Biznes'),
        ('individ', 'Individ'),
    ]

    name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    type_client = models.CharField(
        max_length=100,
        choices=TYPE_CLIENT_CHOICES,
        default='individ'  # Vlerë default që mund të ndryshohet në formë
    )
    point = models.PointField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.city} ({self.branch})"



