# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def is_even(x):
    if x < 0:
        print("is_even::warn::num is negative!\n")
    return x % 2 == 0    
    

def generate_squares(min_num, max_num):
    sqrs = []
    for x in range(min_num, max_num+1):
        sqrs.append(x*x)
    return sqrs

def split_list(in_arr):
    out_arr = []
    for val in in_arr:
        if val != 0:
            out_arr.append(val)
    return out_arr

def make_dict(in_arr):
    out_arr = {"str": [], "num":[]}
    for val in in_arr:
        if type(val) == str:
            out_arr["str"].append((val, len(val)))
        else:
            out_arr["num"].append(val)
    return out_arr




class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def norm(self):
        return (self.x*self.x + self.y*self.y)**0.5
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __lt__(self, other):
        return self.norm() < other.norm()
    
    def __le__(self, other):
        return self.norm() <= other.norm()
    
    def __gt__(self, other):
        return self.norm() > other.norm()
    
    def __ge__(self, other):
        return self.norm() >= other.norm()
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
    
    
if __name__ == "__main__":
    
    assert is_even(-240)    is True
    assert is_even(-17)     is False
    assert is_even(0)       is True
    assert is_even(12)      is True
    assert is_even(131)     is False
    
    assert generate_squares(0, +11) == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
    assert generate_squares(-11, 0) == [121, 100, 81, 64, 49, 36, 25, 16, 9, 4, 1, 0]
    
    assert split_list([0,1,0,2,0,3,0,4,0,5]) == [1,2,3,4,5]
    assert split_list([0,0,0,0,0,0,0,0,0,0]) == []
    
    assert make_dict([1,2,3,45,0]) == {"str":[], "num":[1,2,3,45,0]}
    assert make_dict(["pithon", "zlo", 228]) == {"str":[("pithon", 6), ("zlo", 3)], "num":[228]}
    
    
    
    a = Vector2D(+1,+1)
    b = Vector2D(-1,-1)
    
    assert a.norm() == 2**0.5
    assert b.norm() == 2**0.5
    assert str(a) == "(1, 1)"
    assert str(b) == "(-1, -1)"
    assert (a > b) is False
    assert (a >= b) is True
    assert (a < b) is False
    assert (a <= b) is True
    assert (a == b) is False
    assert (a != b) is True