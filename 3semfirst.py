def is_even(n):
    if n < 0:
        print('is_even: n < 0 \n')
    return bool((n + 1) % 2)


def generate_squares(min_num, max_num):
    return [it**2 for it in range(min_num, max_num + 1)]


def split_list(lt):
    it = lt.count(0)
    for ii in range(it):
        lt.remove(0)
    return lt


def make_dict(lt):
    st = []
    nu = []
    for it in lt:
        if type(it) == str:
            st.append(it)
        else:
            nu.append(it)
    d = {'str': st, 'num': nu}
    return d


class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x ** 2 + self.y ** 2)**0.5

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x**2 + self.y**2 > other.x**2 + other.y**2

    def __lt__(self, other):
        return self.x**2 + self.y**2 < other.x**2 + other.y**2

    def __ge__(self, other):
        return self.x**2 + self.y**2 >= other.x**2 + other.y**2

    def __le__(self, other):
        self.x**2 + self.y**2 <= other.x**2 + other.y**2

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, *args):
        if len(args) != 1:
            raise ValueError('there are '+str(len(args))+'in multiplication')

        if isinstance(args[0], int):
            return (self.x * args[0], self.y * args[0])
        elif isinstance(args[0], float):
            self.x *= float(args[0])
            self.y *= float(args[0])
            return (self.x, self.y)
        elif isinstance(args[0], Vector2D):
            return (self.x * args[0].x + self.y * args[0].y)
        else:
            raise ValueError('unknown type')


a = Vector2D(2, 3)

b = Vector2D(4, 4)

print(a, b*a)
