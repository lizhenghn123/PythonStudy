#! /usr/bin/env python
# coding=utf-8
# author = lizheng
# date = 2015-04-16

import time
import socket
from twisted.internet import protocol, reactor

# 安装twisted，直接执行：easy_install twisted
# see :http://blog.csdn.net/jonahzheng/article/details/8987333

HOST = "localhost"
PORT = 8888

class TcpServerProtocol(protocol.Protocol):
    def connectionMade(self):  # 有客户端连接过来的时候被调用
        clnt = self.clnt = self.transport.getPeer().host
        print("... connected from %s", clnt)
    def dataReceived(self, data):  # 在客户端通过网络发送数据过来时被调用
        self.transport.write("[%s] %s" % (ctime(), data))

def runTwistedReactorServer():
    factory = protocol.Factory()
    factory.protocol = TcpServerProtocol
    print("waiting for connection...")

    #每次有连接进来的时候，它会“生产”一个 protocol 对象。
    #然后在 reactor 中安装一个 TCP监听器以等待服务请求。
    #当有请求进来时，创建一个 TSServProtocol 实例来服务那个客户。 
    reactor.listenTCP(PORT, factory)
    reactor.run()  

class TcpClientProtocol(protocol.Protocol):
    def connectionMade(self):
        self.sendData()
    def dataReceived(self, data):
        print("recv from server: %s" % data)
        self.sendData()
    def sendData(self):
        data = raw_input("please input some msg>>>")
        if data:
            print("send to server : %s" % data)
            self.transport.write(data)
        else:
            self.transport.loseConnection()  # 关闭套接字，触发下面的clientConnectionLost调用
class TcpClientFactory(protocol.ClientFactory):
    protocol = TcpClientProtocol
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason : reactor.stop()
    
def runTwistedReactorClient():
    reactor.connectTCP(HOST, PORT, TcpClientFactory())
    reactor.run()


if __name__ == "__main__":
    funcs = {'s' : runTwistedReactorServer, 'c' : runTwistedReactorClient}
    choice = raw_input("run server(s) or client(c)? enter >>>").strip().lower()[0]
    funcs[choice]()
