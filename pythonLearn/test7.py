#!/usr/bin/python
# -*-coding: UTF-8 -*-

# python面向对象

class Student(object):  # 一般继承于object，可继承于其他

    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print ("%s: %s" % (self.name,self.score))


student = Student('yanghaipeng',99)
student.print_score()


# 继承--------------------------------------------

class Animal(object):

    def functionA(self):
        print ("Animal")


class Goat(Animal):
    pass


goat = Goat()
goat.functionA()


# 获取对象信息--------------------------------------

print (type(123))  # 获取对象类型

print (dir('ABC')) # 获得一个对象的所有属性和方法




