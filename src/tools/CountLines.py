#!/usr/bin/env python
# coding=utf-8
# author=lizhenghn@gmail.com
# date=2015-04-20
# desc=Count files and lines of the directory
# 统计某一目录下所有文件的总数和文件总行数（比如可用来统计源码目录的文件数和代码行数），
# 可以指定统计规则（比如只统计/不统计某些特定文件）。支持输入参数设置待统计目录，待统计文件规则等。
# ex:
# ./CountLines.py (--version, --help, --h)
# ./CountLines.py -d
# ./CountLines.py -p /home/admin -r '*.cpp;!*py;*.h' -d
import os
import sys
import fnmatch
from optparse import OptionParser

class Util:
    @staticmethod
    def isExist(path):
        return os.path.exists(path)
    @staticmethod
    def isDir(path):
        return os.path.isdir(path)    
    @staticmethod
    def isFile(path):
        return os.path.isfile(path)
    @staticmethod
    def countLine(file):
        lines = 0
        for line in open(file).xreadlines():
            lines += 1
        return lines 

class CountLines(object):
    def __init__(self, dir, rules=''):
        if dir[len(dir)-1] == os.sep:
            dir = dir[:len(dir)-1]
        self.searchDir_ = dir
        self.countLines_, self.countFiles_ = 0, 0
        self.fileLineDict_ = {}
        self.rules_ = rules
        self.selectRules_ = set()
        self.ignoreRules_ = set()
        self.parseRules(rules)
    def parseRules(self, rules):
        if not rules:
            return
        if rules[0] == '\'' or rules[0] == '\"':
            rules = rules[1:]
        if rules[len(rules)-1] == '\'' or rules[len(rules)-1] == '\"':
            rules = rules[:len(rules)-1]  
        rules = rules.split(';')
        #print(rules)
        for rule in rules:
            if not rule:
                continue
            if rule[len(rule)-1] == os.sep:
                rule = rule[:len(rule)-1]
            if rule[0] == '!':
                self.ignoreRules_.add(rule[1:].strip())
            else:
                self.selectRules_.add(rule.strip())
        #print(self.ignoreRules_)
        #print(self.selectRules_)
    def selectFilter(self, path):
        if len(self.selectRules_) == 0:
            return True
        select = False 
        for select_rule in self.selectRules_:
            if fnmatch.fnmatch(path, self.searchDir_ + os.sep + select_rule):
                select = True
                break
        return select
    def ignoreFilter(self, path):
        ignore = False
        for ignore_rule in self.ignoreRules_:
            if fnmatch.fnmatch(path, self.searchDir_ + os.sep + ignore_rule):
                ignore = True
                break
        return ignore
    def analyzeFile(self, file):
        self.countFiles_ += 1
        lines = Util.countLine(file)
        self.countLines_ += lines
        self.fileLineDict_[file] = lines

    def countAll(self):
        if Util.isFile(self.searchDir_):
            self.analyzeFile(self.searchDir_)
            return
        dirs = []
        dirs.append(self.searchDir_)
        while 1:
            if len(dirs) == 0:
                break
            curr = dirs.pop(0)

            if Util.isFile(curr):
                if self.ignoreFilter(curr):
                    continue
                elif not self.selectFilter(curr):
                    continue
                self.analyzeFile(curr)
            else:
                for file in os.listdir(curr):
                    abspath = curr + os.sep + file
                    #print(abspath)
                    dirs.append(curr + os.sep + file)
    def printResult(self):
        print("##########################")
        print('==total==')
        print 'file count: %d' % self.countFiles_
        print 'line count: %d' % self.countLines_
        print("##########################")
    def printResultDetail(self):
        sorted_list = sorted(self.fileLineDict_.iteritems(), key=lambda d: d[0], reverse=False)
        for one_file in sorted_list:
            file_name, file_lines = one_file
            file_name = file_name[len(self.searchDir_) + 1:]       
            print('%-50s %10s' % (file_name, str(one_file[1])))        
        self.printResult()
# End class CountLines

def main():
    print('*************************')
    command_parser = OptionParser(usage="%prog [options] [args]", version="%prog 0.8.0",
                                  description="Count the amount of lines and files on the directory")
    command_parser.add_option("-p", "--path", action="store", dest="path", default=os.getcwd(),
                              help="set the dir which will be count, default is current directory")
    command_parser.add_option("-r", "--rule", action="store", dest="rules", default='',
                              help="set some rules(*.cpp is selected or !*.cpp is ignoreed), ex : *.cpp;*.py;!*h")
    command_parser.add_option("-d", "--detail", action="store_true", dest="show_detail", default=False,
                              help="show more detail in the result")


    command_options, command_args = command_parser.parse_args()
    #print(command_options, command_args)
    #print(command_options.rules)

    show_detail = command_options.show_detail

    cl = CountLines(command_options.path, command_options.rules) # r'D:\zzz\readme.txt', r'/root/lizhenghn/src'
    print('Count files and lines in %s' % (command_options.path))
    cl.countAll()
    if show_detail:
        cl.printResultDetail()
    else:
        cl.printResult()  

def test_visitAllFiles():
    oridir = r'D:\zzz\test'
    dirs = []
    dirs.append(oridir)
    while 1:
        if len(dirs) == 0:
            break
        #print(dirs)
        curr = dirs.pop(0)
        if Util.isFile(curr):
            print("file : ", curr)
        else:
            #print("is dir : ", curr)
            for file in os.listdir(curr):
                #print("----", file)
                dirs.append(curr+os.sep+file)

def test_fnamatch():
    if fnmatch.fnmatch(r'd:\rrr\a\r\1.txt', r'd:\rrr\*.txt'):
        print("1")
    if fnmatch.fnmatch(r'D:\os_share\PythonStudy\src\tools\CountLines_v2.py', r'D:\\os_share\\PythonStudy\\src\\*.py'):
        print("1")
    print("ZZZZZZZZZZZZZZZZZZZZZZ")
    
if __name__ == '__main__':
    #test_visitAllFiles()
    #test_fnamatch();
    main()
