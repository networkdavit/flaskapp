import smtplib

TO = "sometypeofemail@samplegmail.com"
SUBJECT = "TEST MAIL"
TEXT = "Here is a message from python."

gmail_sender = "sometypeofemail@samplegmail.com"
gmail_passwd = "enter_your_password_here"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)

BODY = "\r\n".join(["To: %s" % TO,
                    "From: %s" % gmail_sender,
                    "Subject: %s" % SUBJECT,
                    "", TEXT])

try:
    server.sendmail(gmail_sender, [TO], BODY)
    print ("email sent")
except:
    print ("error sending mail")

server.quit()
