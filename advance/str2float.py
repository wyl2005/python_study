#!/usr/bin/env python3

from functools import reduce

def str2float(s):
    n = 0
    L=[]
    #print(s)
    while n < len(s):
        if s[n] == '.':
            num = n
            #print('num =', num)
            #print(len(s) - num)
        else:
            L.append(int(s[n]))
        n = n + 1 
    #print('L=', L)
    #return reduce(lambda x, y: x * 10 + y, L)    
    f = reduce(lambda x, y: x * 10 + y, L)
    print(f)
    
    n = 1
    while n < len(s) - num:
        f = f/10
        n = n + 1
    
    #print('f = ', f)
    return f

#print(str2float('11.31312'))

print('str2float(\'123.456\') =', str2float('123.456'))

#if str2float('123.456') == 123.456:  #浮点数比较

if abs(str2float('123.456') - 123.456) < 0.000000001:  #< 0.00001:
    print('success!!')
else:
    print('fail')

#str2float('11.223') 
