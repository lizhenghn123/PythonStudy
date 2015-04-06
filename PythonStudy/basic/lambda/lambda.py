#!/usr/bin/env python
#coding=utf-8
#date : 2015-04-06

# lambda语句被用来创建新的函数对象，并且在运行时返回它们。
def make_repeater(n):
    return lambda s: s*n

def test_lambda():
    twice = make_repeater(2)
    print twice('word')
    print twice(5) 

if __name__ == '__main__':
    test_lambda()
    print("*******************************************")
    print("*******************************************")