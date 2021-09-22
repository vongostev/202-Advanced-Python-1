def is_even(a):
        if a < 0:
            print('(-_-)Вы ввели отрицательное число(-_-)')
        return a % 2 == 0


def generate_squares(min_num, max_num):
    ans = []
    for i in range(min_num, max_num + 1):
        ans.append(i * i)
    return ans


def split_list(s):
    ans = []
    for i in range(len(s)):
        if s[i] != 0:
            ans.append(s[i])
    return ans


def make_dict(l):
    s = []
    n = []
    for i in l:
        if type(i) == str:
            s.append((i, len(i)))
        else:
            n.append(i)
    return {'str': s, 'num': n}


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x * self.x + self.y * self.y) ** (1 / 2)

    def __str__(self):
        return '(x, y) = ({}, {})'.format(self.x, self.y)

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
        q = [-240, -17, 0, 12, 131]
        a = [True, False, True, True, False]
        for i in range(len(q)):
            assert is_even(q[i] == a[i])
        print('is_even - correct')

    def test_generate_squares():
        assert generate_squares(1, 0) == []
        assert generate_squares(0, 2) == [0, 1, 4]
        print('generate_squares - correct')

    def test_split_list():
        assert split_list([0, 0, 0]) == []
        assert split_list([1, 2, 3]) == [1, 2, 3]
        assert split_list([0, 0, 1]) == [1]
        print('split_list - correct')

    def test_make_dict():
        assert make_dict([1, 2, 3]) == {'str': [], 'num': [1, 2, 3]}
        assert make_dict([]) == {'str': [], 'num': []}
        assert make_dict(['1', 1, '22', 22, '333', 333]) == {'str': [
            ('1', 1), ('22', 2), ('333', 3)], 'num': [1, 22, 333]}
        print('make_dict - correct')

    def test_vector2D():
        first = Vector2D(1, 1)
        second = Vector2D(0, 1)
        assert second.norm() == 1
        assert (first == first)
        assert if (first == second) is False
        assert (first > second)
        assert if (first < second) is False
        assert if (first <= second) is False
        assert (first >= second)
        assert 5 * first == Vector2D(5, 5)
        assert second * 2 == Vector2D(0, 2)
        assert (first + second) == Vector2D(1, 2)
        assert (second - first) == Vector2D(-1, 0)
        print('Vector2D - correct')

    test_is_even()
    test_generate_squares()
    test_split_list()
    test_make_dict()
    test_vector2D()
