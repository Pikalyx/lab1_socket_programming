from socket import *

serverPort = 10001
serverName = "Server of Diego"
serverInterger = "42"

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)
print("The server is ready to receive.")
while True:
    connectionSocket, addr = serverSocket.accept()
    print("Connection established with client")
    
    #recieve client name and interger
    clientName = connectionSocket.recv(1024).decode()
    print("Raw client name received: '" + clientName + "'")
    print("Client name length: " + str(len(clientName)))
    
    interger = connectionSocket.recv(1024).decode()
    print("Raw interger received: '" + interger + "'")
    print("Interger length: " + str(len(interger)))
    
    # sends server name
    print("Sending server name...")
    connectionSocket.send(serverName.encode())
    print("Sent server name")
    # sends server interger
    print("Sending server integer...")
    connectionSocket.send(serverInterger.encode())
    print("Sent server integer")
    
    #close connection
    connectionSocket.close()
