#!/usr/bin/env python
#coding=utf-8

def test_list():
    #this is my shopping list
    shoplist = ['apple', 'mango', 'carrot', 'banana']
    print('I have %d items to purchase.' % len(shoplist))
    print('These items are:'), # 使用一个逗号来消除每个print语句自动打印的换行符
    for item in shoplist:
        print(item),
    print('\nI also have to buy rice.')
    
    shoplist.append('rice')
    print('My shopping list is now %s' % shoplist)
    print('I will sort my list now')
    shoplist.sort()
    
    print('Sorted shopping list is %s' % shoplist)
    print('The first item I will buy is %s' % shoplist[0])

    olditem = shoplist[0]
    del shoplist[0]
    print('I bought the %s' % olditem)
    print('My shopping list is now %s' % shoplist)
# End of test_list

def test_tuple() :
    zoo  = ('wolf', 'elephant', 'penguin')
    print('Number of animals in the zoo is', len(zoo))
    new_zoo = ('monkey', 'dolphin', zoo)
    print('Number of animals in the new zoo is', len(new_zoo))
    print('All animals in new zoo are %s' % str(new_zoo))
    print('All animals in new zoo are ',  new_zoo)
    print('Animals brought from old zoo are', new_zoo[2])
    print('Last animal brought from old zoo is', new_zoo[2][2])
# End of test_tuple

def test_map() :
    ab = { 
         'Swaroop' : 'swaroopch@byteofpython.info',
         'Larry' : 'larry@wall.org',
         'Matsumoto' : 'matz@ruby-lang.org',
         'Spammer' : 'spammer@hotmail.com'
         }
   
    print("Swaroop's address is %s" % ab['Swaroop'])

    # Adding a key/value pair
    ab['Guido'] = 'guido@python.org'
    
    # Deleting a key/value pair
    del ab['Spammer']
    
    print('\nThere are %d contacts in the address-book\n' % len(ab))
    
    for name, address in ab.items():
        print('Contact %s at %s' % (name, address))
    
    if 'Guido' in ab: # or ab.has_key('Guido')
        print("\nGuido's address is %s" % ab['Guido'])
# End of test_map

# 列表、元组和字符串都是序列; 序列的两个主要特点是索引操作符和切片操作符。
# 索引操作符让我们可以从序列中抓取一个特定项目。切片操作符让我们能够获取序列的一个切片，即一部分序列。
def test_sequence():
    shoplist = ['apple', 'mango', 'carrot', 'banana']
    # Indexing or 'Subscription' operation
    print('Item 0 is', shoplist[0])
    print('Item 1 is', shoplist[1])
    print('Item 2 is', shoplist[2])
    print('Item 3 is', shoplist[3])
    print('Item -1 is', shoplist[-1])
    print('Item -2 is', shoplist[-2])
    # Slicing on a list
    print('Item 1 to 3 is', shoplist[1:3])
    print('Item 2 to end is', shoplist[2:])
    print('Item 1 to -1 is', shoplist[1:-1])
    print('Item start to end is', shoplist[:])
    # Slicing on a string
    name = 'swaroop'
    print('characters 1 to 3 is', name[1:3])
    print('characters 2 to end is', name[2:])
    print('characters 1 to -1 is', name[1:-1])
    print('characters start to end is', name[:]) 
# End of test_sequence

# 当创建一个对象并给它赋一个变量的时候，这个变量仅仅引用那个对象，而不是表示这个对象本身！
# 也就是说，变量名指向你计算机中存储那个对象的内存。这被称作名称到对象的绑定。
# 如果你想要复制一个列表或者类似的序列或者其他复杂的对象（不是如整数那样的简单对象 ），必须使用切片操作符来取得拷贝。
# 记住列表的赋值语句不创建拷贝。你得使用切片操作符来建立序列的拷贝。
def test_reference():
    print('Simple Assignment')
    shoplist = ['apple', 'mango', 'carrot', 'banana']
    mylist = shoplist # mylist is just another name pointing to the same object!
    del shoplist[0]
    print('shoplist is', shoplist)
    print('mylist is', mylist)
    # notice that both shoplist and mylist both print the same list without
    # the 'apple' confirming that they point to the same object
    print('Copy by making a full slice')
    mylist = shoplist[:] # make a copy by doing a full slice
    del mylist[0] # remove first item
    print('shoplist is', shoplist)
    print('mylist is', mylist)  # notice that now the two lists are different 

    s1 = [1,2,"hello",4]
    s2 = [1]
    if [1,5] in s1:
        print("[1, 5] in %s" %s1)
    if 1 in s1:
        print("1 in %s"  %s1)
    if "world" not in s1:
        print("world not in %s" %s2 %s1)

# End of test_reference

if __name__ == '__main__' :
    print("------------------test list-------------------")
    test_list();
    print("------------------test tuple-------------------")
    test_tuple();
    print("------------------test map-------------------")
    test_map();
    print("------------------test sequence-------------------")
    test_sequence()
    print("------------------test reference-------------------")
    test_reference()

