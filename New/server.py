import socket

#type of network
#tcp or udp
server_socket=socket.socket()
print('Socket created ')

#ip add and port
server_socket.bind(('localhost',9999))

server_socket.listen(3)
print('waiting for connection')

while True:
    clinet_socket,address_clinet=server_socket.accept()
    print('Connected with',address_clinet)
    clinet_socket.send(bytes('Welcome to telusko','utf-8'))
    clinet_socket.close()

    

