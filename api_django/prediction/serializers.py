from rest_framework import serializers
from .models import Bike


class BikeSerializer(serializers.Serializer):
    Hour = serializers.IntegerField()
    Temperature = serializers.FloatField()
    Humidity = serializers.IntegerField()
    WS = serializers.FloatField()                # Wind speed
    Visibility = serializers.IntegerField()
    SR = serializers.FloatField()                  # Solar Radiation
    Rainfall = serializers.FloatField()
    Snowfall = serializers.FloatField()
    Holiday = serializers.FloatField()
    Seasons = serializers.FloatField()
    WD = serializers.IntegerField()              # Functioning day
    Month = serializers.IntegerField()
    RBC = serializers.FloatField(allow_null=True)

    def create(self, validated_data):
        """Create and return a new `Bike` instance, given the validated data."""
        return Bike.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """"Update and return an existing `House` instance, given the validated data."""
        instance.Hour = validated_data.get('Hour', instance.Hour)
        instance.Temperature = validated_data.get(
            'Temperature', instance.Temperature)
        instance.Humidity = validated_data.get('Humidity', instance.Humidity)
        instance.WS = validated_data.get('WS', instance.WS)
        instance.Visibility = validated_data.get(
            'Visibility', instance.Visibility)
        instance.SR = validated_data.get('SR', instance.SR)
        instance.Rainfall = validated_data.get('Rainfall', instance.Rainfall)
        instance.Snowfall = validated_data.get('Snowfall', instance.Snowfall)
        instance.Holiday = validated_data.get('Holiday', instance.Holiday)
        instance.Seasons = validated_data.get('Seasons', instance.Seasons)
        instance.WD = validated_data.get('WD', instance.WD)
        instance.Month = validated_data.get('Month', instance.Month)
        instance.save()
        return instance
