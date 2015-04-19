#! /usr/bin/env python
# coding=utf-8
# author = lizheng
# date = 2015-04-19
import sys, socket, struct

# getaddrinfo: 返回的是五元组： (family, socktpye, proto, canoname, sockaddr)
res = socket.getaddrinfo("www.baidu.com", None)
print(res)
#print(socket.getaddrinfo("www.zce45456-nonexist.com", None)


# gethostbyaddr
print(socket.gethostbyaddr("127.0.0.1"))
#print(socket.gethostbyaddr("127.0.0.2"))
print(socket.gethostbyaddr("61.135.169.125"))

# 本机字节序和网络字节序的转换（H/I分别用于16/32位整数, !表示使用网络字节序进行编解码）
def htons(num):
    return struct.pack('!H', num)
def htonl(num):
    return struct.pack('!I', num)
def ntohs(data):
    return struct.unpack('!H', data)[0]
def ntohl(data):
    return struct.unpack('!I', data)[0]

def test_htons():
    def sendstr(data):
        return htonl(len(data)) + data
    print("enter a string")
    strs = sys.stdin.readline().rstrip()
    print(repr(sendstr(strs)))