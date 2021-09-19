import numpy as np


def is_even(number):
    if number < 0:
        return 'Error.'
    elif number % 2 == 0:
        return True
    else:
        return False


def generate_squares(min_num, max_num):
    l = []
    for i in range(max_num - min_num + 1):
        l.append((min_num + i) ** 2)
    return l


def split_list(unsorted_list):
    for i in range(unsorted_list.count(0)):
        unsorted_list.remove(0)
    return unsorted_list


def make_dict(some_list):
    l_num, l_str = [], []
    for i in range(len(some_list)):
        if isinstance(some_list[i], str):
            l_str.append([some_list[i], len(some_list[i])])
        else:
            l_num.append(some_list[i])
            return {'str': l_str, 'num': l_num}


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def norm(self):
        return np.sqrt((self.x)**2+(self.y)**2)

    def __str__(self):
        return ('('+self.x+','+self.y+')')

    def __lt__(self, other):
        return (Vector2D.norm(self)) < (Vector2D.norm(other))

    def __le__(self, other):
        return (Vector2D.norm(self)) <= (Vector2D.norm(other))

    def __eq__(self, other):
        return self is other

    def __ne__(self, other):
        return self is not other

    def __gt__(self, other):
        return (Vector2D.norm(self)) > (Vector2D.norm(other))

    def __ge__(self, other):
        return (Vector2D.norm(self)) >= (Vector2D.norm(other))

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2D(self.x * other, self.y * other)

    def __rmul__(self, other):
        return Vector2D(self.x * other, self.y * other)
