#! /usr/bin/env python
# coding=utf-8
# author = lizheng
# date = 2015-04-19
import time
import threading
import SocketServer     # ThreadingTCPServer, ForkingTCPServer
import BaseHTTPServer   # HTTPServer, BaseHTTPRequestHandler
import SimpleHTTPServer # SimpleHTTPRequestHandler
starttime = time.time()
serveraddr = ('', 8888)

# BaseHTTPRequestHandler : send_response, send_header, end_headers, do_XXX
class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    """Definition of the request handler."""
    def _writeheaders(self, doc):
        """Write the HTTP headers for the document.  If there's no
        document, send a 404 error code; otherwise, send a 200 success code."""
        if doc is None:
            self.send_response(404)
        else:
            self.send_response(200)
        # Always serve up HTML for now.
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def _getdoc(self, filename):
        """Handle a request for a document, returning one of two different pages as appropriate."""
        global starttime
        if filename == '/':
            return """<html><head><title>Sample Page</title></head><body>This is a sample page.
            You can also look at the <a href="stats.html">server statistics</a>.</body></html>"""
        elif filename == '/stats.html':
            return """<html><head><title>Statistics</title></head><body>This server has 
            been running for %d seconds.</body></html>""" % int(time.time() - starttime)
        else:
            return None
    def do_HEAD(self):
        """Handle a request for headers only"""
        doc = self._getdoc(self.path)
        self._writeheaders(doc)
    def do_GET(self):
        """Handle a request for headers and body"""
        print("Handling with thread %s" % threading.currentThread().getName())
        doc = self._getdoc(self.path)
        self._writeheaders(doc)
        if doc is None:
            self.wfile.write("""<html><head><title>Not Found</title></head><body>
            The requested document '%s' was not found.</body></html>""" % self.path)
        else:
            self.wfile.write(doc)
        
def httpserver_iterative(): 
    return BaseHTTPServer.HTTPServer(serveraddr, RequestHandler)
def httpserver_threading():
    class ThreadingHttpServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
        pass
    return ThreadingHttpServer(serveraddr, RequestHandler)
def httpserver_simple():
    return BaseHTTPServer.HTTPServer(serveraddr, SimpleHTTPServer.SimpleHTTPRequestHandler)
if __name__ == '__main__':
    print("start server at %s ....." % str(serveraddr))
    #httpserver_iterative().serve_forever()
    #httpserver_threading().serve_forever()
    httpserver_simple().serve_forever()