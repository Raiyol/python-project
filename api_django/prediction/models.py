from django.db import models

# Create your models here.


class House(models.Model):
    Hour = models.IntegerField()
    Temperature = models.FloatField()
    Humidity = models.IntegerField()
    WS = models.FloatField()                # Wind speed
    Visibility = models.IntegerField()
    DPT = models.FloatField()               # Dew point Temperature
    SR = models.FloatField                  # Solar Radiation
    Rainfall = models.FloatField()
    Snowfall = models.FloatField()
    Holiday = models.FloatField()
    Seasons = models.FloatField()
    FD = models.IntegerField()              # Functioning day
    Date = models.DateTimeField()

    class Meta:
        ordering = ['created']
