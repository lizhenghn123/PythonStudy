#!/usr/bin/env python
# coding=utf-8

class emptyClass:
    pass

class A:
    def sayHi(self):
        print("hello, i am A")
# End of class A

# 在类的一个对象被建立时，__init__马上运行, 可以用来对对象做一些初始化 
class B:
    def __init__(self, name="B"):
        self.name = name
    def sayHi(self):
        print("hello, i am ", self.name)
# End of class B

class Person:
    '''Represents a person.'''
    population = 0
    def __init__(self, name):                         # 相当于构造函数（类比C++，下同）
        '''Initializes the person's data.'''
        self.name = name                              # 相当于类对象的成员
        print('(Initializing %s)' % self.name)
        # When this person is created, he/she
        # adds to the population
        Person.population += 1                        # 相当于类的静态成员，所有实例共享
    def __del__(self):                                # 相当于析构函数
        '''I am dying.'''
        print('%s says bye.' % self.name)
        Person.population -= 1
        if Person.population == 0:
            print('I am the last one.')
        else:
            print('There are still %d people left.' % Person.population)
    def sayHi(self):
        '''Greeting by the person. Really, that's all it does.'''
        print('Hi, my name is %s.' % self.name)
    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print('I am the only person here.')
        else:
            print('We have %d persons here.' % Person.population)
# End of class Person

# 类的继承
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: %s)' % self.name)
    def tell(self):
        '''Tell my details.'''
        print('Name:"%s" Age:"%s"' % (self.name, self.age))
# End of class SchoolMember 
class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)    # 必须主动调用基类的初始化，这也是和C++中构造函数不一样的地方
        self.salary = salary
        print('(Initialized Teacher: %s)' % self.name)
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "%d"' % self.salary)
# End of class Teacher        
class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: %s)' % self.name)
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "%d"' % self.marks)
# End of class Student

def test_class():
    p = emptyClass()
    print(p, id(p), str(p), repr(p)); print("");

    a = A();
    a.sayHi(); print("");

    b = B("BBB");
    b.sayHi(); print("");
    
    swaroop = Person('Swaroop')
    swaroop.sayHi()
    swaroop.howMany()
    kalam = Person('Abdul Kalam')
    kalam.sayHi()
    kalam.howMany()
    swaroop.sayHi()
    swaroop.howMany()    # 注意， 在该函数返回后，可能会调用这两个Person对象的析构，相当于RAII
    print("")

    t = Teacher('Mrs. Shrividya', 40, 30000)
    s = Student('Swaroop', 22, 75)
    s.tell();
    print("")
# End of test_class

if __name__ == '__main__' :
    test_class()
else:
    pass
