#!/usr/bin/python

import time, threading

def loop():
    print('thrad %s running...' % threading.current_thread().name)

    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s ' % (threading.current_thread().name, n))
        time.sleep(5)


print('main thread %s end' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('main thread %s end' % threading.current_thread().name)
