#!/usr/bin/env python
# coding=gb2312
import time

def test_assert():
    mylist = ['item']
    assert len(mylist) >= 1
    mylist.pop()
    assert len(mylist) >= 1   # oohs...
# End

def test_basic():
    s = [x ** 2 for x in range(5)]  # 列表解析
    print(s);   # [0, 1, 4, 9, 16]

    listone = [2, 3, 4]               # 列表综合
    listtwo = [2*i for i in listone if i > 2]
    print(listtwo) 

    x,y,z = 1 # 多重赋值
    x,y,z = 2, 1.25, "hello"

    x,y = 1,2
    x,y = y,x  # 值交换

    print(time.strftime('%Y%m%d%H%M%S'))
# End
if __name__ == '__main__':
    test_basic();
    test_assert();
