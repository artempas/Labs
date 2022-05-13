import email
import imaplib
import os
import socket
import time
from datetime import datetime
import logging
from server import HOST as server_adress
from server import PORT as server_port
from dotenv import load_dotenv


handler = logging.FileHandler('successful.log')
success_log = logging.getLogger('success')
success_log.setLevel(logging.INFO)
success_log.addHandler(handler)

handler = logging.FileHandler('failed.log')
failed_log = logging.getLogger('fail')
failed_log.setLevel(logging.ERROR)
failed_log.addHandler(handler)


load_dotenv()
admin_login = os.getenv('ADMIN_LOGIN')
admin_password = os.getenv('ADMIN_PASSWORD')

collector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
collector.bind((server_adress, server_port+1))

collector.listen(1)
server_socket, address = collector.accept()

while True:
    id = server_socket.recv(2048).decode('utf-8')
    time.sleep(10)
    with imaplib.IMAP4_SSL(os.getenv("IMAP_SERVER"), int(os.getenv('IMAP_PORT'))) as imap:
        imap.login(admin_login, admin_password)
        imap.select()
        _, ids = imap.uid('search', None, f'(SENTSINCE {datetime.now().strftime("%d-%b-%Y")})')
        ids = ids[0].decode().split()
        for iD in ids:
            print(iD)
            _, messageRaw = imap.uid('fetch', iD, '(RFC822)')
            message = email.message_from_bytes(messageRaw[0][1])
            print(message.get_payload())
            print(f'{id=} {message["Subject"]}')
            if message['Subject'] == id:
                success_log.info(f'ID:{id}, TEXT:{message.get_payload(decode=True)}')
            else:
                failed_log.error(f'TEXT:{message.get_payload(decode=True)}')
    time.sleep(int(os.getenv('PERIOD_CHECK')))
