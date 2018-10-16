#!/usr/bin/python
# -*-coding: UTF-8 -*-

# 多线程

import threading,time

# def loop():
#     print ('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print ('thread %s >>> %s' % (threading.currentThread().name,n))
#         time.sleep(1)
#     print ('thread %s ended.' % threading.currentThread().name)
#
#
# print ('thread %s is running...' % threading.currentThread().name)
# t = threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print ('thread %s ended.' % threading.currentThread().name)



# 使用多线程，而不同步，造成数据错乱-----------------------------

balance = 0

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))

t1.start()
t2.start()

t1.join()
t2.join()

print (balance)



#使用多线程，使用同步-----------------------------

# balance = 0
# lock = threading.Lock()
#
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     lock.acquire()
#     for i in range(100000):
#         try:
#             print (threading.currentThread().name)
#             change_it(n)
#         finally:
#             lock.release()
#
# t1 = threading.Thread(target=run_thread,args=(5,))
# t2 = threading.Thread(target=run_thread,args=(8,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print (balance)

# 多核CPU--------------------------------------------

import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

t = threading.Thread(target=loop)
t.start()

# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()