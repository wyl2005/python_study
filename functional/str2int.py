#!/usr/bin/env python3

from functools import reduce

DIGITS = {'0':0, '1':1, '2':2, '3':3 , '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

def str2int(s):
    def char2int(x):
        return DIGITS[x]

    def fn(x, y):
        return x*10 + y

    return reduce(fn, map(char2int, s))


s=str2int('123988')

print(s)
print(str2int('11111'))
