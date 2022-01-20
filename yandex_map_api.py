
import requests
import json
from auth_data import ya_geo_key
# city="Рогачев"

def get_geo_point(city):
    url=f'https://geocode-maps.yandex.ru/1.x?format=json&geocode={city},Беларусь&apikey={ya_geo_key}'#& [sco=<string>]
    print(url)
    req_geo = requests.get(url)
    json_string=req_geo.json()
    # print(json_string)
    with open('geo.json', 'w') as outfile:
        json.dump(json_string, outfile)

    # # прописать логику сбора запросов, что бы хранить у себя у какого городе какие координаты. и  в дальнейшем, не делать запросы, и смотреть у себя, есть ли инфа по городу

    with open('geo.json','r') as w:
        geo =json.load(w)
        code=1
        geo_point =geo["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        if "27.701402 52.858254" in geo_point:
            code =0
            return code
            #return f"Не удалось найти {city},Беларусь"
        try:
            geo_name =geo["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]['name']
        except:
            geo_name=''
        try:
            geo_description =geo["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]['description']
        except:
            geo_description=''
        
        
        geo_tuple = str(geo_point).split(" ")
        # print(geo_description)
        # print(geo_name)
        # print(geo_tuple)
    return geo_tuple,geo_name,geo_description

# ss=get_geo_point(city)
# print(ss)