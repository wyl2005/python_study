#!/usr/bin/python

class Student(object):
    def __init__(self,name):
        self.name =  name

    def __str__(self):
        return 'Student object name: %s' % self.name
    __repr__ = __str__


s = Student('Mike')
print(s)
print(Student('lily'))
