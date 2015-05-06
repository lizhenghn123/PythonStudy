#! /usr/bin/env python
# coding=utf-8
# author=lizhenghn@gmail.com
# date=2015-05-05
# desc=测试pyhton装饰器语法
from time import ctime, sleep

# 装饰器可以用来实现AOP(面向切面编程)，比如在函数执行前，运行一些调试代码，或者在函数结束后做一些清理工作:
# 1. 引入日志功能
# 2. 增加计时逻辑来检测性能
# 3. 给函数增加事务的能力
# 装饰器接收一个可调用对象作为输入，并返回一个新的可调用对象.

######    case 1    ######
# 最简单的应用
def decoFunc(func):
    ''' 一个显示何时调用函数的时戳装饰器 '''
    def wrappedFunc():
        print('[%s] %s() called, init something' % (ctime(), func.__name__))
        func()
        print('[%s] %s() called, cleanup......' % (ctime(), func.__name__))
    return wrappedFunc

@decoFunc
def foo():
    print("this is foo")

def test_foo():
    foo()
    print('')
    sleep(2)
    for i in xrange(3):
        foo()
        print('')
        sleep(1)
        
######    case 2    ######
# 装饰器带有参数
def have_arg(name='none'):
    def wrappedFunc(func):
        print('[%s] %s(), arg_name=[%s] called' % (ctime(), func.__name__, name))
        return func
    return wrappedFunc

@have_arg('name_bar')
def bar():
    print('this is bar')
    
######    case 3    ######
# 被包装函数带有参数
def print_two_arg(func):
    def wrappedFunc(a, b):
        print("input", a, b)
        return func(a, b)
    return wrappedFunc

@print_two_arg
def square_sum(a, b):
    return a**2 + b**2

######    case 4    ######
# 多个装饰器
def print_arg(func):
    def wrappedFunc(a, b):
        print("input", a, b)
        return func(a, b)
    return wrappedFunc
def print_time(func):
    def wrappedFunc(a, b):
        print('[%s] %s() called' % (ctime(), func.__name__))
        return func(a, b)
    return wrappedFunc

@print_time
@print_arg
def square_plus(a, b):
    return a**2 - b**2

if __name__ == '__main__':
 #   print("######    case 1    ######")
#    test_foo()

    print("######    case 2    ######")
    bar()
    
    print("######    case 3    ######")
    print(square_sum(3, 4))
    
    print("######    case 4    ######")
    print(square_plus(4, 3))
    
    print('###### GAME OVER ######')