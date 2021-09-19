def is_even(a):
        if a < 0:
            print('(-_-)Вы ввели отрицательное число(-_-)')
        return a % 2 == 0


def generate_squares(min_num, max_num):
    ans = []
    for i in range(min_num, max_num+1):
        if i**0.5 % 1 == 0:
            ans.append(i)
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
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(x, y) = ({}, {})'.format(self.x, self.y)

    def norm(self):
        return (self.x**2 + self.y**2)**0.5

    def __lt__(self, other):
        return self.norm() < other.norm()

    def __le__(self, other):
        return self.norm() <= other.norm()

    def __eq__(self, other):
        return self.norm() == other.norm()

    def __ne__(self, other):
        return self.norm() != other.norm()

    def __gt__(self, other):
        return self.norm() > other.norm()

    def __ge__(self, other):
        return self.norm() >= other.norm()

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        self.x *= other
        self.y *= other
        return self

if __name__ == '__main__':
    q = [-240, -17, 0, 12, 131]
    a = [True, False, True, True, False]
    for i in range(len(q)):
        assert is_even(q[i] == a[i])
