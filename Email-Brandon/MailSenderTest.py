import smtplib

class MailSend(object):
    def message(self, toAdd, fromAdd, body):
        smtpUser = 'myautomationserver@gmail.com'
        smtpPass = 'bottlecap'

        #toAdd = '6616456588@txt.att.net'
        #fromAdd = 'TTTserver'

        subject = ''
        header = 'To: ' + toAdd +  '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
        #body = 'This is the birth of the new System, one of its first texts!'

        print (header + '\n' + body)

        s = smtplib.SMTP('smtp.gmail.com',587)

        s.ehlo()
        s.starttls()
        s.ehlo()

        s.login(smtpUser, smtpPass)
        s.sendmail (fromAdd, toAdd, header + '\n\n' + body)

        s.quit()
