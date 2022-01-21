from sys import api_version
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City_Geo
from .serializator import *







# Create your views here.
        
class City(APIView):
    def get(self,*args, **kwargs):
        all_city = City_Geo.objects.all()
        serialized_city = CitySerializator(all_city,many=True)
        return Response(serialized_city.data)


class NewCity(APIView):
    def post(self,request):
        print(request.data)
        city = CreateCitySerializator(data=request.data)
        #проверяю данные на валидность, если не валидны то метод create в CreateCitySerializator не вызовиться
        if city.is_valid():
            city.save()
            return Response(status=201)
        else:
            print("данные не валидны")
            return Response(f"invalid request {request.data}",status=400)
            
#проверю есть ли в БД уже запись по переданному к АПИ городу
class CityCheck(APIView):
    def post(self,request):
        # print("request.data: ",request.data,"\n_______")
        city_check = City_Geo.objects.filter(geo_name=request.data.get("geo_name"))
        if city_check.exists() :
            serialized_city = CitySerializator(city_check,many=True)
            # print("serialized_city: ",serialized_city)
            return Response(data=serialized_city.data)
        else:
            # print("данные не валидны")
            return Response(f"invalid request {request.data}",status=400)