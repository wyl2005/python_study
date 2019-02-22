#!/usr/bin/env python3

def is_palindrome(n):
    L = str(n)
    if L == L[::-1]:
        return True
    else:
        return False

print(is_palindrome(123456))
print(is_palindrome(12321))
print('1~200:', list(filter(is_palindrome, range(1, 200))))

if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('success')
else:
    print('fail')
