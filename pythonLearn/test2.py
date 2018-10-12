#!/usr/bin/python
# -*-coding: UTF-8 -*-


#python基础练习



# 基本数据类型

print ('I\'m ok') #转义字符使用

a = True and False

b = 3 < 2

print ('%s', a)
print ('%s', b)
print ('%s', not False)
print ('%d', len("abcdef")) # len方法
print ('%d', len('中文'))

# 格式化

str1 = 'Hello, %s' % 'world'
print ('%s' % str1)


str2 = 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
print (str2)

# list

classmates = ['Michael', 'Bob', 'Tracy']
print (classmates[-2])

# list 有序集合，可随时添加
classmates.append("yanghaipeng")
print (classmates[-1])

# 删除元素
classmates.pop(2)
print (classmates)

# 元素替换
classmates[2] = 'red'
print (classmates)

# tuple tuple和list非常类似，但是tuple一旦初始化就不能修改

classmates = ('Michael', 'Bob', 'Tracy')
print (classmates)

number = (1,) #避免歧义（而不是使用number = (1)）
print (number[0])


# 条件判断
age = 20
if(age > 18):
    print('your age is', age)
    print ('adult')

if(age):  #非0就可以
    print ('True')

# 循环(for循环)
for name in classmates:
    print name

sum = 0
for number in [1,2,3,4,5,6,7,8,9,10]:
    sum += number
print (sum)

# 循环（while循环）
sum = 0
number = 1
while(number <= 10):
    sum += number
    number += 1
print (sum)


# 字典
d = {'A': 98, 'B': 97, 'C': 96}

print (d['A'])

print ('E' in d) #in 判断是否在字典中

print (d.get('D',0)) #通过get判断（没有则返回None),也可以指定找不到的默认值

d.pop('B')   #pop: 删除字典中的元素

print (d.get('B'))

# Set(无重复元素)

s = set([1, 2, 3, 0])
s.add(4)          #add操作
print (s)

s = set([1,1,2,3,4,5,7,7]) #重复的元素会被剔除
print (s)

s.remove(2) #remove移除元素
print (s)

s1 = set([1,2,3])
s2 = set([2,3,4])
print (s1 & s2)  #&运算
print (s1 | s2)  #|运算

list1 = ['a','b','d','c']
print (list1)

list1.sort()   # list sort操作
print (list1)

str = 'abcd'
str1 = str.replace('a','A') #string replace操作，str内容不变，str1内容变化
print (str)









