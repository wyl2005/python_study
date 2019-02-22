#!/usr/bin/env python3


class Student(object):
    count = 0

    def __init__(self, name):
        
        Student.count += 1
        self.name = name

print(Student.count)

bart = Student('Bart')

print(bart.count)

lisa = Student('Lisa')
print(lisa.count)
print(Student.count)
'''
s = Student()
print(s.name)
print(Student.name)
s.name = 'mike'
print(s.name)
'''

