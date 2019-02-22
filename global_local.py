#!/usr/bin/env python3

g = 3

def test():
    global g    
    g += 1
    print(g)

test()
