
'''
# -*- coding: utf-8 -*-
#下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，
# 这和命令行直接运行的效果是一样的：

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)
'''

'''
#如果子进程还需要输入，则可以通过communicate()方法输入：
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:',p.returncode)
'''


#进程间通信
#Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等
# 多种方式来交换数据。我们以Queue为例，在父进程中创建两个子进程，一个
# 往Queue里写数据，一个从Queue里读数据：
from multiprocessing import Process,Queue
import os,time,random

#写数据进程执行的代码：
def write(q):
    print('Process to write:%s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

#读数据进程执行的代码：
def read(q):
    print('Process to read:%s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ =='__main__':
    #父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    #启动子进程pw，写入：i
    pw.start()
    #启动子进程pr,读取：
    pr.start()
    #等待pw结束：
    pw.join()
    #pr进程里是死循环，无法等待其结束，只能强行终止：
    pr.terminate()


