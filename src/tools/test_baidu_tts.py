#! /usr/bin/env python
# -*- coding=utf-8 -*-
# date = 2015-06-19
import os, sys,time
import urllib

# 测试百度TTS云服务： 直接访问无需注册
# http://tts.baidu.com/text2audio?lan=zh&ie=UTF-8&text=中华人民共和国
# lan = 中文, zh; 英语, en; 意大利语, it; 俄语, ru; 法语, fra; 韩语, kor; 德语, de; 日语, jp; 
# 荷兰语, nl; 希腊语, el; 粤语, yue; 西班牙语, spa;
# 结论：效果还不错，缺少更多可调参数(男声女声，声速)

def baidu_tts(text, filename = None):
    # url = http://tts.baidu.com/text2audio?lan=zh&ie=UTF-8&text=text
    url = "http://tts.baidu.com/text2audio?lan=zh&ie=UTF-8&text=%s" % text
    #print url

    if filename is None:
        filename = text + ".wav"
    filename = filename.decode("utf-8")
    
    urllib.urlretrieve(url, filename)

def test_bench():
    test_text = "人，生而自由，但无往不在枷锁之中"
    test_count = 0
    while True:
        try:
            baidu_tts(test_text)
            test_count += 1
            if test_count > 10000:
                break
        except Exception, e:
            break
    if test_count > 10000:
        print("至少可连续请求 %d 次 TTS" % test_count)
    else:
        print("最多可连续请求 %d 次 TTS" % test_count)

if __name__ == '__main__':

    baidu_tts("中华人民共和国", "中华人民共和国.wav")
    baidu_tts("hello world", "hello world.wav")
    baidu_tts("比如给定一个说话人ID和声纹库ID，查询该说话人是否在该库中", None)
    baidu_tts("123，哦......我说错了，应该是一二三！", None)
    baidu_tts("中华人民共和国，这里是首都北京")

    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    test_bench()
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    
    print "######### GAME OVER ##########"
