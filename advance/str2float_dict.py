#!/usr/bin/env python3
from functools import reduce

def char2digits(s):
    d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '.':'.'}
    return d[s]

def str2float(s):
    L = map(char2digits, s)

    global p
    p = 0

    def fn(x, y):
        global p
        if y == '.':
            p = 1
            return x
        elif p == 0:
            return x*10 + y
        else:
            p = p+1
            print('pp = ', p)
            return x + 0.1**(p - 1)*y

    print('p = ', p)
    return reduce(fn, L)


#L = map(char2digits, '123.567')
#print(list(L))
print(str2float('123.4588886'))


