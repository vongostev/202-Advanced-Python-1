import math 

def is_even(number):
    if (number < 0):
        print("Warning! Asserted value is less than 0")
    else: 
        return not(number % 2)


def generate_squares(min_num, max_num):
    return [i*i for i in range(min_num, max_num+1)]

def split_list(listing):
    return [element for element in listing if element]

def make_dict(listing):
    str_ = []
    num_ = []
    for element in listing:
        if (isinstance(element, int)):
            num_.append(element)
        else: 
            str_.append((element, len(element)))
    return {'str':  str_, 'num': num_}

class Vector2D:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y 

    def norm(self):
        return (self.x**2+self.y**2)**0.5  

    def __str__(self):
        return 'Vector2D: ({x}, {y})'.format(x=self.x, y=self.y)

    def __lt__(self, vector):
        return self.norm() < vector.norm()

    def __le__(self, vector):
        return self.norm() <= vector.norm()

    def __eq__(self, vector):
        return (self.x == vector.x) and (self.y == vector.y)

    def __ne__(self, vector):
        return not(self.__eq__(vector))

    def __gt__(self, vector):
        return self.norm() > vector.norm()

    def __ge__(self, vector):
        return  self.norm() >= vector.norm()

    def sum(self, vector):
        return Vector2D(self.x + vector.x, self.y + vector.y)

    def sub(self, vector):
        return Vector2D(self.x - vector.x, self.y - vector.y)

    def prod(self, number):
        return Vector2D(self.x * number, self.y * number)

if __name__ == '__main__':
        def is_even_test():
            #assert is_even(-240)
            #assert is_even(-17)
            assert is_even(0) == 1
            assert is_even(1) == 0
            assert is_even(13) == 0
            print('is_even works correctly')

        def generate_squares_test():
            assert generate_squares(0, 1) == [0, 1]
            assert generate_squares(-1, 2) == [1, 0, 1, 4]
            assert generate_squares(2, 2) == [4]
            assert generate_squares(-2, -5) == []
            assert generate_squares(3, 6) == [9, 16, 25, 36]
            print('generate_squares works correctly')

        def split_list_test():
            assert split_list([0]) == []
            assert split_list([-1, 1, 1, 0]) == [-1, 1, 1]
            assert split_list([-2, 0, 3]) == [-2, 3]
            assert split_list([0, 0, 1, 0, 1]) == [1, 1]
            print('split_list works correctly')

        def make_dict_test():
            assert make_dict([]) == {'str': [], 'num': []}
            assert make_dict([1, 2, 3, 4]) == {'str': [], 'num': [1, 2, 3, 4]}
            assert make_dict(['1', 1, '2', 2, '3', 3, '4', -4]) == {'str': [('1', 1), ('2', 1), ('3', 1), ('4', 1)], 'num': [1, 2, 3, -4]}
            print('make_dict works correctly')

        def vector2D_test():
            zero = Vector2D()
            first = Vector2D(-1, 4)
            second = Vector2D(80, -60)
            assert second.norm() == 100
            assert (first == zero) == False
            assert (first == first) == True
            assert (first < second) == True
            assert (first > second) == False
            assert (first >= second) == False
            assert (first <= second) == True
            print('Vector2D works correctly')

        is_even_test()
        generate_squares_test()
        split_list_test()
        make_dict_test()
        vector2D_test()