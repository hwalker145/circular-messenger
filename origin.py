import socket as sk

# goes to 'PERSON'

IS_ORIGIN = False
DEST_ADDRESS = 'INSERT HERE'

send_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

if ~(IS_ORIGIN):
    receive_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    receive_socket.bind(('', 1234))

    receive_socket.listen(1)
    cSocket, addr = receive_socket.accept()

    message = receive_socket.recv(8192)

    send_socket.connect((DEST_ADDRESS, 1234))
    send_socket.sendall(message)
else: 
    send_socket.connect((DEST_ADDRESS, 1234))
    send_socket.sendall(str('Hello Salem!').encode())