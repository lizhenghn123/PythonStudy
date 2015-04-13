#!/usr/bin/env python
#coding=utf-8
#date : 2015-04-12
from socket import *
from time import ctime

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

def create_simple_tcp_client():
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    while True:
        data = raw_input('> ')
        if not data:
            break
        tcpCliSock.send(data)
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print data

    tcpCliSock.close()
# End

def create_simple_tcp_client_test_socketserver():
    while True:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        data = raw_input('> ')
        if not data:
            break
        tcpCliSock.send('%s\r\n' % data)
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print data.strip()
        tcpCliSock.close()
# End

if __name__ == "__main__":
    #create_simple_tcp_client()
    create_simple_tcp_client_test_socketserver()