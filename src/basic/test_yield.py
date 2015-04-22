#!/usr/bin/env python
#coding=utf-8
#author=lizheng
#date=2015-04-17
from inspect import isgeneratorfunction   # 判断一个函数是否是一个特殊的 generator 函数

# 求斐波那契数列的前N个数
# 直接在 fabN 函数中用 print 打印数字会导致该函数可复用性较差，
# 因为 fab 函数返回 None，其他函数无法获得该函数生成的数列
def fabN1(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        print(b)
        a, b = b, a + b 
        n = n + 1
fab(5)  # 输出斐波那契数列的前5个数
print("###############################")

# 该函数在运行中占用的内存会随着参数 max 的增大而增大，
# 如果要控制内存占用，最好不要用 List来保存中间结果(通过 iterable 对象来迭代)
def fabN2(max): 
    n, a, b = 0, 0, 1 
    L = [] 
    while n < max: 
        L.append(b) 
        a, b = b, a + b 
        n = n + 1 
    return L
for i in fabN2(5):
    print(i)
print("###############################")

# 第三版本，通过 next() 不断返回数列的下一个数，内存占用始终为常数，但稍嫌复杂
class fabN3(object): 

    def __init__(self, max): 
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 

    def __iter__(self): 
        return self 

    def next(self): 
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration()
for n in fabN3(5): 
    print n
print("###############################")

# 第四版本，yield出场
# yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，
# Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
# 在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，
# 下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，
# 于是函数继续执行，直到再次遇到 yield。
# 注意：fabN4 是generator function， 而fabN4(5) 是调用fabN4后返回的一个generator
def fabN4(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b  # print(b) , 注意与fabN的差异 
        a, b = b, a + b 
        n = n + 1
for n in fabN4(5): 
    print n
# 手动调用 fab(5) 的 next() 方法（因为 fab(5) 是一个 generator 对象，该对象具有 next() 方法）
f = fabN4(3)
print(f.next())
print(f.next())
print(f.next())
#print(f.next())   # None
print("###############################")

print(isgeneratorfunction(fabN4))
print(isgeneratorfunction(fabN1))