#imports pip install smtplib
import smtplib 

#The Mail
user = input("Your_mail_loggin: ")

pwd = input("Your_password: ")

mail_text = input("Your_Text: ") # ENTER = \n

subject = input("Subject: ")

MAIL_FROM = input("sender(your_mail): ")

RCPT_TO  = input("Reciever: ")

#Formation mail to SMTP
DATA = "From:%s\nTo:%s\nSubject:%s\n\n%s" % (MAIL_FROM, RCPT_TO, subject, mail_text)

#authentification and sending
server = smtplib.SMTP("smtp_of_your_mail_prvider:TLS-Port")#conecting to SMTP server ovfer TLS
server.starttls()#TLS connection
server.login(user, pwd)#authentification
server.sendmail(MAIL_FROM, RCPT_TO, DATA)#sending mail
server.quit()#quitting the session
