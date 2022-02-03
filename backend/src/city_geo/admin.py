from django.contrib import admin
from . import models
# Register your models here.


class CityAdmin(admin.ModelAdmin):
    list_display=['pk','geo_name','geo_lat','geo_lon','geo_description']
    list_editable=['geo_name','geo_lat','geo_lon','geo_description']



admin.site.register(models.City_Geo)
admin.site.register(models.City_weather)
