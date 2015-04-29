#! /usr/bin/env python
# coding=utf-8
# author=lizhenghn@gmail.com
# date=2015-04-27
import os
import random
import string

# 根据字符串集合和长度生成随机密码
def genPasswd(length = 8, chars = string.letters + string.digits):
    return ''.join([random.choice(chars) for i in xrange(length)])

# 生成伪随机密码，使密码有一定易记忆性
# see <<Python Cookbook(第二版，中文版)>> P372 chapter10
# 模仿英文单词的n元语法，也即马尔科夫链英语模拟(Markov Chain Simulation of English)
class password(object):
    # 任何含有大量单词的文件都可以，只要能让self.data成为一个大字符串，以用来模拟其中的文本
    data = open("/usr/share/dict/words").read().lower()
    
    def renew(self, n, maxmem=3):
        ''' 根据回溯的最大‘历史’的maxmem个字符，在self.chars中累积n个随机字符'''
        self.chars = []
        for i in range(n):
            # 随机"旋转"self.data
            randspot = random.randrange(len(self.data))
            self.data = self.data[randspot:] + self.data[:randspot]
            # Get the n-gram
            where = -1
            # 试图定位self.data中最后maxmem各字符，如果i<maxmem,我们其实只获取
            # 最后i个，即使是所有self.chars也没问题：列表切片的容忍度很高，仍然适合此算法
            locate = ''.join(self.chars[-maxmem:])
            while where<0 and locate:
                # 定位data中的n-gram
                where = self.data.find(locate)
                # 如果必要的话后退到一个短一点的n-gram
                locate = locate[1:]
            # if where==-1 and locate='', we just pick self.data[0] --
            # it's a random item within self.data, tx to the rotation
            c = self.data[where+len(locate)+1]
            # we only want lowercase letters, so, if we picked another
            # kind of character, we just choose a random letter instead
            if not c.islower(): c = random.choice(string.lowercase)
            # and finally we record the character into self.chars
            self.chars.append(c)
    def __str__(self):
        return ''.join(self.chars)

def test_genPasswd():
    print(genPasswd(4))
    print(genPasswd(12))
    for i in xrange(3):
        print(genPasswd(6))

def test_passwd():
    "Usage: pastiche [passwords [length [memory]]]"
    import sys
    if len(sys.argv)>1: dopass = int(sys.argv[1])
    else: dopass = 8
    if len(sys.argv)>2: length = int(sys.argv[2])
    else: length = 10
    if len(sys.argv)>3: memory = int(sys.argv[3])
    else: memory = 3
    onepass = password()
    for i in range(dopass):
        onepass.renew(length, memory)
        print onepass
        
if __name__ == '__main__':
    test_genPasswd()
    print("###################")
    test_passwd()
