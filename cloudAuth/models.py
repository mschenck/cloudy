from django.db import models
from libcloud.providers import DRIVERS

class Credential(models.Model):
    services = []
    
    for driver in DRIVERS:
        services.append( (driver, DRIVERS[driver][1]) )

    service_provider = models.IntegerField(choices=services)
    api_id = models.CharField(max_length=200)
    api_secret = models.CharField(max_length=200,blank=True)

