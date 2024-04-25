#import socket module
from socket import *
import sys # In order to terminate the program
import threading
import time
serverSocket = socket(AF_INET, SOCK_STREAM) # TCP 连接

#Prepare a sever socket
#Fill in start

serverPort = 12000
serverSocket.bind(('',serverPort))
serverSocket.listen(5)

def connect(connectionSocket, addr):
    while True:
        # connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024).decode()#Fill in start        #Fill in end
            filename = message.split()[1] # eg: Get /filename HTTP/1.1\r\n   get /filename
            f = open(filename[1:]) # get filename
            outputdata = f.read()#Fill in start    #Fill in end
            #Send one HTTP header line into socket
            #Fill in start
    
           # head = message.split()[2]
           # head = head.rstrip("\r\n")
           # head += " 200 OK\r\n"
            parts = message.split()
            # 获取HTTP版本
            http_version = parts[2] if len(parts) > 2 else 'HTTP/1.1'
            header = '{} 200 OK\r\n'.format(http_version)
            #header += 'Content-Length: {}\r\n'.format(len(outputdata))
            header += '\r\n'
    
            connectionSocket.send(header.encode())
    
            #Fill in end
            #Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())
    
            connectionSocket.close()
        except IOError:

            parts = message.split()
            http_version = parts[2] if len(parts) > 2 else 'HTTP/1.1'
         
            header = '{} 404 Not Found\r\n\r\n'.format(http_version)
            connectionSocket.send(header.encode())
        connectionSocket.close()

def create_connect_thread():
    connectionSocket, addr = serverSocket.accept()
    t = threading.Thread(target=connect,args=(connectionSocket, addr))
    t.start()
    #t.join()

if __name__ == "__main__":
    while True:
        print('Ready to serve...')
        create_connect_thread()


serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding dat

