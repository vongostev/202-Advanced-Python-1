def is_even(i):
    if i < 0:
        print('Warning: Value', i, 'is negative')
    return True if (i % 2 == 0) else False


def generate_squares(min_num, max_num):
    l = []
    for i in range(min_num, max_num + 1):
        l.append(i*i)
    return l


def split_list(l):
    k = []
    for i in range(0, len(l)):
        if l[i]:
            k.append(l[i])
    return k


def make_dict(l):
    s, n = [], []
    for i in range(0, len(l)):
        if isinstance(l[i], str):
            s.append([l[i], len(l[i])])
        else:
            n.append(l[i])
    return {'str': s, 'num': n}


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** (1/2)

    def __str__(self):
        return '{' + str(self.x) + ';' + str(self.y) + '}'

    def __lt__(self, other):
        return self.norm() < other.norm()

    def __le__(self, other):
        return self.norm() <= other.norm()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

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

    def __mul__(self, number):
        return Vector2D(self.x * number, self.y * number)

    def __rmul__(self, number):
        return Vector2D(self.x * number, self.y * number)


if __name__ == "__main__":

    assert is_even(-240)
    assert not is_even(-17)
    assert is_even(0)
    assert is_even(12)
    assert not is_even(131)

    assert generate_squares(1, 3) == [1, 4, 9]
    assert generate_squares(-1, 1) == [1, 0, 1]
    assert generate_squares(4, 3) == []

    assert split_list([0, 0, 0]) == []
    assert split_list([-1, 0, 1]) == [-1, 1]
    assert split_list([1, 0, 3, 0]) == [1, 3]

    assert make_dict([]) == {'str': [], 'num': []}
    assert make_dict([1, 2, 'a', 6, 91, 'char', 0]) == {
        'str': [['a', 1], ['char', 4]], 'num': [1, 2, 6, 91, 0]}

    a = Vector2D()
    b = Vector2D(3, -4)
    assert a.norm() == 0
    assert b.norm() == 5
    assert str(Vector2D()) == '{0;0}'
    assert str(Vector2D(-6, 4)) == '{-6;4}'
    #print (Vector2D ())
    #print (Vector2D (-6, 4))

    assert Vector2D(1, 2) >= Vector2D(1, 2)
    assert Vector2D(1, 1) <= Vector2D(1, 2)
    assert Vector2D(-3, 6) == Vector2D(-3, 6)
    assert Vector2D(-3, 6) != Vector2D(6, -3)

    assert Vector2D() + Vector2D(1, 2) == Vector2D(1, 2)
    assert Vector2D(1, 4) - b == Vector2D(-2, 8)
    assert Vector2D(-2, 8) * 2 == Vector2D(-4, 16)
    assert 3 * Vector2D(4, -1) == Vector2D(12, -3)
