#!/usr/bin/env python
# coding=utf-8
import os

def test_os():
   print(os.name);        # os
   print(os.getcwd());    # current dir
   print(os.getenv("root"));    # current env, os.setenv()
   #print(os.listdir("/home"));  
   print(os.remove("none.log"));
   #print(os.system("ls"));
   print(os.linesep);     # '\r\n'(windows), '\n'(linux), '\r'(mac)
   #print(os.split("/root/1/2.txt"));   # return dir and filename of the path

   if(os.path.isfile("/root/1.cpp")) :
       print("is a file")
   if(os.path.isdir(r("/root/3"))) : 
       print("is a dir")
   if(os.path.exists("/rott/df")) : 
       print("yes, it is exist")
# End of test_os


if __name__ == '__main__' :
    test_os()
else:
    pass
