def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


def generate_squares(min_num, max_num):
    a = [k**2 for k in range(min_num, max_num+1)]
    return a


def split_lis(a):
    a = list(filter(lambda x: x != 0, a))
    return a


def make_dist(a):
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
        return self.norm() == other.norm()

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __gt__(self, other):
        return self.norm() > other.norm()

    def __ge__(self, other):
        return self.norm() >= other.norm()

if __name__ == '__main__':

    print('test for 1 ex:')
    mas = [-240, -17, 0, 12, 131]
    for i in range(len(mas)):
#   assert mas[i] > 0, "a must be non-negative"
        print(is_even(mas[i]))

    print('test for 2 ex:')
    print(generate_squares(1, 4))

    print('test for 3 ex:')
    print(split_lis([0, 1, 2, 0, 4, 0, 0, 5, 0]))

    print('test for 4 ex:')
    print(make_dist(['samaya', 2, 5, 6, 'obichniya', 4, 'muzika']))

    print('rest for 5 ex:')
    v1 = Vector2D(5, 5)
    v2 = Vector2D(4, 3)
    print(v1)
    print(Vector2D.norm(v1))
    print(Vector2D.__str__(v1))
    print(Vector2D.__eq__(v1, v2))
    print(Vector2D.__le__(v1, v2))
#   ----------------
