#!/usr/bin/python
# -*-coding: UTF-8 -*-

# python函数

def circleArea(radius):
    if(radius < 0):
        return -1
    else:
        return 3.14 * radius * radius


print ('半径为2的圆面积为：%.2f' % circleArea(2))



# 一些内置函数

print (int('123') - 1)  # int()函数，同理float(),bool(),str()
#print ('123' - 1)       # 这样会报错

def power(num,n = 2):   # 默认参数
    result = 1
    while(n > 0):
        result *= num
        n -= 1
    return result

print (power(4))        # 默认参数调用（可以传一个参数，也可以传两个参数）

