#!/usr/bin/env python3

from functools import reduce

def prod(L):
    return reduce(lambda x, y: x*y, L)

print(prod([1,2,3,4,6,7]))
