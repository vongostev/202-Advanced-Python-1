def is_even(a):

    if (a < 0):

        print("minus tut kak tut")

    return (a % 2) == 0


def generate_squares(min_num, max_num):
    q = []
    for i in range(min_num, max_num + 1):
        q.append(i * i)
    return q


def split_list(q):
    m = []
    for elem in q:
        if elem != 0:
            m.append(elem)
    return m


def make_dict(q):
    str_ = []
    number = []
    for elem in q:
        if isinstance(elem, int):
            number.append(elem)
        else:
            str_.append((elem, len(elem)))
    return {'str':  str_, 'num': number}


class Vector2D:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def __str__(self):
        return '({x}, {y})'.format(x=self.x, y=self.y)

    def __lt__(self, other):
        return self.norm() < other.norm()

    def __le__(self, other):
        return self.norm() <= other.norm()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, n):
        return Vector2D(self.x * n, self.y * n)

    def __rmul__(self, n):
        return Vector2D(self.x * n, self.y * n)


def test_is_even():
    assert is_even(-240) == True
    assert is_even(-17) == False
    assert is_even(0) == True
    assert is_even(12) == True
    assert is_even(131) == False


def test_generate_squares():
    assert generate_squares(1, 1) == [1]
    assert generate_squares(-1, 1) == [1, 0, 1]
    assert generate_squares(-2, -1) == [4, 1]
    assert generate_squares(3, 6) == [9, 16, 25, 36]
    assert generate_squares(0, 4) == [0, 1, 4, 9, 16]


def test_split_list():
    assert split_list([0]) == []
    assert split_list([0, 0, 0]) == []
    assert split_list([-1, 2, 1]) == [-1, 2, 1]
    assert split_list([-3, 0, 5]) == [-3, 5]
    assert split_list([1, 0, 4, 0, 7]) == [1, 4, 7]
    print('split_list correct')


def test_make_dict():
    assert make_dict([1, 2, 3, 4, 5]) == {
        'str': [], 'num': [1, 2, 3, 4, 5]}
    assert make_dict([]) == {'str': [], 'num': []}
    assert make_dict(['1', 1, '22', 22, '333', 333, '4444', 4444]) == {'str': [
        ('1', 1), ('22', 2), ('333', 3), ('4444', 4)], 'num': [1, 22, 333, 4444]}
    print('make_dict correct')


def test_vector2D():
    zero_vector = Vector2D()
    first = Vector2D(1, 1)
    second = Vector2D(-12, 5)
    assert str(zero_vector) == '(0, 0)'
    assert second.norm() == 13
    assert (first == Vector2D(1, 1))
    assert (first == second) == False
    assert (first < second) == True
    assert (first > Vector2D(-1, 0))
    assert (first >= Vector2D(1, 1))
    assert (first <= Vector2D(3, 4))
    assert (first + second) == Vector2D(-11, 6)
    assert (second - first) == Vector2D(-13, 4)
    assert 5 * first == Vector2D(5, 5)
    assert second * 2 == Vector2D(-24, 10)
    print('Vector2D correct')


if __name__ == '__main__':

    test_is_even()
    test_generate_squares()
    test_split_list()
    test_make_dict()
    test_vector2D()


