import socket
import sys

#creates a varaible to store a socket on
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Set the port to the one you want to work with for the drones
port = 6969
#Sets the s varible socket to allow traffic from assigned destination and port
s.bind(('0.0.0.0', port))
#Prints out a message deliveried over over the pocket on the socket
print('Drone #1 listening on port ' + str(port))
#Sets the s varible socket is waiting for something to connect
s.listen(5)

#Loop that allows for continuous traffic to be sent over the port
while True:
  c, addr = s.accept()
  print (c.recv(1024).decode())
  c.close()
