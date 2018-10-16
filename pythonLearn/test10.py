#!/usr/bin/python
# -*-coding: UTF-8 -*-

# IO

try:
    f = open('./demo.txt','r')
    print (f.read())

finally:
    if f:
        f.close()


with open('./demo.txt','r') as f:  # try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法
    for line in f.readlines():
        print (line.strip())


with open('./demo.png','rb') as f1:  # 读取二进制文件
    print (f1.read())


# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')  指定编码


 # f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
    # 有些编码不规范的文件，你可能会遇到UnicodeDecodeError，加个errors=ignore来忽略



# 写文件（a为追加，w为直接覆盖）-----------------------------

with open('demo1.txt','a') as f2:
    for num in [1,2,3,4,5,6,7,8,9,0]:
        f2.write('第%d行：%d\n' %(num,num))
    f2.flush()


# StringIO(内存中读写str)----------------------------------

from io import BytesIO as StringIO
from io import BytesIO

str = StringIO()

str.write('yang')
str.write(' ')
str.write('haipeng\n')

print (str.getvalue())


str1 = StringIO('yang\nhaipeng\nhello world\n')
for line in str1.readlines():
    print (line.strip())


# BytesIO(内存中读写byte)------------------------------------
byte = BytesIO()
byte.write('中文'.decode('utf-8').encode('utf-8'))
print (byte.getvalue())

byte1 = BytesIO('中文\n是最好的语言\n')
for line in byte1.readlines():
    print (line.strip())


# 操作文件和目录---------------------------------------------

import os

print (os.name)
print (os.uname())
print (os.environ)
print (os.environ.get('PATH'))
print (os.path.abspath('.'))
#os.mkdir(os.path.abspath('.') + '/test')  # 创建新目录
#os.rmdir(os.path.abspath('.') + '/test')

#os.rename()  # 重命名
#os.remove()  # 移除文件


# 序列化--------------------------------------
import pickle
d = dict(name='yang',age=25,score=98)
f = open('./demo.txt','ab')
pickle.dump(d,f)
f.close()


# 反序列化
f1 = open('./seriazble.txt','r')
d1 = pickle.load(f1)
print (d1)
f1.close()

import json
d2 = dict(name='Bob', age=20, score=88)
print (json.dumps(d2))

jsonStr = '{"age": 20, "score": 88, "name": "Bob"}'
print (json.loads(jsonStr))


class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

def student2Dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }




s = Student('yang',26,99)
print (json.dumps(s,default=student2Dict))  # class对象序列化为json


def dict2Student(d):
    return Student(d['name'],d['age'],d['score'])  # json反序列化为class对象

print (json.loads(jsonStr,object_hook=dict2Student))