# forgive me for coding this like a C program . . .

import socket as sk
import sys

IS_ORIGIN = True

destination_address = sys.argv[1]
name = sys.argv[2]

if len(sys.argv) < 4:
    raise RuntimeError('Not enough arguments.\n USAGE:\n ' +
                       '<Python executable> <codefile> <destination address> <name>')

send_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

if ~(IS_ORIGIN):
    receive_socket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
    receive_socket.bind(('', 1234))
    message, addr = receive_socket.recvfrom(8192)

    send_socket.sendto((message.decode() + ' ' + name).encode(), (destination_address, 1234))
else: 
    send_socket.sendto(name.encode(), (destination_address, 1234))