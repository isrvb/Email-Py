#Send Email from Python
import os
import smtplib
#Message email
message = "Hi, a message from Python!"
#Subject
subject = 'Test Email'
#Format
message = 'Subject: {}\n\n{}'.format()
#Server
server = smtplib.SMTP('smtp.gmail.com',587)
#TLS
server.starttls()
#Login User
server
