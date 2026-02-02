from socket import *

# This is the data we are sending to the server
interger = input("Enter an interger from 1 - 100")
name = "Client of Diego"

message = name + "," + interger

#this is the server data
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(("172.19.117.189", serverPort))

#sends data then stops sending
clientSocket.send(message.encode())
print("Sent client name")
print("Sent interger")

clientSocket.shutdown(SHUT_WR)
print("Finished sending data")

#receives server data and displays it
try:
    serverName, serverInterger = clientSocket.recv(1024).decode().split(',')
    print("Received server name: " + serverName)
    print("Received server integer: " + serverInterger)
except ValueError:
    print("Error: Could not decode received data properly.")

clientSocket.close()