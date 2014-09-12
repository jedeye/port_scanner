#!/usr/bin/python

# Import libraries required

import sys
import socket
import subprocess

# Clear the screen ready to display output
subprocess.call('clear', shell=True)

# Parse user input
ip_address = sys.argv[1]


try:
	for port in range(1,1234):
		create_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		test = create_socket.connect_ex((ip_address, port))
		if test == 0:
			print "Found open port number %d" %port
		create_socket.close()
except socket.error:
	print "Could not connect to server, make sure you entered the IP address correctly as an argument when starting the post scanner. \n Exiting...."
	sys.exit()

print "Scanning complete!"