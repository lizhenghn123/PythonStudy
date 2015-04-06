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

def test1():
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

#### 测试变长参数 ####
# 参数名前有一个*，表示会把所有参数当成一个元组，有两个**，会把所有参数当成一个字典
def variadic_params(*nkwargs, **kwargs):
    print("print tuple args:"),
    for i in nkwargs:
       print i,
    print("\nprint dict  args："),
    for k,v in kwargs:
        print("%s : %s" %(k, v))
    print("\nprint over")
# End

def variadic_func(func, *nkwargs, **kwargs):
   try:
       retval = func(*nkwargs, **kwargs)
       result = (True, retval)
   except Exception, diag:
       result = (False, str(diag))
   return result
# End

def test_variadic():
    
    variadic_params(1,2,3)
    variadic_params(1)
    variadic_params(2,5,"d", "a=1", {"b" : "2", "v" : 80})
    variadic_params("v=1", "z=1234")

    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')
    
    for eachFunc in funcs:
        print '-' * 20
        for eachVal in vals:
            retval = variadic_func(eachFunc, eachVal)
            if retval[0]:
                print '%s(%s) =' %(eachFunc.__name__, `eachVal`), retval[1]
            else:
                print '%s(%s) = FAILED:' %(eachFunc.__name__, `eachVal`), retval[1]

# End

if __name__ == '__main__':
    test1()
    print("*******************************************")
    test_variadic()
    print("*******************************************")
