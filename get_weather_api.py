import requests
import json
import datetime

def get_weather():
    api_key_headers={'X-Yandex-API-Key': '9fb7e010-21c2-4133-93ec-1a6b7f5d95ee'}
    url=f"https://api.weather.yandex.ru/v2/informers?lat=53.060277&lon=29.994478&lang=ru_RU"
    req = requests.get(url=url,headers=api_key_headers)
    json_string=req.json()
    with open('weather.json', 'w') as outfile:
        json.dump(json_string, outfile)



    with open('weather.json','r') as w:
        weather =json.load(w)
        wether_cur_date =str(datetime.datetime.fromtimestamp(weather.get("now")))
        print(wether_cur_date)

        weather_temp ="Темература " + str(weather['fact']['temp'])
        print(weather_temp)

        weather_azuzhenie = "Ощущается как "+str(weather['fact']['feels_like'])
        print(weather_azuzhenie)
        
        weather_icon = weather['fact']['icon']
        url_ico=f'https://yastatic.net/weather/i/icons/funky/dark/{weather_icon}.svg'

        condition_dict ={'clear':'ясно','partly-cloudy':'малооблачно','cloudy' : 'облачно с прояснениями','overcast' : 'пасмурно','drizzle' : 'морось','light-rain': 'небольшой дождь',
                    'rain': "дождь",'moderate-rain' : 'умеренно сильный дождь','heavy-rain': 'сильный дождь','continuous-heavy-rain' : 'длительный сильный дождь',
                    'showers' : 'ливень','wet-snow': 'дождь со снегом','light-snow': 'небольшой снег','snow' :'снег','snow-showers' : 'снегопад',
                    'hail' : 'град','thunderstorm' : 'гроза','thunderstorm-with-rain': 'дождь с грозой','thunderstorm-with-hail' : 'гроза с градом'}
        weather_condition = weather['fact']['condition']
        if weather_condition in condition_dict:
            weather_condition= condition_dict[weather_condition]
            print(weather_condition.title())

        weather_wind_speed='Скорость ветра '+ str(weather['fact']['wind_speed'])+' м/с'
        print(weather_wind_speed)

        weather_wind_gust='С порывами до '+ str(weather['fact']['wind_gust'])+' м/с'
        print(weather_wind_gust)
        
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
        print(weather_wind_dir)

        weather_pressure_mm='Атмосферное давление '+str(weather['fact']['pressure_mm'])+' мм рт. ст.'
        print(weather_pressure_mm)
        
        weather_humidity = "Влажность воздуха "+str(weather['fact']['humidity'])+" %"
        print(weather_humidity)


