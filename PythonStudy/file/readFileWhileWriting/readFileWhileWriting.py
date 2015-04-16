#!/usr/bin/env python
# coding=utf-8
#date : 2015-04-14
import os
import time

# 假设一个程序正在往某一文件中写数据（只限追加，比如写日志），本脚本就可以每次读取新添加的行并显示
# 相当于linux下的tail -f 命令

g_filepath = r"test.log"
g_try_readfile_timeout = 0.5   # 秒

def tailFile(path):               # 一个经典做法
    file = open(path)
    #file = open(path, "r", -1, "utf8")
    while(True):
        where = file.tell()
        line = file.readline()
        if not line:
            print("----now it is no much more lines----")
            time.sleep(g_try_readfile_timeout)  # sleep 
            file.seek(where)
        else:
            print(line),
# End

def tailFile1(path):
    file = open(path)
    while(True):
        line = file.readline()
        if not line:
            print("----now it is no much more lines----")
            time.sleep(g_try_readfile_timeout)
        else:
            print(line)
# End

def tailFile2(path):            # 粗鲁做法，简单的记录上次读了多少行，关闭文件再打开，然后跳过读过的行数
    file = open(path)   
    line_last_count = 0 
    line_count = 0;        
    while(True):           
        line = file.readline()
        if not line:       
            print("--ok--%d--%d" % (line_last_count,line_count))
            line_last_count = line_count
            line_count = 0;
            file.close()
            file = open(path)
            time.sleep(g_try_readfile_timeout)
        else:              
            line_count += 1
            if(line_count <= line_last_count):
                pass       
            else:          
                print(line)
# End                      

if __name__ == "__main__":
    #tailFile(g_filepath)
    tailFile1(g_filepath)
    tailFile2(g_filepath)