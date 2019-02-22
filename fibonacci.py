#!/usr/bin/env python3

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
       # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done!!'

g = fib(9)

while True:
    try:
        x = next(g)
        print('x=', x)
    except StopIteration as e:
        print('generator return value:', e.value)
        break
