#! /usr/bin/env python
# coding=utf-8
# author=lizhenghn@gmail.com
# date=2015-04-28
import os
import sys
import time
import pexpect
# pexpect 是一个用来启动子程序并对其进行自动控制的 Python 模块,它可以用来和像 ssh、ftp、passwd、telnet 等命令行程序进行自动交互。
# pexpect 只能在unix-like系统下使用（not windows），直接运行easy_install pexpect进行在线安装。
# Pexpect 也可以源码安装，下载地址：http://sourceforge.net/projects/pexpect/, 解压之后运行 pyhton setup.py install来安装。
# see http://www.ibm.com/developerworks/cn/linux/l-cn-pexpect1/
def test_run():
    print("####  run('ls') have not log  ####")
    pexpect.run("ls")          # 没有日志输出
    print("####  logfilr = run('ls'): log is in logfile  ####")
    log = pexpect.run("ls")
    print(log),
    print("####  run('ls', logfile=sys.stdout): log is standard output  ####")
    pexpect.run("ls", logfile=sys.stdout)
    
def test_spawn():
    try:
        child = pexpect.spawn('ls -l')         # 要执行的命令或者脚本
        fout = open("pexpect.log", "w")
        child.logfile = fout                   # 指定pexpect产生的日志的记录位置
        child.logfile = sys.stdout             # 将日志指向标准输出
        child.logfile_send = sys.stdout        # 不记录向子程序输入的日志，只记录子程序的输出
        #child.expect('ABCDEFGHIJK')           # 执行命令后需要匹配的结果
        #child.sendline('some_command')         # 匹配成功后，发送命令

        while 1:                               # 执行上条命令，需要等待很久才会得到结果的，需要使用while否则报pexpect.TIMEOUT异常
            index = child.expect(['.*unimrcpserver.*', pexpect.EOF, pexpect.TIMEOUT]) # 表示匹配到这个正则表达式时，就认为可以结束了
            if index == 0:
                break                          # 匹配到项后，跳出循环
            elif index == 1:
                pass                           # continue to wait 
            elif index == 2:
                pass                           # continue to wait 
        child.sendline('exit')
        child.sendcontrol('c')
        child.interact()
    except OSError:
        child.close()
        sys.exit(0)
    child.close()
    fout.close()

# expect 不断从读入缓冲区中匹配目标正则表达式，当匹配结束时 pexpect 的 before 成员中保存了缓冲区中匹配成功处之前的内容.
# pexpect 的 after 成员保存的是缓冲区中与目标正则表达式相匹配的内容。
def test():
    child = pexpect.spawn('/bin/ls /')  
    child.expect (pexpect.EOF)  
    print child.before  

if __name__ == '__main__':
    test_run()
    print("######################################")
    test_spawn()
