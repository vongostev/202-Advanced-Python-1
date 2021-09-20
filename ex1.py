import math


def is_even(i):
    if i < 0:
        print('The number is negative')
    return True if (i % 2 == 0) else False


def generate_squares(m1, m2):
    l = []
    if m1 < 0:
        i = 0
    else:
        i = math.ceil(math.sqrt(m1))
    while not i ** 2 > m2:
        l.append(i ** 2)
        i += 1
    return l


def split_list(l):
    for i in range(0, l.count(0)):
        l.remove(0)
    return l


def make_dict(l):
    s, n = [], []
    for i in range(0, len(l)):
        if isinstance(l[i], str):
            s.append([l[i], len(l[i])])
        else:
            n.append(l[i])
    return {'str': s, 'num': n}


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return '{' + str(self.x) + ', ' + str(self.y) + '} '

    def __lt__(self, other):
        return True if self.norm() < other.norm() else False

    def __le__(self, other):
        return True if self.norm() <= other.norm() else False

    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False

    def __ne__(self, other):
        return False if self.x == other.x and self.y == other.y else True

    def __gt__(self, other):
        return True if self.norm() > other.norm() else False

    def __ge__(self, other):
        return True if self.norm() >= other.norm() else False

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2D(self.x * other, self.y * other)

    def __rmul__(self, other):
        return Vector2D(self.x * other, self.y * other)


def main():
    assert is_even(24)
    # print(generate_squares(-9, 50))
    # print(split_list([0, 2, 4, 0, 's', 3]))
    # print(make_dict(['232', 234, 'one', 4, 'e', 2422, 0]))
