import smtplib
import json
try:
    f=open('config','r')
    settings=json.load(f)
    f.close()
except (ValueError,IOError):
    print "Error: No config file exists (to create one, try checking mail!"

def send(toAdd, fromAdd, body):
    smtpUser = 'myautomationserver@gmail.com'
    smtpPass = 'bottlecap'
    subject = ''
    header = 'To: ' + toAdd +  '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(settings['un'], settings['pw'])
    s.sendmail (fromAdd, toAdd, header + '\n\n' + body)
    s.quit()


def us(toAddr):
    send(toAddr,"Automation Server","Error:\nUnfortunately, you are not permitted to request commands to this server")

def uc(toAddr,cmd):
    send(toAddr,"AutomationServer","Error:\n" + cmd + ": unknown command")
