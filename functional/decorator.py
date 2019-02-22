#!/usr/bin/env python3

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call %s' % func.__name__)
        ret = func(*args, **kw)
        print('end call %s' % func.__name__)
        return ret
    return wrapper

@log
def f(x):
    print(x)

f(3)
 
