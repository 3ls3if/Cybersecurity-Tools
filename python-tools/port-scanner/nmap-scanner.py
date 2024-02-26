#! /usr/bin/python3

import nmap
import sys

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("----------------------------------------------")
print("\n")

ip_addr = input("Target IP:  ")
print("Target IP set to: ", ip_addr)
type(ip_addr)

resp = input("""\nPlease enter the type of scan you want to run:
		[1] Syn/Ack Scan
		[2] UDP Scan
		[3] Comprehensive Scan
	       [99] Exit
""")

print("You have selected option: ", resp)

if resp == '1':
	print("Nmap Version: ", scanner.nmap_version())
	scanner.scan(ip_addr, '1-1024', '-v -sS')
	print(scanner.scaninfo())
	
	# Displaying Host Status
	print("IP Status: ", scanner[ip_addr].state())
	
	# Displaying Protocols
	print(scanner[ip_addr].all_protocols())

	# Displaying Open Ports
	print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '2':
	print("Nmap Version: ", scanner.nmap_version())
	scanner.scan(ip_addr, '1-1024', '-v -sU')
	print(scanner.scaninfo())

        # Displaying Host Status
	print("IP Status: ", scanner[ip_addr].state())

        # Displaying Protocols
	print(scanner[ip_addr].all_protocols())

        # Displaying Open Ports
	print("Open Ports: ", scanner[ip_addr]['udp'].keys())

elif resp == '3':
	print("Nmap Version: ", scanner.nmap_version())
	scanner.scan(ip_addr, '1-1024', '-v -sV -sS -sC -A -O -T4')
	print(scanner.scaninfo())

        # Displaying Host Status
	print("IP Status: ", scanner[ip_addr].state())

        # Displaying Protocols
	print(scanner[ip_addr].all_protocols())

        # Displaying Open Ports
	print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '99':
	print("Exiting...Bye...")
	sys.exit()

else:
	print("Provide a valid option!")
