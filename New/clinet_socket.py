import socket

clinet_socket=socket.socket()

clinet_socket.connect(('localhost',9999))


print(clinet_socket.recv(1024).decode())



