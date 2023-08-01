import requests
from flask import Flask
from datetime import datetime

user_api = "740ecb1f4de28b2f65f4905094472388"
location = input("please input city:  ")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api+"&units=imperial"



api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print("Invalid city {}, Please re-enter your city name".format(location))
else:

    temp_city = api_data["main"]["temp"]
    desc = api_data["weather"][0]["description"]
    real_feel = api_data["main"]["feels_like"]
    max_temp = api_data["main"]["temp_max"]
    min_temp = api_data["main"]["temp_min"]
    hmdty = api_data["main"]["humidity"]
    wind_spd = api_data["wind"]["speed"]
    wind_dir = api_data["wind"]["deg"]
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {} deg F".format(temp_city))
print ("Current weather desc  :",desc)
print("Current weather in {}: {}".format(location.upper(), real_feel))
print ("Current Humidity      :",hmdty, '%')
print ("Maximum Temperature for today is   :",max_temp, "deg F")
print ("Minimum Temperature for today is   :",min_temp, "deg F")
print ("Current wind speed    :",wind_spd,'mph')
print ("current wind direction is   :",wind_dir, "degrees")
