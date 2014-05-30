import json
import twill
from twill.commands import *
from twill import get_browser
browser=get_browser()
courses={}
people={}

def init_arrays():
    try:
        f = open('requests','r')
        line=f.readline()
        while line!="":
            if line[0]!="\t":
                t=line.strip().split(" ")         
                courses[t[0].strip()]=t[1]
                people[t[0].strip()]=[]
                line=f.readline()
                while line!="" and line[0]=="\t":
                    person=line.strip()
                    people[t[0].strip()].append(person)
                    line=f.readline()
        print(courses,people)
    except IOError:
        print ("Couldn't open requests file")
        exit(1)


def init_web():
    browser.clear_cookies()
    go("https://classes.uchicago.edu")
    follow("Sign in with your CNET ID")
    browser.showforms()
    fv(1,"j_username","branwall")
    pwd=getpassword("input password\n")
    fv(1,"j_password",pwd)
    submit()
    submit()

def perform_search(keyword):
    browser.showforms()
    fv(1,"TermName",'Autumn 2014')
    fv(2,"Keyword",keyword)
    submit(3)
    showforms()
    showlinks()
    html=show()
    parsed=find('<td class\="six">.*?</td>')
    print
    print parsed


def lookup(term):
    url="https://classes.uchicago.edu/search.php?Keyword="+term+"&CourseLevel=All&search=SEARCH"
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.URLError:
        print("URL Error, could not get course info")
        exit(1)

    html = response.read()
    ttttt=open('sample_out.txt','w')
    ttttt.write(str(html))
    ttttt.close()

init_web()
perform_search("cmsc 151")
'''

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
      wType=="Rain Mist" or wType.split()[1]=="Hail" or wType=="Hail" or wType=="Small Hail"  or 
      wType.split()[1]=="Ice Crystals"  or wType=="Ice Crystals" or wType.split()[1]=="Ice Pellets" or
      wType=="Ice Pellets" or wType.split()[1]=="Hail" or wType=="Hail Showers" or
      wType.split()[2]=="Hail" or wType.split()[2]=="Pellet"):
    wReturn = Catergories['RS']
elif (wType==)
else:
    print( Categories['HS'])
    wReturn = Categories['HS']


  
'''
