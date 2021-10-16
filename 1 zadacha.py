import math

def is_even(x):
    if (x < 0):
        print("Number < 0")
    return x % 2 == 0

def generate_squares(min_num, max_num):
    a = list()
    for i in range(min_num, max_num + 1, 1):
        a.append(i * i)
    print(a)
    return a

def split_list(my_list):
    try:
        for i in range(len(my_list)):
            my_list.remove(0)
    except ValueError:
        return my_list
    return []
def make_dict(l):
    my_dictionary = {"str": [], "num": []}
    for elem in l:
        if type(elem) == str:
            my_dictionary["str"].append((elem, len(elem)))
        else:
            my_dictionary["num"].append(elem)
    return my_dictionary
    
class Vector2D():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def norm(self):
        n = math.sqrt(self.x * self.x + self.y * self.y)
        return n
    def __str__(self):
        return ('(' + str(self.x) + ', ' + str(self.y) + ')')
    def __lt__(self, other):
        return self.norm() < other.norm()
    def __gt__(self, other):
        return self.norm() > other.norm()
    def __ge__(self, other):
        return self.norm() >= other.norm()
    def __le__(self, other):
        return self.norm() <= other.norm()
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __ne__(self, other):
        return not self.__eq__(other)
    
if __name__ == '__main__':

    def test_is_even():
        assert is_even(0)
        assert is_even(12)
        assert not is_even(131)
        assert is_even(-240)
        assert not is_even(-17)
        print('is_even correct')

    def test_generate_squares():
        assert generate_squares(0, 1) == [0, 1]
        assert generate_squares(-1, 1) == [1, 0, 1]
        assert generate_squares(-5, -5) == [25]
        assert generate_squares(5, 4) == []
        assert generate_squares(0, 4) == [0, 1, 4, 9, 16]
        print('generate_squares correct')

    def test_split_list():
        assert split_list([0]) == []
        assert split_list([0, 0, 0]) == []
        assert split_list([-1, 1, 1]) == [-1, 1, 1]
        assert split_list([-1, 0, 1]) == [-1, 1]
        assert split_list([1, 0, 0, 0, 0]) == [1]
        print('split_list correct')

    def test_make_dict():
        assert make_dict([1, 2, 3, 4]) == {'str': [], 'num': [1, 2, 3, 4]}
        assert make_dict([]) == {'str': [], 'num': []}
        assert make_dict(['1', 1, '22', 22, '333', 333, '4444', 4444]) == {'str': [
            ('1', 1), ('22', 2), ('333', 3), ('4444', 4)], 'num': [1, 22, 333, 4444]}
        print('make_dict correct')

    def test_vector2D():
        zero_vector = Vector2D()
        first = Vector2D(1, 1)
        second = Vector2D(-3, 4)
        assert str(zero_vector) == '(0, 0)'
        assert second.norm() == 5
        assert (first == Vector2D(1, 1))
        assert (first == second) == False
        assert (first < second)
        assert (first > Vector2D(-1, 0))
        assert (first >= Vector2D(1, 1))
        assert (first <= Vector2D(3, 4))
        print('Vector2D correct')
    test_is_even()
    test_generate_squares()
    test_split_list()
    test_make_dict()
    test_vector2D()
        
