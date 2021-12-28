#!/bin/python
import sys
import socket

from datetime import datetime

#Define target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
else:
	print("invalid amount of aguments")
	print("syntax : python3 scanner.py <ip>")

#Add a pretty Banner
print("-" * 50)
print("scanner target "+target)
print("time started: "+str(datetime.now()))
print("-"* 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))# return serror for no connection
		if result == 0:
			print("port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\n Exiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("couldn't conect to server.")
	sys.exit()

