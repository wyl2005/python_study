#!/usr/bin/env python3

age = 20

if age >= 18:
	print('your age is', age)
	print('adult')


s = input('birth: ')

birth = int(s)
if birth > 2000:
	print('00后')
else:
	print('00前')
