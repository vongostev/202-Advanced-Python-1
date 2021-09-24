# Task 1
def is_even(x):
    if x < 0:
        print(f"Warning! Number {x} is negative")
    return bool(not x % 2)


def test_Task1():
    assert is_even(-240)
    assert not is_even(-17)
    assert is_even(0)
    assert is_even(12)
    assert not is_even(131)
    print("Task1 is correct")


# Task2
def generate_squares(min_num, max_num):
    return [i**2 for i in range(min_num, max_num+1)]


def test_Task2():
    assert generate_squares(0, 0) == [0]
    assert generate_squares(1, 5) == [1, 4, 9, 16, 25]
    assert generate_squares(-3, 3) == [9, 4, 1, 0, 1, 4, 9]
    assert generate_squares(5, 4) == []
    assert generate_squares(-5, -3) == [25, 16, 9]
    print("Task2 is correct")



# Task3
def split_list(l):
    return [i for i in l if i != 0]


def test_Task3():
    assert split_list([0]) == []
    assert split_list([0, 1, 2, 3]) == [1, 2, 3]
    assert split_list([1, 0, 23, 85, 0, 0, 74]) == [1, 23, 85, 74]
    assert split_list([0, 0, 1, 0]) == []
    assert split_list([]) == []
    print("Task3 is correct")



# Task4
def make_dict(l):
    str_list = [(i, len(i)) for i in l if isinstance(i, str)]
    num_list = [i for i in l if isinstance(i, int) or isinstance(i, float)]
    return {'str': str_list, 'num': num_list}


def test_Task4():
    assert make_dict([]) == {'str': [], 'num': []}
    assert make_dict([1, 2, 3, '1', '2', '3']) == {
        'str': [1, 2, 3], 'num': ['1', '2', '3']}
    assert make_dict(['to', 'be', 'or', 'not', 'to', 'be']) == {
        'str': ['to', 'be', 'or', 'not', 'to', 'be'], 'num': []}
    print("Task4 is correct")



# Task5
class Vector2D:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x**2+self.y**2)**0.5

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __lt__(self, other):
        return self.norm() < other.norm()

    def __le__(self, other):
        return self.norm() <= other.norm()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __gt__(self, other):
        return self.norm() > other.norm()

    def __ge__(self, other):
        return self.norm() >= other.norm()

# Task6
    def __add__(self, other):
        return Vector2D(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector2D(self.x-other.x, self.y-other.y)

    def __mul__(self, number):
        return Vector2D(self.x*number, self.y*number)

    def __rmul__(self, number):
        return Vector2D(self.x*number, self.y*number)


def test_Task5_Task6():
    vector_0 = Vector2D()
    vector_1 = Vector2D(1, 2)
    vector_2 = Vector2D(3, -4)
    vector_3 = Vector2D(1, 2)

    assert vector_2.norm() == 5
    assert vector_0.norm() == 0
    assert vector_1 == vector_3
    assert vector_2 > vector_3
    assert vector_2 >= vector_1
    assert vector_0 <= vector_1
    assert vector_0 < vector_3
    assert vector_0 != vector_2
    assert str(vector_1) == "(1, 2)"
    assert str(vector_2) == "(3, -4)"
    print("Task5 is correct")

    assert vector_1 + vector_2 == Vector2D(4, -2)
    assert vector_1 - vector_2 == Vector2D(-2, 6)
    assert vector_1 * 3 == Vector2D(3, 6)
    assert 2 * vector_2 == Vector2D(6, -8)
    print("Task6 is correct")


if __name__ == '__main__':
    test_Task1()
    test_Task2()
    test_Task3()
    test_Task4()
    test_Task5_Task6()
