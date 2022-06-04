from email import message
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

clientsocket.connect((host, port))
message = clientsocket.recv(1024) # sets max amt of data recieved by client

clientsocket.close()
print(message.decode('ascii'))