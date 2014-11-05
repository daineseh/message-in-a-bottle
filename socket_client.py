#! /usr/bin/env python2

import sys
from socket import socket, AF_INET, SOCK_STREAM

def main():
    if len(sys.argv) < 3:
        print '''
        usage : socket_client SERVER_IP_ADDR SEND_STRING
        '''
        return

    s = socket(AF_INET, SOCK_STREAM)
    s.connect((sys.argv[1], 2000))
    s.send(sys.argv[2])
    print s.recv(8192)


if __name__ == '__main__':
    main()
