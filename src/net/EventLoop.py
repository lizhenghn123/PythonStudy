#!/usr/bin/env python
# coding=utf-8
# author = lizheng
# date = 2015-04-24
# desc : 一个reactor模式的快速实现
import socket, traceback, os, sys, select

class Poller(object):
    eventdefaultmask_ = select.POLLERR | select.POLLHUP | select.POLLNVAL

    def __init__(self):
        self.poll_ = select.poll()
        
    def enableRead(self, fd):
        self.poll_.register(fd, select.POLLIN | self.eventdefaultmask_)
        
    def enableWrite(self, fd):
        self.poll_.register(fd, select.POLLOUT | self.eventdefaultmask_)
        
    def enableAll(self, fd):
        self.poll_.register(fd, select.POLLIN | select.POLLOUT | self.eventdefaultmask_)
        
    def disableAll(self, fd):
        self.poll_.unregister(fd)

    def loop_once(self):
        return self.poll_.poll()
# End class Poller

class EventLoop(object):
    EVENT_NONE  = 0
    EVENT_READ  = select.POLLIN
    EVENT_WRITE = select.POLLOUT
    EVENT_ALL = EVENT_READ | EVENT_WRITE
    
    def __init__(self, acceptsock):
        self.poller_ = Poller()
        self.acceptSock_ = acceptsock
        self.readBuffers_ = {}
        self.writeBuffers_ = {}
        self.sockets_ = { acceptsock.fileno() : acceptsock }
	self.updateSocket(self.acceptSock_, select.POLLIN)
    
    def fd2socket(self, fd):
        return self.sockets_[fd]
    
    def updateSocket(self, sock, event):
        if event == EventLoop.EVENT_ALL:
            self.poller_.enableAll(sock.fileno())
        elif event & EventLoop.EVENT_READ:
            self.poller_.enableRead(sock.fileno())
        elif event & EventLoop.EVENT_WRITE:
            self.poller_.enableWrite(sock.fileno())
        else:
            self.poller_.disableAll(sock.fileno())
       
    def handleAccept(self, sock):
        """Process a new connection"""
        fd = sock.fileno()
        # Start out watching both since there will be an outgoing message
        self.updateSocket(sock, EventLoop.EVENT_ALL)
        # Put a greeting message into the buffer
        self.writeBuffers_[fd] = "Welcome to the echoserver, %s\n" % str(sock.getpeername())
        self.readBuffers_[fd] = ""
        self.sockets_[fd] = sock
        
    def handleRead(self, sock):
        fd = sock.fileno()
        try:
            # Read the data and append it to the write buffer.
            self.readBuffers_[fd] += sock.recv(4096)
        except:
            self.handleClose(fd)

        self.updateSocket(sock, EventLoop.EVENT_ALL)

    def handleWrite(self, sock):
        fd = sock.fileno()
        if not len(self.writeBuffers_[fd]):
            # No data to send?  Take it out of the write list and return.
            self.updateSocket(sock, EventLoop.EVENT_NONE)
            return

        try:
            byteswritten = sock.send(self.writeBuffers_[fd])
        except:
            self.handleClose(fd)

        self.writeBuffers_[fd] = self.writeBuffers_[fd][byteswritten:]

        if not len(self.writeBuffers_[fd]):
            self.updateSocket(sock, EventLoop.EVENT_READ)
            
    def handleError(self, sock):
        self.handleClose(sock)

    def handleClose(self, sock):
        fd = sock.fileno()
        self.updateSocket(sock, EventLoop.EVENT_NONE)
        try:
            sock.close()
        except:
            pass

        del self.writeBuffers_[fd]
        del self.sockets_[fd]            

    def loop(self):
        while 1:
            results = self.poller_.loop_once()
            print('EventLoop has [%d] events!' % len(results))
            for fd, event in results:
                #print(fd, event)
                if fd == self.acceptSock_.fileno() and event == EventLoop.EVENT_READ:
                    try:
                        client, addr = self.acceptSock_.accept()
                        client.setblocking(0)
                        print('Get one connection from %s' % str(client.getpeername()))
                        fd = client.fileno()
                        self.handleAccept(client)
                    except Exception, e:
                        print("somethine error when accepting...[%s]" % str(e))
                        pass
                elif event == EventLoop.EVENT_READ:
                    self.handleRead(self.fd2socket(fd))
                elif event == EventLoop.EVENT_WRITE:
                    self.handleWrite(self.fd2socket(fd))
                else:
                    self.handleError(self.fd2socket(fd))
# End class EventLoop

def test_EventLoop():
    host = ''                               # Bind to all interfaces
    host = '127.0.0.1'                               # Bind to all interfaces
    port = 8888

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(5)
    s.setblocking(0)
    
    #print('server listening on[%s] .....' % str(s.getpeername()))
    print('server listening on[%d] .....' % port)
    el = EventLoop(s)
    try:
        el.loop()
    except Exception, e:
        print("somethine error when looping...[%s]" % str(e))
    
if __name__ == '__main__':
    test_EventLoop()
    print("######### GAME OVER #########")

