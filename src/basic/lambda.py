#!/usr/bin/env python
#coding=gb2312
#date : 2015-04-06

# lambda语句被用来创建新的函数对象，并且在运行时返回它们。
def make_repeater(n):
    return lambda s: s*n

def test_lambda():
    twice = make_repeater(2)
    print twice(5) 
    print twice('word')

    add2 = lambda x, y=2 : x+y
    print add2(1)
    print add2(3, 5)

    b=lambda *x : x   # 接收可变参数的lambda，返回参数元组
    print b(1,2,3)
    print b(1, 2.3, "Fff", {"d":5})


if __name__ == '__main__':
    test_lambda()
    print("*******************************************")
    print("*******************************************")
