import socket
import threading


# create a socket object
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#get local machine name
host = socket.gethostname() 
ip = socket.gethostbyname(socket.gethostname())

serverPort = 12000 # server port

#bind to the port
serverSocket.bind((host,serverPort))

#only 1 request can be handle
serverSocket.listen(1)

print("The server is ready to receive\n")
print("Started listening on ",ip," port: ",serverPort )
connectionSocket, addr = serverSocket.accept() # moved it up
while True:

	print("Got a connection from %s" % str(addr))
	
	data = connectionSocket.recv(1024).decode()
	if not data:
		break
	print("from connected user: "+str(data))

	data = str(data).upper()
	print("sending: "+str(data))
	connectionSocket.send(data.encode())
	
connectionSocket.close()
input("Press ENTER to exit")