#!/usr/bin/env python3


import time
import functools


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start = time.time()
        f = func(*args, **kw)
        end = time.time()
        print('%s execute time: %s ms' % (func.__name__, end - start))
        return f
    #print('test')
    return wrapper

#fast = metic(fast)
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x+y
print('start1')

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z
print('start')

f = fast(11, 22)
s = 1
#s = slow(11, 22, 33)

if f != 33:
    print('fail')
elif s != 7986:
    print('fail')

    
