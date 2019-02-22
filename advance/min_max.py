#!/usr/bin/env python3

def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)

    min = L[0]
    max = L[0]
    for k in L:
        if k < min:
            min=k
        if k > max:
            max=k
    return (min, max)




if findMinAndMax([]) != (None, None):
    print('fail1')
elif findMinAndMax([1,4,6,4,9,0]) != (0, 9):
    print('fail3')
elif findMinAndMax([7, 7]) != (7, 7):
    print('fail2')
elif findMinAndMax([7, 1]) != (1, 7):
    print('fail4')
else:
    print('sucess')

