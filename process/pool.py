#!/usr/bin/python

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s %s' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s run %0.2f seconds' % (name, end-start))
    #print('Task %s run % seconds' % (name, end-start))


#print(__name__)


p = Pool(5)

for i in range(5):
    p.apply_async(long_time_task, args=(i,))

print('wait for all child process done...')
p.close()
p.join()

