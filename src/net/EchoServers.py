#!/usr/bin/env python
# coding=utf-8
# author = lizheng
# date = 2015-04-16
import socket
from SocketServer import BaseRequestHandler, TCPServer, ForkingTCPServer, ThreadingTCPServer
import select  # for select.poll(epoll)

listen_address = ("0.0.0.0", 8888)

def handle(client_socket, client_address):
    while True:
        data = client_socket.recv(4096)
        if data:
            sent = client_socket.send(data)    # sendall?
        else:
            print "disconnect", client_address
            client_socket.close()
            break
# socket.socket
def test_echoserver_iterative():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(listen_address)
    server_socket.listen(5)
    while True:
        (client_socket, client_address) = server_socket.accept()
        print "got connection from", client_address
        handle(client_socket, client_address)
        
class EchoHandler(BaseRequestHandler):
    def handle(self):
        print "got connection from", self.client_address
        while True:
            data = self.request.recv(4096)
            if data:
                sent = self.request.send(data)    # sendall?
            else:
                print "disconnect", self.client_address
                self.request.close()
                break
            
class EchoHandlerSingle(EchoHandler):
    pass
class EchoHandlerThread(EchoHandler):
    pass
class EchoHandlerFork(EchoHandler):
    pass

#  SocketServer. TCPServer       
def test_echoserver_single():
    server = TCPServer(listen_address, EchoHandlerSingle)
    server.serve_forever()
#  SocketServer. ThreadingTCPServer 
def test_echoserver_thread():
    server = ThreadingTCPServer(listen_address, EchoHandlerThread)
    server.serve_forever()
#  SocketServer. ForkingTCPServer 
def test_echoserver_fork():
    server = ForkingTCPServer(listen_address, EchoHandlerFork)
    server.serve_forever()

# select.poll(epoll)
def test_echoserver_poll():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(listen_address)
    server_socket.listen(5)
    # server_socket.setblocking(0)
    poll = select.poll() # epoll() should work the same
    poll.register(server_socket.fileno(), select.POLLIN)

    connections = {}
    while True:
        events = poll.poll(10000)  # 10 seconds
        for fileno, event in events:
            if fileno == server_socket.fileno():
                (client_socket, client_address) = server_socket.accept()
                print "got connection from", client_address
                # client_socket.setblocking(0)
                poll.register(client_socket.fileno(), select.POLLIN)
                connections[client_socket.fileno()] = client_socket
            elif event & select.POLLIN:
                client_socket = connections[fileno]
                data = client_socket.recv(4096)
                if data:
                    client_socket.send(data) # sendall() partial?
                else:
                    poll.unregister(fileno)
                    client_socket.close()
                    del connections[fileno]
# select.reactor
def test_echoserver_reactor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(listen_address)
    server_socket.listen(5)
    # serversocket.setblocking(0)

    poll = select.poll() # epoll() should work the same
    connections = {}
    handlers = {}

    def handle_input(socket, data):
        socket.send(data) # sendall() partial?
        for (fd, other_socket) in connections.iteritems():
            if other_socket != socket:
                other_socket.send(data)   # 相当于群聊，把一个人消息转发给其他所有人
    def handle_request(fileno, event):
        if event & select.POLLIN:
            client_socket = connections[fileno]
            data = client_socket.recv(4096)
            if data:
                handle_input(client_socket, data)
            else:
                poll.unregister(fileno)
                client_socket.close()
                del connections[fileno]
                del handlers[fileno]

    def handle_accept(fileno, event):
        (client_socket, client_address) = server_socket.accept()
        print "got connection from", client_address
        # client_socket.setblocking(0)
        poll.register(client_socket.fileno(), select.POLLIN)
        connections[client_socket.fileno()] = client_socket
        handlers[client_socket.fileno()] = handle_request

    poll.register(server_socket.fileno(), select.POLLIN)
    handlers[server_socket.fileno()] = handle_accept

    while True:
        events = poll.poll(10000)  # 10 seconds
        for fileno, event in events:
            handler = handlers[fileno]
            handler(fileno, event)
        
funcs = {
    '0' : test_echoserver_iterative,
    '1' : test_echoserver_single,
    '2' : test_echoserver_thread,
    '3' : test_echoserver_fork,
    '4' : test_echoserver_poll,
    '5' : test_echoserver_reactor
    }

if __name__ == "__main__":

    choice = raw_input('''  Choose a echo server model :
0. echo_socket
1. echoserver_single
2. echoserver_thread
3. echoserver_fork
4. echoserver_poll
5. echoserver_reactor

Enter choice: ''').strip().lower()[0]

    funcs[choice]()


