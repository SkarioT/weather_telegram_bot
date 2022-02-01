import requests

city="Минск"
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