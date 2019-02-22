#!/usr/bin/env python3


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
    
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

lisa = Student('Lisa', 80)
bart = Student('Bart', 99)

print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())

lisa.age = 19
lisa.name = 'lisa ss'
print(lisa.age, lisa.name)
