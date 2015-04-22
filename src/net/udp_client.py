#!/usr/bin/env python
#coding=utf-8
#date : 2015-04-12
from socket import *

def create_udp_client():
    HOST = 'localhost'
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    udpCliSock = socket(AF_INET, SOCK_DGRAM)

    while True:
        data = raw_input('please input msg> ')
        if not data:
            break
        udpCliSock.sendto(data, ADDR)
        data, ADDR = udpCliSock.recvfrom(BUFSIZ)
        if not data:
            break
        print data

    udpCliSock.close()
# End

if __name__ == "__main__":
    create_udp_client()