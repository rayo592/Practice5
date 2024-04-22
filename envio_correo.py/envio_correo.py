import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def enviar_correo():
    # Configuración del servidor SMTP y credenciales
    smtp_server = 'tu_servidor_smtp'
    smtp_port = 587
    username = 'tu_correo@gmail.com'
    password = 'tu_contraseña'

    # Crear instancia de servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)

    # Configuración del correo
    mensaje = MIMEMultipart()
    mensaje['From'] = 'tu_correo@gmail.com'
    mensaje['To'] = 'destinatario@example.com'
    mensaje['Subject'] = 'Asunto del correo'

    cuerpo_correo = MIMEText('Texto del cuerpo del correo')
    mensaje.attach(cuerpo_correo)

    archivo_adjunto = MIMEApplication(open('archivo_adjunto.xlsx', 'rb').read())
    archivo_adjunto.add_header('Content-Disposition', 'attachment', filename='archivo_adjunto.xlsx')
    mensaje.attach(archivo_adjunto)

 
    server.send_message(mensaje)

  
    server.quit()