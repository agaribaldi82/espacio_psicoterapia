from flask import Flask, request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

app = Flask(__name__)

@app.route('/contacto.html' methods=['POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form("name")
        apellido = request.form("lastname")
        email = request.form("email")
        telefono = request.form("tel")
        mensaje = request.form("textarea")
        
        email_destino = "adgaribaldi@gmail.com"
        password = "bruno3"
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        
   
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = email_destino
        msg['Subject'] = "Nuevo mensaje de contacto desde tu sitio web"
        cuerpo = f"Nombre: {nombre}\nApellido: {apellido}\nEmail: {email}\nTeléfono: {telefono}\nMensaje: {mensaje}"
        msg.attach(MIMEText(cuerpo, 'plain'))
        
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_destino, password)
            server.sendmail(email, email_destino, msg.as_string())
        
        return "Mensaje enviado correctamente"

if __name__ == '__main__':
    app.run(debug=True)