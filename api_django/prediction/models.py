from django.db import models

# Create your models here.


class Bike(models.Model):
    Hour = models.IntegerField()
    Temperature = models.FloatField()
    Humidity = models.IntegerField()
    WS = models.FloatField()                # Wind speed
    Visibility = models.IntegerField()
    SR = models.FloatField()                  # Solar Radiation
    Rainfall = models.FloatField()
    Snowfall = models.FloatField()
    Holiday = models.FloatField()
    Seasons = models.FloatField()
    WD = models.IntegerField()              # working day
    Month = models.IntegerField()
    RBC = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
