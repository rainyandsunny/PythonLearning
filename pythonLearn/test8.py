#!/usr/bin/python
# -*-coding: UTF-8 -*-

# python面向对象高级编程

class Student(object):
    pass

s = Student()
s.name = "Michael"  # 动态绑定字段
print (s.name)

def setAge(self,age):
    self.age = age

from types import MethodType

s.set_age = MethodType(setAge,s)   # 动态绑定方法
s.set_age(18)

print (s.age)


# 想要限制实例的属性，可以使用_slots_

class Person(object):
    __slots__ = ('name','age')

p = Person()

#p.sex = 'male'  # 会报错，AttributeError: 'Person' object has no attribute 'sex'
p.name = 'yang'
print (p.name)


# 使用@property-------------------------------------
class Person(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise  ValueError('score must between 0 ~ 100!')
        self._score = value

p1 = Person()

p1.score = 10


# 多重继承---------------------------------------

class Child(Student,Person):
    pass


# 定制类----------------------------------------------

# _str_: python中的toString

class Test(object):
    def __init__(self,name):
        self._name = name
    def __str__(self):
        return 'Student name: %s' % self._name

test = Test('abc')

print (test)


# _iter_

class Fib(object):
    def _init_(self):
        self.a , self.b = 0 , 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.b + self.a
        if(self.a > 10000):
            raise StopIteration()
        return self.a

for n in Fib():
    print (n)

