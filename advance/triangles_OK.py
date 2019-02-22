#!/usr/bin/env python3

def triangles():
    N = [1]
    count = 1
    while True:
        yield N
        S = N[:]
        S.append(0)
        N = [S[i-1] + S[i] for i in range(len(S))]
        count = count + 1
        if count > 10:
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


