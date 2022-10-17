import socket as sk

# goes to 'Justin'

IS_ORIGIN = True
DEST_ADDRESS = '10.220.94.124'

send_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

if not IS_ORIGIN:
    receive_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    receive_socket.bind(('10.220.49.117', 1234))

    receive_socket.listen(10)
    cSocket, addr = receive_socket.accept()

    message = receive_socket.recv(10)

    send_socket.connect((DEST_ADDRESS, 1234))
    send_socket.sendall(message)
else:
    send_socket.connect(('10.220.49.117', 1239))
    send_socket.sendall(b'Hello Salem!')