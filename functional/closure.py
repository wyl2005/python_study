#!/usr/bin/env python3

def count():
    fs = []
    def f(i):
        def g():
            return i*i
        return g

    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
