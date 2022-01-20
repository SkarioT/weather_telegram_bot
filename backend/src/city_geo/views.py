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
        city = CreateCitySerializator(data=request.data)
        if city.is_valid():
            city.save()
        return Response(status=201)