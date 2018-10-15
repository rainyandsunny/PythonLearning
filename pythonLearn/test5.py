#!/usr/bin/python
# -*-coding: UTF-8 -*-

# python函数

from collections import Iterable
from functools import reduce

# 高阶函数-----------------------------------------

def f(x):
    return x * x

r = map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])  # map函数

def add(x,y):
    return x + y

result = reduce(add, [1, 3, 5, 7, 9])  # reduce函数
print (result)

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算

def isOdd(x):
    return x % 2 == 1

print (filter(isOdd,[1,2,3,4,5,6,7,8,9]))  # filter函数


print (sorted([5,6,1,2,9,0]))    #sorted函数

print (sorted([36, 5, -12, 9, -21], key=abs))  #可以加上key

print (sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# 返回函数-----------------------------------------

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)

print (f1)
print (f1())
print (f1 == f2)


# 装饰器--------------------------------------------


def now():
    print ('2015-3-25')

f = now   # 函数也可以赋值
print (f.__name__)
f()

def log(func):     #装饰器的用法
    def wrapper (*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper

@log           # @log = log(wrapperTest)
def wrapperTest(x):
    print ('装饰器' + x)

wrapperTest('a')


# 偏函数
import functools

int2 = functools.partial(int, base=2)

print (int2('1000000'))

