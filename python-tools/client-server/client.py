#! /usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 444
#host = socket.gethostname()

clientsocket.connect((host,port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
