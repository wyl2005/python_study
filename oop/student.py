#!/usr/bin/env python3

class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            raise ValueError('bad gender')
        
bart = Student('Bart', 'male')

if bart.get_gender() != 'male':
    print('fail')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('fail')
    else:
        print('success')

print(bart.get_gender())
print(type(bart))
