#!usr/bin/env python2.7

# import socket module
from socket import *
import ssl

# Create welcome socket with IPv4 and TCP packet
serverSocket = socket(AF_INET, SOCK_STREAM)

# define server port and address
serverPort = 3216
serverAddress = 'localhost'

# Wait for client connection
serverSocket.bind((serverAddress, serverPort))
serverSocket.listen(1)

# Wrap server socket as an ssl socket
sslSocket = ssl.wrap_socket(serverSocket, certfile="newserver.pem", do_handshake_on_connect=True, ciphers="AES256-GCM-SHA384")
# Process client requests one at a time
while True:

    # Establish the connection
    print "Ready to serve..."
    connectionSocket, addr = sslSocket.accept()

    try:
        # store client request in message
        message = (connectionSocket.recv(1024)).decode('utf-8')

        # Parse client request and open file
        filename = message.split()[1]
        f = open(filename[1:], 'rb')

        # Store file data in outputdata
        outputdata = f.read()


        # Send a 200 OK response to the client if file is found
        connectionSocket.send("\nHTTP/1.1 200 OK\n\n")

        # Send the content of the requested file to the client
        connectionSocket.send(outputdata)
        connectionSocket.send(b'\r\n')

        # Close file
        f.close()

        # Close the client connection socket
        connectionSocket.shutdown(SHUT_RDWR)
        connectionSocket.close()

    except IOError:

        # Print error message to server
        print "404 Not Found"

        # File not found header response
        connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
        connectionSocket.send(b'<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n')

        # Close client socket
        connectionSocket.shutdown(SHUT_RDWR)
        connectionSocket.close()

# Close server socket
sslSocket.close()
