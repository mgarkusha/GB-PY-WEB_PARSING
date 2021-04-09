import requests
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()


# Функция для апи openweathermap.org
def open_weather(city_name):
    concrete_params = {
        "q": city_name,
        "appid": ow_appid,
        "lang": "ru",
        "units": "metric"
    }
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    return requests.get(base_url, params=concrete_params)


# Креды OW
ow_appid = os.getenv("ow_appid")

####################
# 2 Часть задания (про погоду)
####################
print("Погода в городе!")
city = str(input("Введите наименование города: "))
r_ow = open_weather(city)
pprint(r_ow.json())
