import socket as sk

receiver_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
receiver_socket.bind(('10.220.49.117', 1239))

receiver_socket.listen(10)
cSocket, addr = receiver_socket.accept()

message = receiver_socket.recv(60)

print(message.decode())

receiver_socket.close()