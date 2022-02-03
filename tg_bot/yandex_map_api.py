
import requests
from auth_data import ya_geo_key,server_address


def get_geo_point(city):


    drf_check_url = f"{server_address}/city_check/"
    data_req = {"geo_name": f"{city}"}
    drf_req = requests.post(url=drf_check_url,data=data_req)

    if "Not Found city" not in drf_req.text:
        print("ГОРОД НАЙДЕН В БАЗЕ")
        
        drf_req_json=drf_req.json()[0]
        
        # print("drf_req_json",drf_req_json)
        geo_city_pk=drf_req_json.get("pk")
        geo_name =drf_req_json.get("geo_name")
        geo_lat =drf_req_json.get("geo_lat")
        geo_lon =drf_req_json.get("geo_lon")
        geo_description =drf_req_json.get("geo_description")
        weather =drf_req_json.get("weather")
        
        if len(weather)==0:
            print("ДЛЯ ГОРОДА В БАЗЕ НЕТ ИНФОРМАЦИИ ПО ПОГОДЕ")
        return geo_lat,geo_lon,geo_name,geo_description,weather,geo_city_pk
    else:
        print("ГОРОДА НЕТ В БАЗЕ, ВЫПОЛНЯЮ ЗАПРОС ")
        url=f'https://geocode-maps.yandex.ru/1.x?format=json&geocode={city},Беларусь&apikey={ya_geo_key}'
        # print(url)
        req_geo = requests.get(url)
        json_string=req_geo.json()
        

        geo_point =json_string["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        #дэфолднаые координаты для всякого города, которого невозможно найти в Беларуси
        if "27.701402 52.858254" in geo_point:
            code = 0
            return code
            
        try:
            geo_name =json_string["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]['name']
        except:
            geo_name=''
        try:
            geo_description =json_string["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]['description']
        except:
            geo_description=''
        
        
        geo_tuple = str(geo_point).split(" ")
        geo_lat = geo_tuple[0]
        geo_lon =geo_tuple[1]


        #после получения данных из апи яндекса, заношу их в свою БД
        drf_create_url =f"{server_address}/create_city/"
        drf_create_data ={
                    "geo_name": f"{geo_name}",
                    "geo_lat": f"{geo_lat}",
                    "geo_lon": f"{geo_lon}",
                    "geo_description": f"{geo_description}"
                    }
        # print("Данные для отправки к API create\n",drf_create_data)
        dfr_create_req = requests.post(drf_create_url,data=drf_create_data)
       
        drf_req_json=dfr_create_req.json()
        
        # print("drf_req_json",drf_req_json)
        geo_city_pk=drf_req_json.get("id")
        # geo_name =drf_req_json.get("geo_name")
        # geo_lat =drf_req_json.get("geo_lat")
        # geo_lon =drf_req_json.get("geo_lon")
        # geo_description =drf_req_json.get("geo_description")
        weather=[]
        
        return geo_lat,geo_lon,geo_name,geo_description,weather,geo_city_pk



