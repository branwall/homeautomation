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
            'CN': 'Cold Night'}


#Default values for variables:
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
        print("URL Error, could not get weather for %s, %s"
              + " (Check  your master-config file)" % (location,state))
        exit(1)

html = response.read()
weather = json.loads(html.decode("utf-8"))

wValues=weather["current_observation"]
wType=wValues["weather"]
wTemp=wValues["feelslike_f"]
wTime=wValues["local_time_rfc822"]

wReturn=Categories['CS'] #just an initializer

if ( wType=="Light Drizzle" or wType=="Heavy Drizzle" or wType=="Drizzle" or wType=="Light Rain" or 
     wType=="Light Rain Showers" or wType=="Light Rain Mist" or wType=="Light Freezing Rain" or 
     wType=="Light Freezing Drizzle" or wType=="Freezing Drizzle" or wType=="Heavy Freezing Drizzle" or
     wType=="Unknown Precipitation" ):
    print (Categories['LR'])
    wReturn = Categories['LR']
elif (wType=="Rain" or wType=="Heavy Rain" or wType=="Rain Showers" or wType=="Heavy Rain Showers" or
      wType=="Heavy Freezing Rain" or wType=="Freezing Rain" or wType=="Heavy Rain Mist" or
      wType=="Rain Mist" or wType.split()[1]=="Hail" or wType=="Hail"):
    #there are more but I have to stop for the night
    wReturn = Catergories['RS']
else:
    print( Categories['HS'])
    wReturn = Categories['HS']


  
