#!/usr/bin/env python3
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw) 
    return wrapper 
#now = log(now)
@log
def now():
    print('2018.12.27') 

now()

print(now.__name__)

def log1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s call %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


#now1 = log1('execute')(now1)
@log1('execute')
def now1():
    print('2018.12.27 1')

#now1 = log1('exe')(now)
now1()
print(now1.__name__)


print(__name__)
