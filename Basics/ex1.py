# Grigoriev Semyon
def is_even(i):
    if i < 0:
        print('Warning! Function undefined for negative numbers')
    return True if (i % 2 == 0) else False


def generate_squares(min_num, max_num):
    list = []
    for i in range(min_num, max_num + 1):
        list.append(i * i)
    return list


def split_list(list):
    relist = []
    for i in range(0, len(list)):
        if list[i]:
            relist.append(list[i])
    return relist


def make_dict(list):
    str_list, num_list = [], []
    for i in range(0, len(list)):
        if isinstance(list[i], str):
            str_list.append([list[i], len(list[i])])
        else:
            num_list.append(list[i])
    return {'str': str_list, 'num': num_list}


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def __str__(self):
        return '(' + str(self.x) + '; ' + str(self.y) + ')'

    def __lt__(self, other):
        return self.norm() < other.norm()

    def __le__(self, other):
        return self.norm() <= other.norm()

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, num):
        return Vector2D(num * self.x, num * self.y)

    def __rmul__(self, num):
        return Vector2D(num * self.x, num * self.y)


# Tests
def is_even_test():
    assert is_even(-240)
    assert not is_even(-17)
    assert is_even(0)
    assert is_even(12)
    assert not is_even(131)
    print("1 - correct")


def generate_squares_test():
    assert generate_squares(1, 6) == [1, 4, 9, 16, 25, 36]
    assert generate_squares(-5, -1) == [25, 16, 9, 4, 1]
    assert generate_squares(0, 0) == [0]
    assert generate_squares(-5, 5) == [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25]
    assert generate_squares(0, 2) == [0, 1, 4]
    assert generate_squares(-2, 0) == [4, 1, 0]
    print('2 - correct')


def split_list_test():
    assert split_list([0, 0, 0]) == []
    assert split_list([]) == []
    assert split_list([1, 2, 3]) == [1, 2, 3]
    assert split_list([-1, -2, -3]) == [-1, -2, -3]
    assert split_list([-2, -1, 0, 1, 2]) == [-2, -1, 1, 2]
    assert split_list([-2, -1, 1, 2]) == [-2, -1, 1, 2]
    print("3 - correct")


def make_dict_test():
    assert make_dict([]) == {'str': [], 'num': []}
    assert make_dict([1, 3, 8, 9, 'list', 5, 91, -1, 'a']) == {'str': [['list', 4], ['a', 1]],
                                                               'num': [1, 3, 8, 9, 5, 91, -1]}
    assert make_dict([0]) == {'str': [], 'num': [0]}
    assert make_dict(['list']) == {'str': [['list', 4]], 'num': []}
    print("4 - correct")


def vector2d_test():
    zero = Vector2D()
    a = Vector2D(3, 4)
    b = Vector2D(-1, 2)
    c = Vector2D(-3, 4)
    e = Vector2D(3, 4)

    assert a.norm() == 5
    assert zero.norm() == 0
    assert c.norm() == 5
    assert a.norm() > b.norm()
    assert a == e
    assert a > b
    assert a >= e
    assert a >= b
    assert c >= a
    assert b < e
    assert b <= a
    assert a != b
    assert a != zero
    assert str(a) == "(3; 4)"
    assert str(b) == "(-1; 2)"
    assert str(zero) == "(0; 0)"
    print("5.1 - correct")

    assert a + b == Vector2D(2, 6)
    assert a - b == Vector2D(4, 2)
    assert a * 10 == Vector2D(30, 40)
    assert 10 * a == Vector2D(30, 40)
    print("5.2 - correct")


if __name__ == '__main__':
    is_even_test()
    generate_squares_test()
    split_list_test()
    make_dict_test()
    vector2d_test()
    # Everything works
