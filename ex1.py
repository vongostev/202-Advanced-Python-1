# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 21:15:22 2021

@author: grego
"""

def is_even(x):
    assert x > 0, "number must be not negative"
    if (x % 2) == 0:
        return True
    else:
        return False
    
def generate_squares (min_num, max_num):
    squares = []
    for i in range(min_num, max_num, 1):
        squares.append(i*i)
    return squares

def split_list(input_list):
    splited = []
    for element in input_list:
        if element:
            splited.append(element)
    return(splited)

def is_number(input_string):
    number = ['0','1','2','3','4','5','6','7','8','9']
    for element in input_string:
        if number.count(element) == 0:
            return False
    return True
  
def make_dict(input_list):
    dictionary = {'str' : [], 'num': []}
    for element in input_list:
        if is_number(element):
            dictionary['num'].append(element)
        else:
            dictionary['str'].append((element, len(element)))
    return dictionary
 
class Vector2D:
    x = 0
    y = 0
    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __str__(self):
        return '({x},{y})'.format(x = self.x, y = self.y)
    
    def __lt__(self, another):
        return self.norm() < another.norm()
    
    def __le__(self, another):
        return self.norm() <= another.norm()
    
    def __gt__(self, another):
        return self.norm() > another.norm()
    
    def __ge__(self, another):
        return self.norm() >= another.norm()
    
    def __eq__(self, another):
        return (self.x == another.x) and (self.y == another.y)
    
    def __ne__(self, another):
        return (self.x != another.x) or (self.y != another.y)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    