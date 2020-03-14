import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename

username = 'smtp_login'
password = 'smtp_password'
addresses = [
"one_email@address.com",
"another_email@address.com"
]

path = 'path/to/files/that/will/be/attached'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

def send_email(send_from: str, send_to: str, msg: str):
    smtp = smtplib.SMTP(host="smtp.zenbox.pl", port= 587) 
    smtp.starttls()
    smtp.login(username,password)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()

def prepare_and_send_emails(send_from: str, subject: str, text: str, send_to: list, files: list):
    i = 0
    for address in send_to:
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['Subject'] = subject
        msg.attach(MIMEText(text))

        filename = files[i]
        
        print(filename + " - " + address)
        with open(filename, "rb") as fil:
            ext = filename.split('.')[-1:]
            attachedfile = MIMEApplication(fil.read(), _subtype = ext)
            attachedfile.add_header(
                'content-disposition', 'attachment', filename=basename(filename) )
        msg.attach(attachedfile)
        msg['To'] = address
        i += 1

        send_email(send_from= send_from, send_to= address, msg = msg)

prepare_and_send_emails(
send_from = username,
subject = "[Pisz Lepsze Testy] Twoja licencja na produkt JetBrains",
text = "Cześć! W załączniku znajdziesz swoją licencję.",
send_to = addresses,
files = files)


