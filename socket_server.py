#! /usr/bin/env python2

from SocketServer import BaseRequestHandler, TCPServer
import socket

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print 'Got connection from', self.client_address
        ip = socket.gethostbyname(socket.gethostname())
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            print 'Received :', msg
            msg += (' (%s replied)' % ip)
            self.request.send(msg)

if __name__ == '__main__':
    serv = TCPServer(('', 2000), EchoHandler)
    serv.serve_forever()
