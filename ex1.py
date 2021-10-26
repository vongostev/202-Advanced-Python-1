def is_even(i):
    if i < 0:
        print('Warning: operation undefined for negative numbers')
    return True if (i % 2 == 0) else False


def generate_squares(min_number, max_number):
    l = []
    for i in range(min_number, max_number + 1):
        l.append(i*i)
    return l


def split_list(l):
    s = []
    for i in range(0, len(l)):
        if l[i]:
            s.append(l[i])
    return s


def make_dict(l):
    s = [] 
    n = []
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
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return '(' + str(self.x) + ';' + str(self.y) + ')'

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


if __name__ == "__main__":

    assert is_even(-240)
    assert not is_even(-17)
    assert is_even(0)
    assert is_even(12)
    assert not is_even(131)

    assert generate_squares(1, 3) == [1, 4, 9]
    assert generate_squares(0, 1) == [0, 1]
    assert generate_squares(-4, 3) == [16, 9, 4, 1, 0, 1, 4, 9]

    assert split_list([0, 0, 0]) == []
    assert split_list([-1, 0, 1]) == [-1, 1]
    assert split_list([0, 5, 0, 1, 0]) == [5, 1]

    assert make_dict([]) == {'str': [], 'num': []}
    assert make_dict([1, 2, 'word 1', 'number 1', 3, 'word 2', 0]) == {
        'str': [['word 1', 6], ['number 1', 8], ['word 2', 6]], 'num': [1, 2, 3, 0]}

    a = Vector2D()
    b = Vector2D(4, 3)
    assert a.norm() == 0
    assert b.norm() == 5
    assert str(a) == '(0;0)'
    assert str(Vector2D(3, 4)) == '(3;4)'
 


    assert Vector2D(0, 0) >= a
    assert Vector2D(1, 1) <= b
    assert Vector2D(1, 2) == Vector2D(1, 2)
    assert a != b
    

 