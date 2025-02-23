import smtplib

to = input("Enter the email of the recipient : ")
content = input("Enter the content of the message : ")

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('archedossou26@gmail.com','ragh ovoz dbib xalt')
    server.sendmail("archedossou26@gmail.com",to,content)
    server.close()

sendmail(to, content)