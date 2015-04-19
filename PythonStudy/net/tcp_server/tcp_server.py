#!/usr/bin/env python
#coding=utf-8
#date : 2015-04-12
from socket import *
from time import ctime

from SocketServer import TCPServer, StreamRequestHandler

from twisted import protocol, reactor

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

def create_simple_tcp_server():
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)

    while True:
        print 'waiting for connection...'
        tcpCliSock, addr = tcpSerSock.accept()
        print '...connected from:', addr

        tcpCliSock.settimeout(5)  # 5s
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            print("recv [%s]" % data)
            tcpCliSock.send('[%s] %s' % (ctime(), data))

        tcpCliSock.close()
    tcpSerSock.close()
# End

def create_tcp_server_by_socketserver():
    class MyRequestHandler(StreamRequestHandler):
        def handle(self):
            print '...connected from:', self.client_address
            self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))

    tcpServ = TCPServer(ADDR, MyRequestHandler)
    print 'waiting for connection...'
    tcpServ.serve_forever()
# End

if __name__ == "__main__":
   # create_simple_tcp_server()
    create_tcp_server_by_socketserver()
