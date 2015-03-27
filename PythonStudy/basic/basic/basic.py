#!/usr/bin/env python
# coding=gb2312

def test_assert():
    mylist = ['item']
    assert len(mylist) >= 1
    mylist.pop()
    assert len(mylist) >= 1   # oohs...
# End

if __name__ == '__main__':
    test_assert()