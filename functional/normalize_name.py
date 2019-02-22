#!/usr/bin/env python3


def _normalize(s):
    n = 1
    y = ''
    for x in s:
        if n == 1:
            x = x.upper()
        else:
            x = x.lower()
        y = y + x
        n = n + 1
    return y

        
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(_normalize, L1))
print(L2)

