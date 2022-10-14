import socket as sk

receiver_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
receiver_socket.bind(('', 1235))

receiver_socket.listen(1)
cSocket, addr = receiver_socket.accept()

message = receiver_socket.recv(8192)

print(message.decode())

receiver_socket.close()