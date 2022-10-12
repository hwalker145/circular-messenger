import socket as sk

receiver_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
receiver_socket.bind(('', 1235))

message, addr = receiver_socket.recvfrom(8192)

print(message.decode())

receiver_socket.close()

