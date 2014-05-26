#!/user/bin/env/python
import feedparser
import json
import time
def main():
    try:
        f=open('config','r')
        settings=json.load(f)
        f.close()
    except (ValueError,IOError):
        settings={}
        settings['un']=input('Enter a Gmail address in quotes ("user@gmail.com")')
        settings['pw']=input("Enter " + settings['un'] + "'s password (in quotes)")
        settings['tot']=0

    if not settings['tot']=="":
        settings['tot']=int(settings['tot'])
    else:
        settings['tot']=0

    response = feedparser.parse("https://" + settings['un'] + ":" + settings['pw'] 
                                + "@mail.google.com/gmail/feed/atom")

#NOTE: I have changed the "timeout" parameter of feedparser to be 10 seconds.
#this can be adjusted (or completely removed) by opening feedparser.py
#and altering line 3005

    output={}
    
    try:
        unread_count = int(response["feed"]["fullcount"])
        if settings['tot']>unread_count:
            settings['tot']=0
        elif settings['tot']==unread_count:
            output['type']='No new mail.'
        else:
            i=unread_count-settings['tot']-1
            output['type']='Mail'
            output['subject']=response.entries[i].title
            output['from']=response.entries[i].author
            output['body']=response.entries[i].summary_detail['value']
            output['time']=str(response.entries[i].updated_parsed)
            settings['tot']+=1
            f=open('config','w')
            json.dump(settings,f)
    except KeyError:
        output['type']="Timeout"

    with open('last_email','w') as f:
        json.dump(output,f)

main()
