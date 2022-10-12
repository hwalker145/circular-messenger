# forgive me for coding this like a C program . . .

import socket as sk
import sys

# goes to Justin

IS_ORIGIN = False
DEST_ADDRESS = '10.220.20.215'

if len(sys.argv) < 4:
    raise RuntimeError('Not enough arguments.\n USAGE:\n ' +
                       '<Python executable> <codefile> <destination address> <name>')

send_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

if ~(IS_ORIGIN):
    receive_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    receive_socket.bind(('', 1234))
    message, addr = receive_socket.recvfrom(8192)

    send_socket.sendto((message.decode()).encode(), (DEST_ADDRESS, 1234))
else: 
    send_socket.sendto(str('Hello Salem!').encode(), (DEST_ADDRESS, 1234))