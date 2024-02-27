#!/usr/bin/python3

import socket

def banner(ip, port):
	s = socket.socket()
	s.connect((ip, int(port)))
	banner=s.recv(1024).decode()
	print(banner)

def main():
	ip = str(input("Please Enter Target IP: "))
	port = str(input("Enter Target Port: "))
	

	banner(ip, port)

main()
