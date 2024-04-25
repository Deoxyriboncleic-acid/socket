from socket import *
import sys

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]
#serverName = '123.60.221.93'
#serverPort = 12000
#filename = 'c.html'

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


header = 'GET /{} HTTP/1.1'.format(filename)
header += '\r\n'
# print(header)

clientSocket.send(header.encode())

modifiedfilename = clientSocket.recv(1024).decode()
#print(modifiedfilename)


with open(filename, 'w') as file:
    file.write(modifiedfilename)
with open(filename, 'r') as file:
    lines = file.readlines()
with open(filename, 'w') as file:
    file.writelines(lines[2:-1])


clientSocket.close()


