#!/usr/bin/python

import os


print('process %s start' % os.getpid())

pid = os.fork()

if pid == 0:
    print('child process pid = %s' % os.getpid())
else:
    print('father , child pid = %s' %   os.getpid())
