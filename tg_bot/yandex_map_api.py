
import requests
import json
from auth_data import ya_geo_key
city="Минск"

def get_geo_point(city):
    
    drf_check_url = "http://127.0.0.1/city_check/"
    data_req = {"geo_name": {city}}
    DFR_req = requests.post(url=drf_check_url,data=data_req)
    if "Not Found city" not in DFR_req.text:
        print("город найден")
        print(DFR_req.json())
        drf_req_json=DFR_req.json()[0]
        geo_name =drf_req_json.get("geo_name")
        geo_lat =drf_req_json.get("geo_lat")
        geo_lon =drf_req_json.get("geo_lon")
        geo_description =drf_req_json.get("geo_description")
    else:
        dfr_create_url ="http://127.0.0.1/create_city/"
        dfr_create_data =""
        dfr_create_req = requests.post(dfr_create_url,)

    url=f'https://geocode-maps.yandex.ru/1.x?format=json&geocode={city},Беларусь&apikey={ya_geo_key}'
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
        #дэфолднаые координаты для всего чего невозможно найти в Беларуси
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
        lat = geo_tuple[0]
        lon =geo_tuple[1]
        print(geo_description)
        print(geo_name)
        print(geo_tuple)
    return lat,lon,geo_name,geo_description

# ss=get_geo_point(city)
# print(ss)