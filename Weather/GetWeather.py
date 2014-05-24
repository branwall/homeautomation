import urllib.request
import json

while True:
    try:
        response = urllib.request.urlopen('http://api.wunderground.com/api/325cc240406ab251/conditions/q/CA/Merced.json')
        break
    except ValueError:
        print("HELP I FAILED YOU")

html = response.read()


weather = json.loads(html.decode("utf-8"))
print ("weather " + weather["current_observation"]["weather"])
print ("feelslike " + weather["current_observation"]["feelslike_f"])
print ("wind gust " + weather["current_observation"]["wind_gust_mph"])
print ("visibility " + weather["current_observation"]["visibility_mi"])
print ("humidity " + weather["current_observation"]["relative_humidity"])

usefulWeather = ""
usefulWeather += weather["current_observation"]["weather"]
usefulWeather+="\n"
usefulWeather += weather["current_observation"]["feelslike_f"]
usefulWeather+="\n"
usefulWeather += weather["current_observation"]["wind_gust_mph"]
usefulWeather+="\n"
usefulWeather += weather["current_observation"]["visibility_mi"]
usefulWeather+="\n"
usefulWeather += weather["current_observation"]["relative_humidity"]

file = open('weatherUnrefined.txt','w')
file.write(html.decode("utf-8"))
file.close()

file = open('weather.txt','w')
file.write(usefulWeather)
file.close()
