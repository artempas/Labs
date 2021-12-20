import os
import socket
from email.utils import parseaddr
from smtplib import SMTP, SMTPAuthenticationError
import datetime
from dotenv import load_dotenv

load_dotenv()
HOST = "127.0.0.1" #localhost
PORT = 4321
admin_email = os.getenv('ADMIN_LOGIN')


if __name__ == '__main__':


    # AF_INET - семейство адресов типа ИНТЕРНЕТ|SOCK_STREAM - TCP/IP протокол подключения
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    collector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST,PORT)) # присваиваем сокету сервера адрес и порт

    server.listen(1) # начинаем прослушивание входящих подключений макс одно

    collector.connect((HOST,PORT+1))
    unique_id = int(datetime.datetime.utcnow().timestamp())

    while True:
        client_socket, address = server.accept() # подключение пользователя к серверу

        while True:
            print(f"Client {address} connected")
            try:
                client_email = client_socket.recv(2048).decode('utf-8') # получение 2048байт от пользователя
                print(f"Email received {client_email}")
                client_socket.send('Response [200]'.encode('utf8'))

                client_password = client_socket.recv(2048).decode('utf-8')
                print(f"Password received {client_password}")
                client_socket.send('Response [200]'.encode('utf8'))

                client_text = client_socket.recv(2048).decode('utf-8')
                print(f"Text received {client_text}")


                message_text = f'Subject: {unique_id}\n\n{client_text}'
                if "@" not in parseaddr(client_email)[1] or '.' not in parseaddr(client_email)[1]:
                    client_socket.send("Incorrect email format. Try again".encode('utf-8'))
                    continue
                with SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT'))) as smtp:
                    smtp.starttls()
                    try:
                        smtp.login(client_email, client_password)
                    except SMTPAuthenticationError:
                        client_socket.send('Authentication error, try again please'.encode('utf-8'))
                        continue
                    try:
                        smtp.sendmail(client_email,admin_email, message_text)
                    except BaseException as exc:
                        client_socket.send(('Sending error: '+str(exc)).encode('utf-8'))
                        continue
                    client_socket.send("OK".encode('utf8'))
                    collector.send(str(unique_id).encode('utf8'))
                    unique_id+=1
                    break
            except ConnectionError:
                break

