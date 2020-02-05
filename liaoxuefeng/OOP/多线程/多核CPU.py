# -*- coding:utf-8 -*-

#写个死循环，观察CPU使用率

import threading,multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()