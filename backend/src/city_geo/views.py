from sys import api_version
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City_Geo,City_weather
from .serializator import *







# Create your views here.
        
class City(APIView):
    def get(self,*args, **kwargs):
        all_city = City_Geo.objects.all()
        # print("all_city",all_city)
        serialized_city = CitySerializator(all_city,many=True)
        return Response(serialized_city.data)


class NewCity(APIView):
    def post(self,request):
        print(request.data)
        city = CreateCitySerializator(data=request.data)
        #проверяю данные на валидность, если не валидны то метод create в CreateCitySerializator не вызовиться
        if city.is_valid():
            #при сохранении
            city.save()
            return Response(status=201)
        else:
            print("данные не валидны")
            return Response(f"invalid request {request.data}",status=400)
            
#проверю есть ли в БД уже такая запись, если есть - возвращаю её значение
class CityCheck(APIView):
    def post(self,request):
        print("request.data: ",request.data,"\n_______")
        serialized_city_req = CityCheckSerializator(data=request.data)
        #проверяю валидацию
        # print(serialized_city_req.is_valid())
        if serialized_city_req.is_valid():
            print("данные валидны")
            valid_geo_name=request.data.get("geo_name")
            city_check = City_Geo.objects.filter(geo_name=valid_geo_name)
            if city_check.exists() :
                print("Данные валидны и есть в базе\n\n\n")   
                city_weather_check = City_weather.objects.filter(city__geo_name=valid_geo_name)
                if city_weather_check.exists():
                    print("В базе есть информация по погоде для указанного города")
                    ser_city_weather = CityCheckWeatherSerializator(city_weather_check,many=True)
                    # данно реализации я возвращаю информацию по погоде для города
                    return Response(data=ser_city_weather.data)

                    # отдать информацию и по погоде
                    
                else:
                    print("Для города нет информации по погоде")
                    pass
                    #запросить актуальную информацию по погоде или вернуть что инфы нет и пусть запрашивает get_weather_api?

                serialized_city = CitySerializator(city_check,many=True)
                return Response(data=serialized_city.data)
            else:
                return Response(f"Not Found city {valid_geo_name} in DB",status=400)
        else:
            print("данные не валидны")
            return Response(serialized_city_req.errors,status=400)