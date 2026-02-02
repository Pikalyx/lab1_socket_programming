from socket import *

serverPort = 10001
serverName = "Server of Diego"
serverInterger = "42"

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))

serverSocket.listen(1)
isOn = True
while isOn:
    print("The server is ready to receive.")
    connectionSocket, addr = serverSocket.accept()
    print("Connection established with client")
    
    #recieve client name and interger
    clientName, interger = connectionSocket.recv(1024).decode().split(',')
    print("Client name received: " + clientName)
    print("Interger received: " + interger)
    
    try:
        interger = int(interger.strip())
        if interger >= 100 or interger <= 1:
            print("Invalid integer received, closing connection.")
            connectionSocket.close()
            turnOff = input("Turn off server? (y/n): ")
            if turnOff.lower() == 'y':
                isOn = False
                print("Shutting down server.")
            continue
    except ValueError:
        print(interger)
        print("Error: received data is not a valid integer")
        connectionSocket.close()
        continue
    
    print("Raw interger received: '" + str(interger) + "'")
    
    message = serverName + "," + serverInterger
    connectionSocket.send(message.encode())
    print("Sent server name and integer to client")
    
    
    '''
    This is deprecated code that ran into several issues such as 
        value error, 
        packets being lost completely,
        bad formatting when sending multiple pieces of data separately.
    It has been replaced with a single send and recv using a comma to separate values.
    
    Would be nice to have a protocol for sending multiple pieces of data in a specific format.
    '''
    # # sends server name
    # print("Sending server name...")
    # connectionSocket.send(serverName.encode())
    # print("Sent server name")
    # # sends server interger
    # print("Sending server integer...")
    # connectionSocket.send(serverInterger.encode())
    # print("Sent server integer")
    
    #close connection
    connectionSocket.close()
    turnOff = input("Turn off server? (y/n): ")
    if turnOff.lower() == 'y':
        isOn = False
        print("Shutting down server.")
