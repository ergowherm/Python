import smtplib

sender = 'gowherm@aptechqatar.com'
receivers = ['gowherm@aptechqatar.com']

message = ("""From: From Person <gowherm@aptechqatar.com>
To: To Person <gowherm@aptechqatar.com>
Subject: SMTP e-mail test

This is a test e-mail message.
""")

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")
