#! /usr/bin/env python
# coding=utf-8
# author = lizheng
# date = 2015-04-17
import urllib
import urllib2

# 使用python简单调用www.tuling123.com提供的聊天、问答接口

# http://www.tuling123.com
MY_KEY='02286ed1a6b50fb5de05fcad202093e4'
url = 'http://www.tuling123.com/openapi/api?key=' + MY_KEY + "&info="
#http://www.tuling123.com/openapi/wechatapi?key=02286ed1a6b50fb5de05fcad202093e4
 


#用urllib2库的Request方法获取内容
def test_tuling123():
    query = {'key': MY_KEY, 'info': '北京天气'}
    data = urllib.urlencode(query)
    req = urllib2.Request('http://www.tuling123.com/openapi/api', data)
    f = urllib2.urlopen(req)
    print(f.read())

# 使用urllib库的urlopen通过get方式获取内容
def have_a_joke_with_tuling123():
    while(True):
        question = raw_input("请输入你要查询的问题：>>>")
        if not question:
            print("haha, gameover")
            break
        requrl = url + question              # "明天北京到南京的航班"
        requrl = requrl.decode("gb18030")    # 在windows下输入的一般是gbk编码，先decode成unicode
        requrl = requrl.encode("utf-8")      # 再encode成utf-8
        print(requrl)
        docu = urllib.urlopen(requrl)
        print(docu.read())

if __name__ == "__main__":
    print("########  ########")
    test_tuling123()
    print("########  ########")
    
    for i in range(5):
        requrl = url + '讲个笑话'
        print(urllib.urlopen(requrl).read())
    
    print("########  ########")
    have_a_joke_with_tuling123()
