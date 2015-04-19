#! /usr/bin/env python
# coding=utf-8
# author = lizheng
# date = 2015-04-17
import os, sys
import urlparse
import urllib
import urllib2
import getpass

url_site = "http:///www.python.org/doc/FAQ.html"
# url_site == urlparse.urlunparse(urlparse.urlparse(url_site))
tup = urlparse.urlparse(url_site)
url2 = urlparse.urlunparse(tup)
print(tup)
print(url2)
print("################")

document = urllib.urlopen("http://www.baidu.com")
print(document.geturl())
print(document.readline())
#print(document.readlines())
print("################")

tup = urllib.urlretrieve("http://www.baidu.com", "baidu.html")
tup = urllib.urlretrieve("https://ss0.bdstatic.com/5a21bjqh_Q23odCf/static/superplus/img/logo_white_ee663702.png", "baidu.jpg")
print(tup)
print("################")

req = urllib2.Request("http://www.baidu.com")
fd = urllib2.urlopen(req)
print("get url: %s" % fd.geturl())
info = fd.info()
for key,value in info.items():
    print("[header] %s = %s" % (key, value))
print(fd.readline())


# 带认证功能的请求
class TerminalPassword(urllib2.HTTPPasswordMgr):
    def find_user_password(self, realm, authuri):
        print("###### TerminalPassword ######")
        retval = urllib2.HTTPPasswordMgr.find_user_password(self, realm, authuri)
        if retval[0] == None and retval[1] == None:
            sys.stdout.write("Login required for %s at %s" & (realm, authuri))
            sys.stdout.write("Username: ")
            username = sys.stdin.readline().rstrip()
            password = getpass.getpass().rstrip()
            return (username, password)
        else:
            return retval

def test_urlauth():
    url_site = "http://passport.cnblogs.com/user/signin"
    req = urllib2.Request(url_site)
    opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler(TerminalPassword()))
    fd = opener.open(req)
    print("get url: %s" % fd.geturl())
    info = fd.info()
    for key,value in info.items():
        print("[header] %s = %s" % (key, value))
    print(fd.readline())

if __name__ == '__main__':
    test_urlauth()