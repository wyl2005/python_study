#!/usr/bin/env python3

def trim(s):

	if len(s) == 0:
		return s

	while len(s)!=0 and s[0] == ' ':
		s = s[1:]

	while len(s)!=0 and s[-1] == ' ':
		s = s[:-1]
	
	return s



# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功7!')

	
