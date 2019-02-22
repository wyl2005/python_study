#!/usr/bin/env python3

L = [('Bob', 90), ('adam', 88), ('Lisa', 60), ('curry',66)]

def by_name(n):
    print('n =', n)    
    return n[0].lower()    
#    return n[0]    

def by_score(n):
    return n[1]

print(sorted(L, key=by_name))
print(sorted(L, key=by_score, reverse=True))
