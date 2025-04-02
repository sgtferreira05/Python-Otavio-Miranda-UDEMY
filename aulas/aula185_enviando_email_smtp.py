# Sending emails SMTP with Python

import os
import pathlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import smtplib

from dotenv import load_dotenv #type: ignore


load_dotenv()
# Caminho arquivo HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'aula185.html'



# Dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# Configurações do servidor SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto

with open(CAMINHO_HTML, 'r', encoding='utf-8') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='João')

# Transformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['From'] = remetente
mime_multipart['To'] = destinatario
mime_multipart['Subject'] = 'Este é um assunto do e-mail'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)


# Envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mime_multipart)
    print('Email enviado com sucesso!')