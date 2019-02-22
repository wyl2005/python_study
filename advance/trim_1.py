#!/usr/bin/env python3

def trim(s):

	if len(s) == 0:
		return s

	if s[0] == ' ':
		return trim(s[1:])

	if s[-1] == ' ':
		return trim(s[:-1])

	return s

if trim('hello  ') != 'hello':
	print('fail 1') 
elif trim('  hello') != 'hello':
	print('fail 2')
elif trim('  hello world  ') != 'hello world':
	print('fail 3')
elif trim('') != '':
	print('fail 4')
elif trim('    ') != '':
	print('fail 5')
else:
	print('success')
