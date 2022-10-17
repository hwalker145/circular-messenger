# socket
import socket as sk

# source info
RECV_ADDRESS = '10.220.49.117'
RECV_SOCKET = 1236

# initializing the server socket
receiver_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
receiver_socket.bind((RECV_ADDRESS, RECV_SOCKET))

# accept tcp connection
receiver_socket.listen(1)
cSocket, addr = receiver_socket.accept()

# grab message
message = cSocket.recv(60)

print(message.decode())

# close socket once message is received
receiver_socket.close()