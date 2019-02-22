#!/usr/bin/env python3


bmi=80.5/1.75/1.75
print('bmi %s' % bmi)

if bmi < 18.5:
	print('低于18.5：过轻')
elif bmi < 25:
	print('18.5-25：正常')
elif bmi < 28:
	print('25-28：过重')
	

