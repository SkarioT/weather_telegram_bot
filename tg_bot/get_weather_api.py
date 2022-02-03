import requests
import json
import datetime
from yandex_map_api import get_geo_point
from auth_data import api_key_headers,server_address

def get_weather(city):
    
    #вызываю функцию, получающую из названия его координаты
    req_city_geo = get_geo_point(city)
    if req_city_geo == 0:
        return f"Неудалость найти город {city}"
    lon=req_city_geo[0]
    lat=req_city_geo[1]
    city_name =req_city_geo[2]
    city_description =req_city_geo[3]
    weather=req_city_geo[4]
    geo_city_pk=req_city_geo[5]

    if len(weather) == 0:
        print("данных по погоде в базе нет, забирую их у яндекса")
        url=f"https://api.weather.yandex.ru/v2/informers?lat={lat}&lon={lon}&lang=ru_RU"
        req = requests.get(url=url,headers=api_key_headers)
        #сохроняю в файл json
        weather=req.json()


        weather_cur_date =datetime.datetime.fromtimestamp(weather.get("now"))
        # print(wether_cur_date)

        weather_temp ="Темература " + str(weather['fact']['temp'])
        # print(weather_temp)

        weather_azuzhenie = "Ощущается как "+str(weather['fact']['feels_like'])
        # print(weather_azuzhenie)
        
        weather_icon = weather['fact']['icon']
        # url_ico=f'https://yastatic.net/weather/i/icons/funky/dark/{weather_icon}.svg'

        condition_dict ={'clear':'ясно','partly-cloudy':'малооблачно','cloudy' : 'облачно с прояснениями','overcast' : 'пасмурно','drizzle' : 'морось','light-rain': 'небольшой дождь',
                    'rain': "дождь",'moderate-rain' : 'умеренно сильный дождь','heavy-rain': 'сильный дождь','continuous-heavy-rain' : 'длительный сильный дождь',
                    'showers' : 'ливень','wet-snow': 'дождь со снегом','light-snow': 'небольшой снег','snow' :'снег','snow-showers' : 'снегопад',
                    'hail' : 'град','thunderstorm' : 'гроза','thunderstorm-with-rain': 'дождь с грозой','thunderstorm-with-hail' : 'гроза с градом'}
        weather_condition = weather['fact']['condition']
        if weather_condition in condition_dict:
            weather_condition= condition_dict[weather_condition]
            # print(weather_condition)

        weather_wind_speed='Скорость ветра '+ str(weather['fact']['wind_speed'])+' м/с'
        # print(weather_wind_speed)

        weather_wind_gust='С порывами до '+ str(weather['fact']['wind_gust'])+' м/с'
        # print(weather_wind_gust)
        
        wind_dir_dict={'nw' : 'северо-западное',
                        'n' : 'северное',
                        'ne' : 'северо-восточное',
                        'e' : 'восточное',
                        'se' : 'юго-восточное',
                        's' : 'южное',
                        'sw' : 'юго-западное',
                        'w' : 'западное',
                        'с' : 'штиль'}
        weather_wind_dir = weather['fact']['wind_dir']
        
        if weather_wind_dir in wind_dir_dict:
            weather_wind_dir="Направление ветра - "+str(wind_dir_dict[weather_wind_dir])
        # print(weather_wind_dir)

        weather_pressure_mm='Атмосферное давление '+str(weather['fact']['pressure_mm'])+' мм рт. ст.'
        # print(weather_pressure_mm)
        
        weather_humidity = "Влажность воздуха "+str(weather['fact']['humidity'])+" %"
        # print(weather_humidity)
        
        url_create_weather_for_city = f"{server_address}/city_weather_create/"
        drf_create_weather_data = {
                "weather_cur_date": f"{weather_cur_date}",
                "weather_temp": f"{weather_temp}",
                "weather_azuzhenie": f"{weather_azuzhenie}",
                "weather_condition": f"{weather_condition}",
                "weather_wind_speed": f"{weather_wind_speed}",
                "weather_wind_gust": f"{weather_wind_gust}",
                "weather_wind_dir": f"{weather_wind_dir}",
                "weather_pressure_mm": f"{weather_pressure_mm}",
                "weather_humidity": f"{weather_humidity}",
                "city": f"{geo_city_pk}"
                }
        dfr_create_weather_req = requests.post(url_create_weather_for_city,data=drf_create_weather_data)
        print("Отправляю данные для создания информации по городу и получаю ответ:\n",dfr_create_weather_req.json())
        
        return city_name,city_description,weather_cur_date,weather_temp,weather_azuzhenie,weather_condition,weather_wind_speed,weather_wind_gust,weather_wind_dir,weather_pressure_mm,weather_humidity
    else:
        print("данные по погоде для города есть базе, возвращаю их")
        return city_name,city_description,weather