def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


def generate_squares(min_num, max_num):
    a = [k**2 for k in range(min_num, max_num+1)]
    return a


def split_list(a):
    a = list(filter(lambda x: x != 0, a))
    return a


def make_dict(a):
    lst1 = []
    lst2 = []
    for x in range(len(a)):
        if type(a[x]) == int:
            lst1.append(a[x])
        else:
            lst2.append([a[x], len(a[x])])
    dictionary = {'str': lst2, 'num': lst1}
    return dictionary


class Vector2D:

    def __init__(self, x, y):
        self.x, self.y = x, y

    def norm(self):
        return (self.x**2 + self.y**2)**0.5

    def __str__(self):
        return '{:g}i + {:g}j'.format(self.x, self.y)

    def __lt__(self, other):
        return self.norm() < other.norm()

    def __le__(self, other):
        return self.norm() <= other.norm()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __gt__(self, other):
        return self.norm() > other.norm()

    def __ge__(self, other):
        return self.norm() >= other.norm()

if __name__ == '__main__':

    assert is_even(-240) is True
    assert is_even(-17) is False
    assert is_even(0) is True
    assert is_even(12) is True
    assert is_even(131) is False

    assert generate_squares(0, 9) == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    assert split_list([0, 1, 4, 2, 0, 3, 0, 4, 0, 5]) == [1, 4, 2, 3, 4, 5]

    assert make_dict([4, 2, 5, 'musika', 0]) == {'str': [['musika', 6]], 'num': [4, 2, 5, 0]}

    a = Vector2D(1, 1)
    b = Vector2D(-1, -1)

    assert a.norm() == 2 ** 0.5
    assert b.norm() == 2 ** 0.5
    assert str(a) == '1i + 1j'
    assert str(b) == '-1i + -1j'
    assert (a > b) is False
    assert (a < b) is False
    assert (a == b) is False
    assert (a != b) is True