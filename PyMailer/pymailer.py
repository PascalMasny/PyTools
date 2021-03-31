#imports pip install smtplib
import smtplib 

#The Mail
user = "your_mail_loggin"

pwd = "your_password"

mail_text = "Hello World!\n" # ENTER = \n

subject = "subject"

MAIL_FROM = "sender(your_mail)"

RCPT_TO  = "reciever"

#Formation mail to SMTP
DATA = "From:%s\nTo:%s\nSubject:%s\n\n%s" % (MAIL_FROM, RCPT_TO, subject, mail_text)

#authentification and sending
server = smtplib.SMTP("smtp_of_your_mail_prvider:TLS-Port")#conecting to SMTP server ovfer TLS
server.starttls()#TLS connection
server.login(user, pwd)#authentification
server.sendmail(MAIL_FROM, RCPT_TO, DATA)#sending mail
server.quit()#quitting the session
