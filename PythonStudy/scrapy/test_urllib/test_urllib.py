#! /usr/bin/env python
# coding=utf-8
# author = lizheng
# date = 2015-04-17
import os
import urlparse
import urllib
import urllib2

url_site = "http:///www.python.org/doc/FAQ.html"
# url_site == urlparse.urlunparse(urlparse.urlparse(url_site))
tup = urlparse.urlparse(url_site)
url2 = urlparse.urlunparse(tup)
print(tup)
print(url2)


document = urllib.urlopen("http://www.baidu.com")
print(document.geturl())
print(document.readline())
#print(document.readlines())

tup = urllib.urlretrieve("http://www.baidu.com", "baidu.html")
tup = urllib.urlretrieve("https://ss0.bdstatic.com/5a21bjqh_Q23odCf/static/superplus/img/logo_white_ee663702.png", "baidu.jpg")
print(tup)
print("done!")