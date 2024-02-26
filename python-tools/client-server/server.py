#! /usr/bin/python3

import  socket
import os

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostname()
host = "127.0.0.1"
port = 444

serversocket.bind((host,port))

serversocket.listen(3)

while True:
	clientsocket, address = serversocket.accept()
	
	print("Received Connection From: %s"% str(address))
	
	message1 = "Connection Established..."+"\r\n"
		
	clientsocket.send(message1.encode('ascii'))

	clientsocket.close()

