#!/usr/bin/python


try:
    print('try...')
    r = 10 /0
    print('result:' , r)

except Exception as e:
#except ZeroDivisionError as e:
    print('expect :', e)

finally:
    print('finally...')

print('END')

'''
try:
    print('try')  
    r = 10 / int('a')

    print('result:' , r)

except ValueError as e:
    print('ValueError',e)

except ZeroDivisionError as e:
    print('zero division error,', e)
'''

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except Exception as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')
