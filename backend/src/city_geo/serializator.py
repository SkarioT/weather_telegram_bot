
from rest_framework import serializers
from .models import City_Geo

#добавление данных по апи
class CreateCitySerializator(serializers.ModelSerializer):
    class Meta:
        model = City_Geo
        fields = ['geo_name','geo_lat','geo_lon','geo_description']
    
    def create(self, validated_data):
        city = City_Geo.objects.get_or_create(
            geo_name=validated_data.get('geo_name',None),
            geo_lat=validated_data.get('geo_lat',None),
            geo_lon=validated_data.get('geo_lon',None),
            geo_description=validated_data.get('geo_description',None),
        )
        return city

#получение данных по апи
class CitySerializator(serializers.ModelSerializer):
    # my_field = serializers.SerializerMethodField('my_custom_field')
    # def my_custom_field(self,City_Geo):
    #     return  "Содержимое кастомного вывода" 
    class Meta:
        model = City_Geo
        fields = ['pk','geo_name','geo_lat','geo_lon','geo_description']#,'my_field']