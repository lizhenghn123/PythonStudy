#!/usr/bin/env python
# coding=gb2312

# 注意分支后面的":"号
# test_if
number = 23
guess = int(input('Enter an integer : '))
if guess == number:
    print('Congratulations, you guessed it.')
    print("(but you do not win any prizes!)")
elif guess < number:
    print('No, it is a little higher than that')
else:
    print('No, it is a little lower than that')
print('test if Done')

# test_while
number = 23
running = True
while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print ('Congratulations, you guessed it.') 
        running = False
    elif guess < number:
        print ('No, it is a little higher than that') 
    else:
        print ('No, it is a little lower than that') 
else:   # 在退出while之后执行的，当然不写else也一样的，毕竟会顺序往下执行
    print ('The while loop is over.') 
print('test while Done') 


# test_for
for i in range(10):
    if i > 5:
        break;        # just break for-loop
    elif i % 2 == 0:  # 如遇偶数，直接跳过
        continue
    else:
        print(i),
print('test for Done') 