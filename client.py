from socket import *

# This is the data we are sending to the server
interger = input("Enter an interger from 1 - 100: ")
name = "Client of Diego"

message = name + "," + interger

#this is the server data
serverPort = 10001

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(("localhost", serverPort))

#sends data then stops sending
clientSocket.send(message.encode())
clientSocket.shutdown(SHUT_WR)
print("Sent client name: " + name)
print("Sent interger: " + interger)
print("Finished sending data")

#receives server data and displays it
serverName, serverInterger = clientSocket.recv(1024).decode().split(',')
print("Received server name: " + serverName)
print("Received server integer: " + serverInterger)

'''
This is deprecated code that ran into several issues such as 
    value errors, 
    packets being lost completely,
    bad formatting when sending multiple pieces of data separately.
It has been replaced with a single send and recv using a comma to separate values.

Would be nice to have a protocol for sending multiple pieces of data in a specific format.
'''
# #receives server data and displays it
# serverName = clientSocket.recv(1024).decode()
# print("Received server name: " + serverName)
# serverInterger = clientSocket.recv(1024).decode()
# print("Received server integer: " + serverInterger)


if serverInterger.isdigit() and interger.isdigit():
    print("Sum of client and server integers: " + str(int(interger) + int(serverInterger)))
else:
    print("Error: One of the received integers is not valid.")

clientSocket.close()