import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "kostyukovkg@gmail.com"
    password = os.getenv('PASSWORD') # .zshrc folder in the root

    receiver = "kostyukovkg@gmail.com"
    context = ssl.create_default_context()

    #message = """\
    #Subject: Hello
    #How are you?!"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
