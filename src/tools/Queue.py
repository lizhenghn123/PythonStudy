#!/usr/bin/env python
#coding=utf-8

# 利用列表实现queue功能
class queue:
    def __init__(self):
        self.queue_ = []

    def enqueue(self, o):
        self.queue_.append(o)

    def dequeue(self):
        if len(self.queue_) == 0:
            print("cannot pop from an empty stack")
            throw
        else:
            return self.queue_.pop(0)  # 删除第一个元素

    def view(self):
        print(self.queue_)
        
# End class

def test_queue():

    desc = """    ---- test queue ----
        (e)nqueue
        (d)equeue
        (v)iew
        (q)uit

        enter your choice: """

    ss = queue()
    while(True):

        while True:
            choice = (raw_input(desc))[0].lower();
            if(choice not in "edvq"):
                print("invalid option, try again")
            else:
                break;

        if(choice == "q"):
            break;
        elif choice == "e":
            s = raw_input("input one element: ").strip()
            ss.enqueue(s);
        elif choice == "d":
            print("pop the top element %s" % ss.dequeue())
        elif choice == "v":
            ss.view()
#end

if __name__ == '__main__':
    test_queue();
