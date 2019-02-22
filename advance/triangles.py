#!/usr/bin/env python3


def triangles():
    n = 1
    L = []
    while True:
        
        if n == 1:
            L = [1]
            yield L
        elif n == 2:
            L= [1, 1]
            yield L
        else:
            #L1 = L #指针，没有重新负责List
            L1 = [j for j in L] #重新生成一样的List, same with: L1 = L[:]
            for i in range(1,n-1):
                L1[i] = L[i-1] + L[i]
            L1.append(1)
            L = L1
            #print('L=',L)
            #print('L1=', L1)
            yield L
            
        n = n + 1
        if n > 10:
            break
    return 'done'

#test
n = 0
results = []
print('t')
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

#tmp = [1, 1]
#results.append(tmp)

print('results:')
print(results)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')


