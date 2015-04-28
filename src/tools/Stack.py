#!/usr/bin/env python
#coding=utf-8

# 利用列表实现stack功能
class stack:
    def __init__(self):
        self.stack_ = []

    def push(self, o):
        self.stack_.append(o)

    def pop(self):
        if len(self.stack_) == 0:
            print("cannot pop from an empty stack")
            throw
        else:
            return self.stack_.pop()

    def view(self):
        print(self.stack_)
        
# End class

def test_stack():
    desc = """    ---- test stack ----
        p(u)sh
        p(o)op
        (v)iew
        (q)uit

        enter your choice: """

    ss = stack()
    while(True):

        while True:
            choice = (raw_input(desc))[0].lower();
            if(choice not in "quov"):
                print("invalid option, try again")
            else:
                break;

        if(choice == "q"):
            break;
        elif choice == "u":
            s = raw_input("input one element: ").strip()
            ss.push(s);
        elif choice == "o":
            print("pop the top element %s" % ss.pop())
        elif choice == "v":
            ss.view()
#end

if __name__ == '__main__':
    test_stack();
