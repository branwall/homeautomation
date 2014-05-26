import urllib.request
import json
state= "IL"
location = "60637"
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
wTimev=wTime.split(" ")
wTimeh=wTimev[4].split(":")
if int(wTimeh[0]) > 12:
    wTimeh[0]=str(int(wTimeh[0])-12)
wTimePretty=(wTimev[0]+" "+wTimev[2]+" " + wTimev[1] + " at " + ":".join(wTimeh[0:2]) )
import send_email
import sys
sys.argv[1]
send_email.send(sys.argv[1],"Weather Info","It's %s and %s in %s as of %s" %(wTemp,wType.lower(),location,wTimePretty))
