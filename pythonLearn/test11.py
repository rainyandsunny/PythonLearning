#!/usr/bin/python
# -*-coding: UTF-8 -*-

# 多进程

# import os
#
# print ('Process (%s) start' % (os.getpid()))
#
# pid = os.fork() # 子进程永远返回0，而父进程返回子进程的ID
#
# if pid == 0:
#     print ('I\'m child process (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
# else:
#     print ('I\'m (%s) just created a child process(%s).' % (os.getpid(),pid))


from multiprocessing import Process


#通过Process方式创建新的进程

def run_proc(name):
    print ("Run child process %s (%s)... " % (name,os.getpid()))

# if __name__ == '__main__':
#     print ("Parent process %s." % os.getpid())
#     p = Process(target=run_proc,args=('test',))
#     print ('Child process will start.')
#     p.start()
#     p.join()
#     print ('Child process end.')


# 进程池------------------------------------------

# from multiprocessing import Pool
# import os,time,random
#
# def long_time_task(name):
#     print ('Run task %s (%s)...' % (name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print ('Task %s runs %0.2f seconds.' % (name,(end - start)))
#
# if __name__ == '__main__':
#     print ('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print ('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print ('All subprocesses done.')


# 子进程--------------------------------------------
# import subprocess
#
# print ('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print ('Exit code: ',r)



# 子进程（需要输入）-----------------------------------

# import subprocess
# print ('$ nslookup')
# p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# output,err = p.communicate(b'set q=mx\n python.org\nexit\n')
# print (output.decode('utf-8'))
# print ('Exit code:',p.returncode)


# 进程间通信-------------------------------------------

# 进程间通信是通过Queue、Pipes等实现的

from multiprocessing import Process,Queue
import os,time,random


def write(q):
    print ('Process to write: %s' % (os.getpid()))
    for value in ['A','B','C']:
        print ('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print ('Process to read: %s' % (os.getpid()))
    while True:
        value = q.get(True)
        print ('Get %s from queue.' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()