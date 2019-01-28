from django.db import models

class Reading(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    temp = models.IntegerField()
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    
    wind_speed = models.IntegerField()
    
    weather = models.CharField(max_length=100)
