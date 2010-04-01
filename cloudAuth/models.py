from django.db import models
from libcloud.providers import DRIVERS

class Credential(models.Model):
    services = DRIVERS.values()

    service_provider = models.CharField(max_length=200, choices=services)
    api_id = models.CharField(max_length=200)
    api_secret = models.CharField(max_length=200,blank=True)

