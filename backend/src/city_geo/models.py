from django.db import models

# Create your models here.

class City_Geo (models.Model):
    geo_name =models.CharField(verbose_name="City Name",max_length=100)
    geo_lat=models.CharField(verbose_name="Geo lat",max_length=20)
    geo_lon=models.CharField(verbose_name="Geo lon",max_length=20)
    geo_description =models.CharField(verbose_name="Description",max_length=200)

    def __str__(self):
        return self.geo_name +" "+ self.geo_lat+' '+self.geo_lon+' '+self.geo_description