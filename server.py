from email import message
from http import client
from multiprocessing import connection
import socket
# AF_INET because IPV4, SOCK_STREAM specifies what type of connection, Eg TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#store the host name
host = socket.gethostname()
# host = '192.168.192.1' if u want to this specifically


# What port to listen
port = 444

#bind the host name, address etc to the object
serversocket.bind((host, port))

#we need to listen to connections from the client , ie starting the tcp listener    

serversocket.listen(3) #how many computers to connect from

#how many requests to allow
while True:
    #start the connection
    clientsocket, address = serversocket.accept()
    print("Received connection from %s " % str(address))
    message = 'Thank you for connecting to the server' + '\r\n'
    clientsocket.send(message.encode('ascii'))
    #close the client socket, not server socket
    clientsocket.close()