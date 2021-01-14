import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_address = 'tu-correo@gmail.com' #gmail
sender_pass = 'contraseña'

session = smtplib.SMTP('smtp.gmail.com',587)
session.starttls()
session.login(sender_address, sender_pass)

correo = 'correo@gmail.com'

for i in range(3):
    message = MIMEMultipart()
    message['From'] = sender_address
    message['Subject'] = 'Prueba'
    mail_content = "Hola mundo"
    message.attach(MIMEText(mail_content, 'plain'))
    text = message.as_string()

    session.sendmail(sender_address, correo, text)
    #time.sleep(3)

session.quit()