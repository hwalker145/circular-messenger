# socket
import socket as sk

# is the process the 
# original process (put True) or a 
# forwarding process (put False)
IS_ORIGIN = False

# destination info
DEST_ADDRESS = '10.220.49.117'
DEST_SOCKET = 1236

# source info
RECV_ADDRESS = '10.220.49.117'
RECV_SOCKET = 1235

# initializing the client socket
send_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
send_socket.connect((DEST_ADDRESS, DEST_SOCKET))

if not IS_ORIGIN:
    #initializing the server socket
    receive_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    receive_socket.bind((RECV_ADDRESS, RECV_SOCKET))

    # waiting and accepting the connection
    receive_socket.listen(1)
    cSocket, addr = receive_socket.accept()

    # recv call to grab the message
    message = cSocket.recv(60)

    # close socket once message is received
    receive_socket.close()

    # forwarding the message
    send_socket.sendall(message)
else:
    # sending the message 'Hello Salem'
    send_socket.sendall(b'Hello Salem!')

    # close socket once message is sent
    send_socket.close()