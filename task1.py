# задача 1
def is_even (x) :
    if x < 0 :
        print("отрицательное значение")
    return x % 2 == 0

# задача 2
def generate_squares(min_num, max_num):
    resl = []
    for x in range(min_num, max_num + 1):
        resl.append(x ** 2)
    return resl

# задача 3
def split_list(unsorted_list):
    for resl in range(unsorted_list.count(0)):
        unsorted_list.remove(0)
    return unsorted_list

# задача 4
def make_dict(some_list):
    l_num, l_str = [], []
    for i in range(len(some_list)):
        if isinstance(some_list[i], str):
            l_str.append([some_list[i], len(some_list[i])])
        else:
            l_num.append(some_list[i])
    return {'str': l_str, 'num': l_num}

# задача 5
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
    # Tests
    # 1
    assert is_even(-240) is True
    assert is_even(-17) is False
    assert is_even(0) is True
    assert is_even(12) is True
    assert is_even(131) is False
    print("Tests for task 1 passed")

    # 2
    assert generate_squares(1, 10) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert generate_squares(3, 1) == []
    assert generate_squares(786, 786) == [786 ** 2]
    assert generate_squares(-12, -8) == [144, 121, 100, 81, 64]
    assert generate_squares(-3, 1) == [9, 4, 1, 0, 1]
    print("Tests for task 2 passed")

    # 3
    assert split_list([1, 0, 2, 0, 3, 4, 0]) == [1, 2, 3, 4]
    assert split_list([]) == []
    assert split_list([10, 11, 14, 17]) == [10, 11, 14, 17]
    assert split_list([0, 0, 0, 0, 0]) == []
    assert split_list([0, 0, 0, 123, 0]) == [123]
    print("Tests for task 3 passed")

    # 4
    assert make_dict([1, 2, 3]) == {'str': [], 'num': [1, 2, 3]}
    assert make_dict([]) == {'str': [], 'num': []}
    assert make_dict(['1', 2, '123', 123, 123, 'asd', '1', 2]) == {'str': [['1', 1], ['123', 3], ['asd', 3], ['1', 1]],
                                                                   'num': [2, 123, 123, 2]}
    print('Tests for task 4 passed')

    # 5
    a = Vector2D()
    b = Vector2D(3, -4)
    assert a.norm() == 0
    assert b.norm() == 5
    assert str(Vector2D()) == '{0;0}'
    assert str(Vector2D(-6, 4)) == '{-6;4}'
    # print (Vector2D ())
    # print (Vector2D (-6, 4))

    assert Vector2D(1, 2) >= Vector2D(1, 2)
    assert Vector2D(1, 1) <= Vector2D(1, 2)
    assert Vector2D(-3, 6) == Vector2D(-3, 6)
    assert Vector2D(-3, 6) != Vector2D(6, -3)

    assert Vector2D() + Vector2D(1, 2) == Vector2D(1, 2)
    assert Vector2D(1, 4) - b == Vector2D(-2, 8)
    assert Vector2D(-2, 8) * 2 == Vector2D(-4, 16)
    assert 3 * Vector2D(4, -1) == Vector2D(12, -3)
    print('Tests for task 5 passed')