#!/usr/bin/env python
# coding=utf-8
# author=lizhenghn@gmail.com
# date=2015-04-20
import os
import sys
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
    def __init__(self, dir):
        self.searchDir_ = dir
        self.countLines_, self.countFiles_ = 0,0
        self.files=set()
        self.fileLineDict_ = {}  
    def analyzeFile(self, file):
        self.files.add(file)
        self.countFiles_ += 1
        lines = Util.countLine(file)
        self.countLines_ += lines
        self.fileLineDict_[file] = lines
    def printResult(self):
        print("##########################")
        print 'file count: %d' % self.countFiles_
        print 'line count: %d' % self.countLines_
        print("##########################")
    def printResultDetail(self):
        sorted_list = sorted(self.fileLineDict_.iteritems(), key=lambda d: d[0], reverse=False)
        for one_file in sorted_list:
            file_name, file_lines = one_file
            file_name = file_name[len(self.searchDir_) + 1:]       
            print('%-50s %10s' % (file_name, str(one_file[1])))
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
                self.analyzeFile(curr)
            else:
                for file in os.listdir(curr):
                    dirs.append(curr + os.sep + file)
            
# End class CountLines

def visitAllFiles():
    oridir = r'D:\zzz\test'
    cl = CountLines(r'D:\zzz\test')

    dirs = []
    dirs.append(oridir)
    while 1:
        if len(dirs) == 0:
            break
        #print(dirs)
        curr = dirs.pop(0)
        if cl.isFile(curr):
            print("file : ", curr)
        else:
            #print("is dir : ", curr)
            for file in os.listdir(curr):
                #print("----", file)
                dirs.append(curr+os.sep+file)

def main():
    command_parser = OptionParser(usage="%prog [options] [args]", version="%prog 0.8.0",
                                  description="Count the amount of lines and files on the directory")
    command_parser.add_option("-p", "--path", action="store", dest="path", default=os.getcwd(),
                              help="set the dir which will be count, default is current directory")    
    command_parser.add_option("-d", "--detail", action="store_true", dest="show_detail", default=False,
                              help="show more detail in the result")

    command_options, command_args = command_parser.parse_args()
    print(command_options, command_args)

    show_detail = command_options.show_detail

    cl = CountLines(command_options.path)   # r'D:\zzz\readme.txt', r'/root/lizhenghn/src'

    print('Count files and lines in %s' % (os.getcwd() + os.sep))
    cl.countAll()
    if show_detail:
        cl.printResultDetail()
    else:
        cl.printResult()

if __name__ == '__main__':
    #visitAllFiles()
    main()
