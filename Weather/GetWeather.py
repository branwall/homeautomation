import urllib.request
import json
state= "CA"
location = "Santa Clarita"

try:
    file = open('master-config','r')
    for c,line in enumerate(file,start=1):
        if (c==1):
            location=line.rstrip()
        if (c==2):
            state = line.rstrip()        
except IOError:
    print ("Error: master-config not found. Using default location of Santa Clarita, CA")
url =  'http://api.wunderground.com/api/325cc240406ab251/conditions/q/' + state + '/' + location + '.json' 

while True:
    try:
        response = urllib.request.urlopen(url)
        break
    except urllib.error.URLError:
        print("URL Error, could not get weather for %s, %s" % (location,state))
        exit(1)

html = response.read()
weather = json.loads(html.decode("utf-8"))
print ("weather " + weather["current_observation"]["weather"])
print ("feelslike " + weather["current_observation"]["feelslike_f"])
print ("wind gust " +str(weather["current_observation"]["wind_gust_mph"]))
print ("visibility " + weather["current_observation"]["visibility_mi"])
print ("humidity " + weather["current_observation"]["relative_humidity"])

usefulWeather = ""
usefulWeather += weather["current_observation"]["weather"]
usefulWeather+="\n"
usefulWeather += weather["current_observation"]["feelslike_f"]
usefulWeather+="\n"
usefulWeather += str(weather["current_observation"]["wind_gust_mph"])
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
