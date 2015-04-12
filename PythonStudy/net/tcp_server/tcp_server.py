#!/usr/bin/env python
#coding=utf-8
#date : 2015-04-12
from socket import *
from time import ctime

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

        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data:
                break
            print("recv [%s]" % data)
            tcpCliSock.send('[%s] %s' % (ctime(), data))

        tcpCliSock.close()
    tcpSerSock.close()
# End

if __name__ == "__main__":
    create_simple_tcp_server()