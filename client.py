from socket import *

# This is the data we are sending to the server
interger = input("Enter an interger from 1 - 100")
name = "Client of Diego"

#this is the server data
serverPort = 10001

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(("localhost", serverPort))

clientSocket.send(name.encode())
print("Sent client name")
clientSocket.send(interger.encode())
print("Sent interger")
clientSocket.shutdown(SHUT_WR)
print("Finished sending data")

serverName = clientSocket.recv(1024).decode()
print("Received server name: " + serverName)
serverInterger = clientSocket.recv(1024).decode()
print("Received server integer: " + serverInterger)

print("Server name: " + serverName)
print("Server interger: " + serverInterger)

clientSocket.close()