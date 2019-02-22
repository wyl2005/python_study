#!/usr/bin/env python3

# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Allan Wang'

import sys


def test():
    args = sys.argv
    print('sys.argv: %s' % sys.argv)
    print('len(sys.argv): %s' % len(sys.argv))
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello %s ' % args[1])
    else:
        print('too many arguments')

#print(__name__)

#if __name__=='__main__':
if __name__ == '__main__':
    test()
#else:
#    print('222')

#print(__name__)
