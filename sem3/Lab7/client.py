import socket
from server import HOST, PORT

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаём сокет клиента

client_socket.connect((HOST, PORT))  # подключаем сокет клиента к адресу по которому расположен сокетсервера

response = str()

while response != 'OK':
    sender_email = input("Input your email: ")

    client_socket.send(sender_email.encode("utf-8"))
    response = client_socket.recv(2048).decode('utf8')
    assert response == 'Response [200]'

    sender_password = input("Input ur password: ")

    client_socket.send(sender_password.encode('utf-8'))
    response = client_socket.recv(2048).decode('utf8')
    assert response == 'Response [200]'

    text = input("Message text: ")
    client_socket.send(text.encode('utf-8'))

    response = client_socket.recv(2048).decode('utf8')
    print(response)
