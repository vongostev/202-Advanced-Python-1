# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 21:15:22 2021

@author: grego
"""


def is_even(x):
    if x > 0:
        print("number must be not negative")
    if (x % 2) == 0:
        return True
    else:
        return False


def generate_squares(min_num, max_num):
    squares = []
    for i in range(min_num, max_num + 1):
        squares.append(i*i)
    return squares


def split_list(input_list):
    splited = []
    for element in input_list:
        if element:
            splited.append(element)
    return(splited)


def make_dict(input_list):
    dictionary = {'str': [], 'num': []}
    for element in input_list:
        if isinstance(element, int):
            dictionary['num'].append(element)
        else:
            dictionary['str'].append((element, len(element)))
    return dictionary


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return '({x}, {y})'.format(x=self.x, y=self.y)

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
    if __name__ == '__main__':    

    def test_is_even():
        assert is_even(-240)
        assert not is_even(-17)
        assert is_even(0)
        assert is_even(12)
        assert not is_even(131)
        print('is_even correct')
        
    def test_generate_squares():
        assert generate_squares(0, 1) == [0, 1]
        assert generate_squares(-1, 1) == [1, 0, 1]
        assert generate_squares(-5, -5) == [25]
        assert generate_squares(5, 4) == []
        assert generate_squares(0, 4) == [0, 1, 4, 9, 16]
        print('generate_squares correct')
        
    def test_split_list():
        assert split_list([0]) == []
        assert split_list([0, 0, 0]) == []
        assert split_list([-1, 1, 1]) == [-1, 1, 1]
        assert split_list([-1, 0, 1]) == [-1, 1]
        assert split_list([1, 0, 0, 0, 0]) == [1]
        print('split_list correct')
        
    def test_make_dict():
        assert make_dict([1, 2, 3, 4]) == {'str': [], 'num': [1, 2, 3, 4]}
        assert make_dict([]) == {'str': [], 'num': []}
        assert make_dict(['1', 1, '22', 22, '333', 333, '4444', 4444]) == {'str': [
            ('1', 1), ('22', 2), ('333', 3), ('4444', 4)], 'num': [1, 22, 333, 4444]}
        print('make_dict correct')
        
    def test_vector2D():
        zero_vector = Vector2D()
        first = Vector2D(1, 1)
        second = Vector2D(-3, 4)
        assert str(zero_vector) == '(0, 0)'
        assert second.norm() == 5
        assert (first == Vector2D(1, 1))
        assert (first == second) == False
        assert (first < second)
        assert (first > Vector2D(-1, 0))
        assert (first >= Vector2D(1, 1))
        assert (first <= Vector2D(3, 4))
        print('Vector2D correct')
        
    test_is_even()
    test_generate_squares()
    test_split_list()
    test_make_dict()
    test_vector2D()    
