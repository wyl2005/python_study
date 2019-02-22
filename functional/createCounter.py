#!/usr/bin/env python3

'''
def createCounter():
    i = [0]
    def counter():
        i[0] = i[0] + 1
        return i[0]
    return counter

c1 = createCounter()
print(c1(), c1(), c1())
'''
#error

def count():
#    for i in range(1, 4):
    j = 3
    i = 0
    def f():
        nonlocal i
        i = i + 1
        return i
    return f

f = count()

print(f(), f(), f(), f())


'''
def createCounter():
    def counter():
        n = 1
        while True:
            yield n
            n = n + 1
    c = counter()

    def fn():
        return next(c)

    return fn

f = createCounter()
print(f(), f(), f(),f())
'''
