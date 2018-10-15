#!/usr/bin/python
# -*-coding: UTF-8 -*-

# python模块

' a test module '

import sys

__author__ = 'yanghaipeng'

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()


# 作用域----------------------------

#类似_xxx和__xxx这样的函数或变量就是非公开的（private）