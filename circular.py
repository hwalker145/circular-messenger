import socket as sk

# goes to 'PERSON'

IS_ORIGIN = False
DEST_ADDRESS = '10.220.49.117'
RECV_ADDRESS = '10.220.49.117'
DEST_SOCKET = 1236
RECV_SOCKET = 1235

send_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

if not IS_ORIGIN:
    receive_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    receive_socket.bind((RECV_ADDRESS, RECV_SOCKET))

    receive_socket.listen(1)
    cSocket, addr = receive_socket.accept()

    message = cSocket.recv(60)

    send_socket.connect((DEST_ADDRESS, DEST_SOCKET))
    send_socket.sendall(message)
else: 
    send_socket.connect((DEST_ADDRESS, DEST_SOCKET))
    send_socket.sendall(str('Hello Salem!').encode())