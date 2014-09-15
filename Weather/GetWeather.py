#!/usr/bin/python3

#uses Python3

import urllib.request
import json
Categories={'LR': 'Light Rain',
            'RS': 'Rain Storm',
            'TS': 'Thunder Storms',
            'HS': 'Hot and Sunny',
            'CS': 'Cold and Sunny',
            'CD': 'Cloudy',
            'FG': 'Foggy',
            'SW': 'Snowy',
            'WN': 'Warm Night',
            'CN': 'Cold Night',
            'PT': 'Particulate'}


#Default values for variables:
state= "CA"
location = "Santa Clarita"
try:
    file = open('/home/pi/dev/HomeAutomation/homeautomation/Weather/master-config','r')
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
        print("URL Error, could not get weather for " + location + ", " + state
              + " (Check  your master-config file)")
        exit(1)

html = response.read()
weather = json.loads(html.decode("utf-8"))

wValues=weather["current_observation"]
wType=wValues["weather"]
wTemp=wValues["feelslike_f"]
wTime=wValues["local_time_rfc822"]

wReturn=Categories['CS'] #just an initializer

#print (wType,end=" = ");
if((wType.split( )[0] == 'Light') or (wType.split( )[0] == 'Heavy')):
        wType=wType[6:];
if(wType.split( )[0] == 'Blowing'):
        wType=wType[8:];
if(wType.split( )[0] == 'Low'):
        wType=wType[13:];
if(wType.split( )[0] == 'Widespread'):
        wType=wType[11:];
if(wType.split( )[0] == 'Freezing'):
        wType=wType[9:];
    #NOTE: "Patches/Shallow/Partial" are all unique identifiers of FOG
    #NOTE: "Mostly/Partly/Scattered/Funnel" are all unique to CLOUDS,
            #^^^ however there is a thunderstorm->thunderstorms clause there (cloudy->clouds)

if ((wType.split( )[0] == 'Drizzle') or (wType[0:5] == 'Rain ') or (wType.split( )[0] == 'Ice') or (wType.split( )[0] == 'Small') or (wType.split( )[0] == 'Spray')):
    wReturn=Categories['LR'];
elif ((wType.split( )[0] == 'Rain') or (wType.split( )[0] == 'Hail')):
    wReturn=Categories['RS'];
elif ((wType.split( )[0] == 'Snow')):
    wReturn=Categories['SW'];
elif ((wType.split( )[0] == 'Thunderstorm') or (wType.split( )[0] == 'Thunderstorms')):
    wReturn=Categories['TS'];
elif ((wType.split( )[0] == 'Mist') or (wType.split( )[0] == 'Overcast') or (wType.split( )[0] == 'Fog') or (wType.split( )[0] == 'Patches') or (wType.split( )[0] == 'Shallow') or (wType.split( )[0] == 'Funnel') or (wType.split( )[0] == 'Partial')):
    wReturn=Categories['FG'];
elif ((wType.split( )[0] == 'Haze') or (wType.split( )[0] == 'Clear') or (wType.split( )[0] == 'Partly') or (wType.split( )[0] == 'Mostly') or (wType.split( )[0] == 'Scattered')):
    if(int(wTemp) > 65):
        wReturn=Categories['HS'];
    else:
        wReturn=Categories['CS'];
else:
    wReturn=Categories['PT'];
print(wReturn);

def weatherReturn():
    return wReturn;

