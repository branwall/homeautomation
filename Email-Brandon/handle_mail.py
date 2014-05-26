import time
import json
import os
import send_email

def pull():
    try:
        f=open("last_email",'r')
        inp=json.load(f)
        f.close()
    except IOError:
        print "Error, no mail"
        exit(1)
    return inp

def main():
    allowed_commands=["weather"]
    whitelist=["6617557009@mms.att.net","6616456588@mms.att.net"]
    inp=pull()
    if inp['type']=='Mail':
        from_name=inp['from'].split('(')[0]
        from_addr=inp['from'].split('(')[1]
        from_addr=from_addr.split(')')[0]
        if from_addr in whitelist:
            cmd=inp['body'].split()
            if cmd[0].lower().rstrip() in allowed_commands:
                print "Processing command %s for %s" % (cmd[0],from_name)
                os.system("python3 " + cmd[0].lower().rstrip() + ".py " + from_addr + " "+ " ".join(cmd[1:]))
            else:
                print "%s tried to use invalid command %s" % (from_name, cmd[0])
                send_email.uc(from_addr,cmd[0])
        else:
            print "%s attempted to access the server; sending rejection" % from_addr
            send_email.us(from_addr)
