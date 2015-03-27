#!/usr/bin/env python
# coding=gb2312

#在外部使用时，比如
#use_module.py  或者
#use_module.py 1 2 argu
#就会通过sys.argv打印出所有出入参数
#类似C语言中的int main(int argc[], char **argv)

import sys
import mymodule

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')


print("--------------------\n")
mymodule.sayHi()

print('mymodule.version : ', mymodule.version)
print(mymodule.sayHi.__doc__)


#使用内建的dir函数来列出模块定义的标识符。标识符有函数、类和变量。
#当你为dir()提供一个模块名的时候，它返回模块定义的名称列表。如果不提供参数，它返回当前模块中定义的名称列表
s = dir(mymodule.sayHi)
print(s)

print("\n")
print(dir())  # 不带参数时返回当前模块的属性列表