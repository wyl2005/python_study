#!/usr/bin/env python3


def _odd_iterator():
    n = 1
    while True:
        n = n+2
        yield n

def _not_divisible(n):
    return lambda x: x%n > 0

def primes():
    yield 2
    it = _odd_iterator() #init odd iterator: 3, 5, 7 ,9 ,11 ...
    while True:
        n = next(it)
        yield n
#        it = filter(lambda x: x % n > 0, it)  # output not correct
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 20:
        print(n)
    else:
        break
'''
for n in _odd_iterator():
    if n < 20:
        print(n)
    else:
        break
'''
