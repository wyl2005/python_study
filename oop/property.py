#!/usr/bin/python

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
  
    @property
    def area(self):
        return self._height * self._width

s = Screen()
s.width = 10
print(s.width)
s.height = 20

print(s.area)
