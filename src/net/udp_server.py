#!/usr/bin/env python
#coding=utf-8
#date : 2015-04-12
from socket import *
from time import ctime

def create_udp_server():
    HOST = ''
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    udpSerSock = socket(AF_INET, SOCK_DGRAM)
    udpSerSock.bind(ADDR)

    while True:
        print 'UDP Server waiting for message...'
        data, addr = udpSerSock.recvfrom(BUFSIZ)
        udpSerSock.sendto('[%s] %s' % (
            ctime(), data), addr)
        print '...received from and returned to:', addr
    udpSerSock.close()
# End

if __name__ == "__main__":
    create_udp_server()