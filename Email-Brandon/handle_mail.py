import time
import send_email
allowed_commands=["weather"]
whitelist=["6617557009@mms.att.net"]
try:
    f=open("last_email",'r')
    input=json.load(f)
    f.close()
except IOError:
    exit(1)

recheck=True

if input['type']=='No new mail.':
    recheck=False
elif input['type']=='Mail':
    from_name=input['from'].split('(')[0]
    from_addr=input['from'].split('(')[1]
    from_addr=from_addr.split(')')[0]
    print "from" from_name
    print "fromd" from_addr
    if from_addr in whitelist:
        cmd=body.split()
    
        if cmd in allowed_commands:
            os.system(cmd[0]+".py " +cmd[1:])
        else:
            #unknown command
            send_email.uc(from_addr)
    else:
        send_email.us(from_addr)

if recheck:
    os.system("check_and_handle.py")
