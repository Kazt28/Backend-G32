from smtplib import SMTP
from email.message import EmailMessage
from os import getenv


def enviar_correo(destinatarios, asunto, cuerpo):
    mensaje = EmailMessage()
    mensaje["From"] = getenv("EMAIL")
    mensaje["to"] = destinatarios
    
    mensaje["Subject"] = asunto
    
    mensaje.set_content(cuerpo)
    
    mensaje.add_alternative(cuerpo, subtype='html')
    
    servidor = SMTP(host=getenv("SMTP_HOST"), port=getenv("SMTP_PUERTO"))
    
    servidor.starttls()
    
    servidor.login(user=getenv("EMAIL"), password= getenv("EMAIL_PASSWORD"))
    
    servidor.send_message(mensaje)
    
    servidor.close()