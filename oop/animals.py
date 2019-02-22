#!/usr/bin/env python3

class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('Dog is running')  
    pass

class Cat(Animal):
    def run(self):
        print('Cat is running')  
    pass

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly')

class Timer(object):
    def run(self):
        print('start...')

def run_twice(x):
    x.run()
    x.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()

print(isinstance(dog, Animal))
print(isinstance(dog, Dog))

run_twice(Animal())
run_twice(Cat())
run_twice(Tortoise())

t = Timer()
run_twice(t)
