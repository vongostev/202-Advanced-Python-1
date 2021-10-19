def is_even(arg):

    if(arg <= 0):
        print("Число должно быть положительным")
        return(False)
    if (arg % 1 != 0):
        print("Число должно быть натуральным")
        return(False)

    return (arg % 2 == 0)


def generate_squares(min_num, max_num):

    lis = []
    for i in range(min_num, max_num+1):
        lis.append(i*i)

    return (lis)


def split_list(lis):

    new = []
    for elt in lis:
        if elt:
            new.append(elt)

    return (new)


def make_dict(lis):
    dic = {"str": [], "num": []}
    for elt in lis:
        if isinstance(elt, str):
            dic["str"].append((elt, len(elt)))
        else:
            dic["num"].append(elt)
    return dic


class Vector2D:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x * self.x + self.y * self.y) ** (0.5)

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
    assert is_even(-240) == False
    assert is_even(-17) == False
    assert is_even(0) == False
    assert is_even(12) == True
    assert is_even(131) == False


def test_generate_squares():
    assert generate_squares(1, 1) == [1]
    assert generate_squares(-1, 1) == [1, 0, 1]
    assert generate_squares(-2, -2) == [4]
    assert generate_squares(-1, -5) == []
    assert generate_squares(0, 5) == [0, 1, 4, 9, 16, 25]


def test_split_list():
    assert split_list([0]) == []
    assert split_list([0, 0]) == []
    assert split_list([2, 5, 6]) == [2, 5, 6]
    assert split_list([-0, 0, 1, 9]) == [1, 9]
    assert split_list([2, 0, 2, 0, 0]) == [2, 2]


def test_make_dict():
    assert make_dict([1, 1, 1, 1]) == {'str': [], 'num': [1, 1, 1, 1]}
    assert make_dict([]) == {'str': [], 'num': []}


def test_vector2D():
    zero_vector = Vector2D()
    first = Vector2D(1, 2)
    second = Vector2D(-3, 4)
    assert(zero_vector == '(0, 0)')
    assert(second.norm() == 5)
    assert first == Vector2D(1, 2) == True
    assert(first == second) == False
    assert(first < second) == True
    assert(first > second) == False
    assert(first >= second) == False
    assert(first <= second) == True
    assert(first + second) == Vector2D(-2, 6)
    assert(second - first) == Vector2D(-4, 2)
    assert(first * 5) == Vector2D(5, 10)
    assert(5 * first) == Vector2D(5, 10)
    assert(Vector2D.dotproduct(first, second)) == Vector2D(-3, 8)


if __name__ == "__main__":
    test_is_even()
    test_generate_squares()
    test_split_list()
    test_make_dict()
    test_vector2D()

