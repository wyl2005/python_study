#!/usr/bin/env python3

L = ['Hello', 'World', 18, 'Apple', None] 

print('L=', L)

L2 = [k.lower() for k in L if isinstance(k, str)]

print('L2=', L2)

if L2 == ['hello', 'world', 'apple']:
    print('success')
else:
    print('fail')
