
from venv import create
from django.forms import fields
from rest_framework import serializers
from .models import City_Geo, City_weather

#добавление данных по городу через API
class CreateCitySerializator(serializers.ModelSerializer):
    class Meta:
        model = City_Geo
        fields = '__all__'
    
    def create(self, validated_data):
        print("validated_data:",validated_data)
        #что бы уменьшить кол-во обрабочиков, сделал через get_or_create
        #по умолчанию, подразумевается, что города(название) в базе будут уникальными, соответствено, при запросе на добавление, 
        #если город уже есть - просто верну его обратно, если нет - создам
        city,create = City_Geo.objects.get_or_create(
            geo_name=validated_data.get('geo_name',None),
            geo_lat=validated_data.get('geo_lat',None),
            geo_lon=validated_data.get('geo_lon',None),
            geo_description=validated_data.get('geo_description',None),
        )
        print("ser_city",city)
        return city

#добавление данных по погоде для города через API
class CreateCityWeatherSerializator(serializers.ModelSerializer):
    class Meta:
        model = City_weather
        fields = [
                'weather_cur_date',
                'weather_temp',
                'weather_azuzhenie',
                'weather_condition',
                'weather_wind_speed',
                'weather_wind_gust',
                'weather_wind_dir',
                'weather_pressure_mm',
                'weather_humidity',
                'city'
                ]
    
    def create(self, validated_data):
        # print("validated_data:",validated_data)
        #что бы уменьшить кол-во обрабочиков, сделал через get_or_create
        #по умолчанию, подразумевается, что ПОГОДА ДЛЯ ГОРОДА в базе будут уникальными, соответствено, при запросе на добавление, 
        #если ПОГОДА ДЛЯ ГОРОДА уже есть - просто верну его обратно, если нет - создам
        city,create = City_weather.objects.get_or_create(
            weather_cur_date=validated_data.get('weather_cur_date',None),
            weather_temp=validated_data.get('weather_temp',None),
            weather_azuzhenie=validated_data.get('weather_azuzhenie',None),
            weather_condition=validated_data.get('weather_condition',None),
            weather_wind_speed=validated_data.get('weather_wind_speed',None),
            weather_wind_gust=validated_data.get('weather_wind_gust',None),
            weather_wind_dir=validated_data.get('weather_wind_dir',None),
            weather_pressure_mm=validated_data.get('weather_pressure_mm',None),
            weather_humidity=validated_data.get('weather_humidity',None),
            city=validated_data.get('city',None),
        )
        return city



#класс требуется для первичной валидации запроса по имени города
class CityCheckSerializator(serializers.ModelSerializer):

    class Meta:
        model = City_Geo
        fields = ['geo_name']

#сериализатор для вывода всей информации из таблицы/модели City_weather
class CityCheckWeatherSerializator(serializers.ModelSerializer):
    class Meta:
        model = City_weather
        fields = '__all__'


#получение данных по апи.
#Как для получения всех значений, так и для вывода результата поиска по  имени
class CitySerializator(serializers.ModelSerializer):
    weather = CityCheckWeatherSerializator(many=True,read_only=True)
    class Meta:
        model = City_Geo
        fields = ['pk','geo_name','geo_lat','geo_lon','geo_description','weather'] 
        


