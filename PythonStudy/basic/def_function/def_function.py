#!/usr/bin/env python
# coding=gb2312
from time import ctime, sleep
from random import randint

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
def variadic_params(one, *nkwargs, **kwargs):
    print("print main args: %s" %str(one))
    print("print tuple args:"),
    for i in nkwargs:
       print i,
    print("\nprint dict  args："),
    for k,v in kwargs.items():
        print("(%s : %s) " %(k, v)),
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
    variadic_params("huo",5,"d",a=1)
    variadic_params(1,v=1, z=1234)
    variadic_params(2, *(4, 6, 8), **{'foo': 10, 'bar': 12}) 
    aTuple = (6, 7, 8) 
    aDict = {'z': 9} 
    variadic_params(4, 9, x=2, y=1, *aTuple, **aDict)  # 这种方式太灵活了！

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

# 内部函数
def outerFunc():
    def innerFunc():
        print("innerFunc")
    print("outerFunc")
    innerFunc()
# End

def test_innerFunc():
    outerFunc()   # ok
   # innerFunc()   # error, 函数不可见
# End

# 装饰器：我们能在包装的环境下在合适的时机调用它。我们在执行函数之前，可以运行些预备代码，也可以在
# 执行代码之后做些清理工作。所以当你看见一个装饰器函数的时候，很可能在里面找到这样一些代码， 
# 它定义了某个函数并在定义内的某处嵌入了对目标函数的调用或者至少一些引用。 从本质上看，
#这些特征引入了 java 开发者称呼之为 AOP （Aspect Oriented Programming， 面向方面编程） 的概念。
# 装饰器的语法以@开头，接着是装饰器函数的名字和可选的参数。紧跟着装饰器声明的是被修饰的函数，和装饰函数的可选参数。
def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()
    return wrappedFunc

@tsfunc
def foo():
    print("---foo()---")

def test_aop():
    foo()   # 相当于在真正调用foo之前会先执行tsfunc
    sleep(3)
    for i in range(2):
        sleep(1)
        foo()
    tsfunc(foo)()
# End

# 传递函数：函数是可调用的
def convert(func, seq):
	'conv. sequence of numbers to same type'
	return [func(eachNum) for eachNum in seq]

def test_func():
    myseq = (123, 45.67, -6.2e8, 999999999L)
    print convert(int, myseq)
    print convert(long, myseq)
    bar = convert  # bar 引用 convert
    print bar(float, myseq)
# End

# 内建函数filter、map、reduce的使用
def test_filter_map_reduce():
    #### filter(func, seq)
    def is_odd(n):     # 判断奇数
        return n % 2 != 0

    num1 = []
    for i in range(9):   # 产生9个随机数
        num1.append(randint(1,99))
    print num1

    num = filter(is_odd, num1)   # 将序列num1元素逐次调用布尔函数is_odd，为true则返回该元素
    print num

    num = filter(lambda n : n%2!=0, num1)
    print num

    num = [n for n in num1 if n %2!=0]
    print num

    num = [n for n in [randint(1, 99) for i in range(9)] if n%2 !=0]
    print num

    #### map(func, seq1, seq2...)
    num = map(lambda x : x + 2, [0,1,2,3,4])
    print num 

    num = map(lambda x : x**2, range(5))
    print num 

    num = [x**2 for x in range(5)]
    print num 

    num = map(lambda x,y : x+y, [1,2,3], [4,5,6])
    print num 
    num = map(lambda x,y : (x+y,x-y), [1,2,3], [4,5,6])
    print num 
    num = map(None, [1,2,3], [4,5,6])
    print num 

    #### reduce(func, seq[, init])
    def mysum(x,y) : return x+y
    num2 = range(1,6)
    total = 0
    for x in num2:
        total = mysum(total, x)
    print total
    
    total = reduce((lambda x,y : x+y), range(1,6))
    print total 

# End

if __name__ == '__main__':
    test1()
    print("*******************************************")
    test_variadic()
    print("*******************************************")
    test_innerFunc()
    print("*******************************************")
    test_aop()
    print("*******************************************")
    test_func()
    print("*******************************************")
    test_filter_map_reduce()