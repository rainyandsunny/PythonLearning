#!/usr/bin/python
# -*-coding: UTF-8 -*-

# python高级特性


from collections import Iterable

# 切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print (L[0:3])  # 返回 ['Michael', 'Sarah', 'Tracy']
print (L[-3:-1])  # 返回 ['Tracy', 'Bob']

list = list(range(100))

print (list[:10])  # 返回前10个元素

print (list[-10:])  # 返回后10个元素

print (list[:10:2])  # 前10个数，每2个取一个

print ('ABCDEFG'[:3])  # 字符串也可以看成一个list
print ('ABCDEFG'[::2])  # 返回ACEG


def trimStr(str):
   length = len(str)
   start = 0
   end = length - 1
   while(start < length):
       if(str[start] == ' '):
           start += 1
       else:
            break
   while (end >= 0):
       if (str[end] == ' '):
           end -= 1
       else:
           break
   print (start,end)
   return str[start:end + 1]


# 迭代
d = {'A': 'a', 'B': 'b', 'C': 'c'}
for key in d:
    print (key, d.get(key))

print (isinstance('ABCD',Iterable))   # 判断对象是否可以迭代
print (isinstance(123,Iterable))
print (isinstance([1,2,4],Iterable))

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print (x,y)


# 列表生成式
for number in range(0,100):
    print (number)

print (isinstance("abc",str))   # 判断对象是否是字符串类型


L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [string.lower() for string in L1 if isinstance(string,str)] # for循环后还可以加上if判断

print (L2)


# 生成式
g = (x * x for x in range(10))
print (g)       # <generator object <genexpr> at 0x10df62640>

print (next(g))  # 可以通过next()函数获得generator的下一个返回值

for n in g:      # 遍历生成式
    print (n)


