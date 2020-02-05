# -*- coding:utf-8 -*-
# task_master.py

'''
#以下代码在Unix/Linux下，测试程序可以正常运行，但如果实在Windows下，将会报错：
# 在Unix/Linux下，multiprocessing模块封装了fork（）调用，是我们不需要
# 关注fork（）的细节。由于windows没有fork调用，因此，multiprocessing需
# 要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列号再传到
# 子进程中去。所以，如果multiprocessing在Windows下调用失败了，要先考虑是
# 不是pickle失败了。Python3中模拟分布式调用时，如果是在Unix/Linux下，测
# 试程序可以正常运行，但如果实在Windows下，将会报错：

#官网中给出解释说明：pickle模块不能序列化lambda function，
# 故我们需要自行定义函数，实现序列化

import random,time,queue
from multiprocessing.managers import BaseManager

#发送任务的队列：
task_queue = queue.Queue()
#接收结果的队列：
result_queue = queue.Queue()

#从BaseManager继承的QueueManager：
class QueueManager(BaseManager):
    pass

#把两个Queue都注册到网络上，callable参数关联了Queue对象：
QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)
#绑定端口5000，设置验证码‘abc’：
manager = QueueManager(address=('',5000),authkey=b'abc')
#启动Queue：
manager.start()
#获得通过网络访问的Queue对象：
task = manager.get_task_queue()
result = manager.get_result_queue()
#放几个任务进去：
for i in range(10):
    n = random.randint(0,10000)
    print('Put task %d...' % n)
    task.put(n)
#从result队列读取结果：
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result:%s' % r)
#关闭：
manager.shutdown()
print('master exit.')
'''


import random,queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

class QueueManager(BaseManager):
    pass

if __name__ =='__main__':
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result:%s' % r)

    manager.shutdown()
    print('master exit.')