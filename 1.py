import numpy as np


def is_even(a):
    if a < 0:
        print('Error')
    if a % 2 == 0:
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
        return ('('+str(self.x)+', '+str(self.y)+')')

    def __lt__(self, other):
        return (Vector2D.norm(self)) < (Vector2D.norm(other))

    def __le__(self, other):
        return (Vector2D.norm(self)) <= (Vector2D.norm(other))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

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

    def __mul__(self, num):
        return Vector2D(self.x * num, self.y * num)

    def __rmul__(self, num):
        return Vector2D(self.x * num, self.y * num)


if __name__ == '__main__':
    def test_is_even():
        assert is_even(-2)
        assert not is_even(-1)
        assert is_even(0)
        assert is_even(2)
        assert not is_even(1)
        print('is_even correct')

    def test_generate_squares():
        assert generate_squares(0, 1) == [0, 1]
        assert generate_squares(-1, 1) == [1, 0, 1]
        assert generate_squares(1, 1) == [1]
        assert generate_squares(10, 1) == []
        assert generate_squares(0, 3) == [0, 1, 4, 9]
        print('generate_squares is correct')

    def test_split_list():
        assert split_list([0]) == []
        assert split_list([0, 0]) == []
        assert split_list([1, 0, 1]) == [1, 1]
        assert split_list([1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1]
        assert split_list([1, 0, 0, 0]) == [1]
        print('split_list is correct')

    def test_make_dict():
        assert make_dict([1, 2, 3]) == {'str': [], 'num': [1, 2, 3]}
        assert make_dict([]) == {'str': [], 'num': []}
        assert make_dict(['1', 2, '123', 123, 123, 'asd', '1', 2]) == {
            'str': [['1', 1], ['123', 3], ['asd', 3], ['1', 1]], 'num': [2, 123, 123, 2]}
        print('make_dict is correct')

    def test_Vector2D():
        a = Vector2D(1, 1)
        b = Vector2D(-4, 0)
        assert str(a) == '(1, 1)'
        assert b.norm() == 4
        # assert (a == a)
        assert (a == Vector2D(1, 1))
        assert not (a == b)
        assert (a < b)
        # assert not (a > b)
        assert not (a > Vector2D(-4, 0))
        # assert not (a >= b)
        assert not (a >= Vector2D(-4, 0))
        # assert (a <= b)
        assert (a <= Vector2D(-4, 0))
        assert (a + b) == Vector2D(-3, 1)
        assert (a - b) == Vector2D(5, 1)
        assert 2 * a == Vector2D(2, 2)
        assert b * 2 == Vector2D(-8, 0)
        print('Vector2D is correct')
    test_is_even()
    test_generate_squares()
    test_split_list()
    test_make_dict()
    test_Vector2D()