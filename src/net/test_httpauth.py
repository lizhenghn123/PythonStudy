#! /usr/bin/env python
# coding=utf-8
# author = lizheng
# date = 2015-04-17
import os
import re
import sys
import time
import urlparse
import urllib
import urllib2
import getpass
import httplib
import cookielib
import getpass

def just_visit_url(url):
    req = urllib2.Request(url)
    fd = urllib2.urlopen(req)
    print("get url: %s" % fd.geturl())
    info = fd.info()
    for key,value in info.items():
        print("[header] %s = %s" % (key, value))
    print(fd.read())

# 带认证功能的请求(有问题)
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

def test_urlauth():  # (有问题)
    url_site = "https://passport.baidu.com/?login"
    postdata=urllib.urlencode({'username':'XXXX','password':'XXXXX'})
    req = urllib2.Request(url_site)
    opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler(TerminalPassword()))
    fd = opener.open(req)
    print("get url: %s" % fd.geturl())
    info = fd.info()
    for key,value in info.items():
        print("[header] %s = %s" % (key, value))
    print(fd.readline())

def auto_login_renren(url,user,password):    
    login_page = "http://www.renren.com/PLogin.do"
    try:
        cj = cookielib.CookieJar()
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
        data = urllib.urlencode({"email":user,"password":password})
        #以post的方法访问登陆页面，访问之后cookieJar会自定保存cookie
        opener.open(login_page,data)
        #以带cookie的方式访问页面
        op=opener.open(url)
        #读取页面源码
        data= op.read()
        return data
    except Exception,e:
        print str(e)

def auto_login_baidu(url, user, pwd):
    URL_BAIDU_INDEX = u'http://www.baidu.com/';
    #https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=true 也可以用这个
    URL_BAIDU_TOKEN = 'https://passport.baidu.com/v2/api/?getapi&tpl=pp&apiver=v3&class=login';
    URL_BAIDU_LOGIN = 'https://passport.baidu.com/v2/api/?login';

    #设置cookie
    cookie=cookielib.CookieJar()
    cj=urllib2.HTTPCookieProcessor(cookie)
    #cookieJar作为参数，获得一个opener的实例
    opener=urllib2.build_opener(cj)   # opener=urllib2.build_opener(request,cj)
    urllib2.install_opener(opener)
    reqReturn = urllib2.urlopen(URL_BAIDU_INDEX)

    #获取token
    tokenReturn = urllib2.urlopen(URL_BAIDU_TOKEN);
    matchVal = re.search(u'"token" : "(?P<tokenVal>.*?)"',tokenReturn.read());
    tokenVal = matchVal.group('tokenVal');

    #构造登录请求参数，该请求数据是通过抓包获得，对应https://passport.baidu.com/v2/api/?login请求
    postData = {
        'username' : user,
        'password' : pwd,
        'u' : 'https://passport.baidu.com/',
        'tpl' : 'pp',
        'token' : tokenVal,
        'staticpage' : 'https://passport.baidu.com/static/passpc-account/html/v3Jump.html',
        'isPhone' : 'false',
        'charset' : 'UTF-8',
        'callback' : 'parent.bd__pcbs__ra48vi'
        };
    postData = urllib.urlencode(postData);

    #发送登录请求
    loginRequest = urllib2.Request(URL_BAIDU_LOGIN,postData);
    loginRequest.add_header('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8');
    loginRequest.add_header('Accept-Encoding','gzip,deflate,sdch');
    loginRequest.add_header('Accept-Language','zh-CN,zh;q=0.8');
    loginRequest.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36');
    loginRequest.add_header('Content-Type','application/x-www-form-urlencoded');
    sendPost = urllib2.urlopen(loginRequest);
    
    # 以带cookie的方式访问页面
    hi_html=opener.open(url)
    print(hi_html.read())
    return hi_html

if __name__ == '__main__':
    #test_urlauth()
    #print(auto_login_renren('http://www.renren.com/home','XXXXX','XXXX'))
    print(auto_login_baidu('https://passport.baidu.com/v2/account/password', 'XXXX', 'XXXX'))