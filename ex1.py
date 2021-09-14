def is_even(a):
    if (a < 0):
        print("Warning: The number is negative")
    return a % 2 == 0


def generate_squares(min_num, max_num):
    l = []
    for i in range(min_num, max_num + 1):
        l.append(i * i)
    return l


def split_list(l):
    k = []
    for elem in l:
        if elem:
            k.append(elem)
    return k


def make_dict(l):
    d = {'str': [], 'num': []}
    for elem in l:
        if isinstance(elem, str):
            d['str'].append((elem, len(elem)))
        else:
            d['num'].append(elem)
    return d


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x * self.x + self.y * self.y) ** (1 / 2)

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


if __name__ == '__main__':

    def test_is_even():
        assert is_even(-240)
        assert not is_even(-17)
        assert is_even(0)
        assert is_even(12)
        assert is_even(131)

    def test_generate_squares():
        assert generate_squares(0, 1) == [0, 1]
        assert generate_squares(-1, 1) == [1, 0, 1]
        assert generate_squares(-5, -5) == [25]
        assert generate_squares(-5, -4) == []
        assert generate_squares(0, 4) == [0, 1, 4, 9, 16]

    def test_split_list():
        assert split_list([0]) == []
        assert split_list([0, 0, 0]) == []
        assert split_list([-1, 1, 1]) == [-1, 1, 1]
        assert split_list([-1, 0, 1]) == [-1, 1]
        assert split_list([1, 0, 0, 0, 0]), [1]

    def test_make_dict():
        assert make_dict([1, 2, 3, 4]) == {'str': [], 'num': [1, 2, 3, 4]}
        assert make_dict([]) == {}
        assert make_dict(['1', 1, '22', 22, '333', 333, '4444', 4444]) == {'str': [
            ('1', 1), ('22', 2), ('333', 3), ('4444', 4)], 'num': [1, 22, 333, 4444]}

    def test_vector2D():
        zero_vector = Vector2D()
        first = Vector2D(1, 1)
        second = Vector2D(-3, 4)
        assert str(zero_vector) == '(0, 0)'
        assert second.norm() == 5
        assert (first == first)
        assert (first == second) == False
        assert (first < second)
        assert (first > second) == False
        assert (first >= second) == False
        assert (first <= second)
        assert (first + second) == Vector2D(-2, 5)
        assert (second - first) == Vector2D(-4, 3)
        assert 5 * first == Vector2D(5, 5)
        assert second * 2 == Vector2D(-6, 8)

        test_is_even()
        test_generate_squares()
        test_split_list()
        test_make_dict()
