#!/usr/bin/env python
#coding=utf-8
#date : 2015-04-12
from socket import *
from time import ctime

from SocketServer import TCPServer, StreamRequestHandler, ThreadingMixIn, ForkingMixIn

#from twisted import protocol, reactor

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

class TimeRequestHandler(StreamRequestHandler):
    def handle(self):   #rfile和wfile是由socket.makefile()创建的文件对象
        print("Connection from", self.client_address)
        req = self.rfile.readline().strip()
        if req == "asctime":
            result = time.asctime()
        elif req == "seconds":
            result = str(int(time.time()))
        elif req == "rfc822":
            result = time.strftime("%a, %d %b %Y %H:%M:%S +0000",
                     time.gmtime())
        else:
            result = """Unhandled request.  Send a line with one of the
following words:

asctime -- for human-readable time
seconds -- seconds since the Unix Epoch
rfc822  -- date/time in format used for mail and news posts"""
        self.wfile.write(result + "\n")

class ThreadingTimeServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = 1           # 地址复用。只需要设置即可
    #address_family = socket.AF_INET6  # 用于支持IPv6
class ForkingTimeServer(ForkingMixIn, TCPServer):
    allow_reuse_address = 1
def test_ThreadingTimeServer():
    srvr = ThreadingTimeServer(ADDR, TimeRequestHandler)
    srvr.serve_forever()

if __name__ == "__main__":
   # create_simple_tcp_server()
   # create_tcp_server_by_socketserver()
    test_ThreadingTimeServer()