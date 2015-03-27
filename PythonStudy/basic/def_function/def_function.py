#!/usr/bin/env python
# coding=gb2312

# 测试python中的函数定义和调用方式，注意定义时函数名后面的":"号
def sayHello():
    '''my first function, using python'''
    print("hello world")

def sayHello2(msg):   # 此处不能写sayHello，貌似没有函数重载
    '''my second function, using python'''
    print(msg)

def sayHello3(msg, times = 1): 
    '''my third function, using python'''
    print(msg * times)

def add(a, b = 2, c = 10):
    '''add thread int num, and then return the sum'''
    d = a + b + c
    print("%d + %d + %d = %d" % (a, b, c, d))   # 基本和C语言类似，注意参数集前后要用()包围，参数前有%符号
    #print(a, "+", b, "+", c, "=", d)  # ok too
    return d;

sayHello()  #call this func
sayHello2("new function")  #call this func
sayHello3("sayHello3")
sayHello3("sayHello3", 3)

add(1)
add(1, 2)
add(1, 2, 3)
add(3, c = 5)   # 这种调用方式，不像C系语言，参数a,b,c是无意义的，此处称为关键参数
add(b = 3, a = 0, c=0)
print(add(a=3, c=4))

print(add.__doc__)