import time
import json
import os
import send_email
import check_and_handle

def main():
    allowed_commands=["weather"]
    whitelist=["6617557009@mms.att.net","6616456588@mms.att.net"]
    try:
        f=open("last_email",'r')
        inp=json.load(f)
        f.close()
    except IOError:
        print "Error, no mail"
        exit(1)

    recheck=True

    if inp['type']=='No new mail.':
        recheck=False
    elif inp['type']=='Mail':
        from_name=inp['from'].split('(')[0]
        from_addr=inp['from'].split('(')[1]
        from_addr=from_addr.split(')')[0]
        if from_addr in whitelist:
            cmd=inp['body'].split()
            if cmd[0] in allowed_commands:
                os.system(cmd[0]+".py " +cmd[1:])
            else:
                send_email.uc(from_addr,cmd[0])
        else:
            send_email.us(from_addr)

    if recheck:
        check_and_handle.main

main()
