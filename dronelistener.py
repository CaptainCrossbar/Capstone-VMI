import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port 6969
s.bind(()'0.0.0.0', port))
print('Drone Listening on port ' + str(port))
s.listen(5)

while True:
  c, addr = s.accept()
  print (c.recv(1024).decode())
  c.close()
