from django.db import models
from django.contrib.gis.db import models as gis_models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    mail = models.EmailField(unique=True)
    password = models.TextField()
    avatar = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    socia_networks = models.JSONField(null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    account_status = models.BooleanField(default=True)
    last_activity_date = models.DateTimeField(auto_now=True)
    address = gis_models.PointField(geography=True, null=True, blank=True, srid=4326)

    def __str__(self):
        return f"{self.last_activity_date} {self.first_name} "
