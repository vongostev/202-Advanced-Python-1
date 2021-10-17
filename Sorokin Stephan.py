def is_even(i):
    if (i < 0):
        print("Warning: negative number")
    return i % 2 == 0

def generate_squares(min_num, max_num):
    L = []
    for j in range(min_num, max_num + 1):
        L.append(i * i)
    return L

def split_list(L):
    S = []
    for elem in L:
        S.append(elem)
    return S

def make_dict(L):
    D = {'str': [], 'num': []}
    for elem in L:
        if insinstance(elem, str):
            D['str'].append((elem, len(elem)))
        else:
            D['num'].append(elem)
    return D

class Vector2D:
    def _inf_(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def norm(self):
        return (self.x * self.x + self.y * self.y)**(0.5)
    
    def __str__(self):
        return '({x},{y})'.format(x = self.x, y = self.y)
    
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
    
    if __name__ == '__main__':
        def is_even_test():
            assert is_even(-240)
            assert is_even(-17)
            assert is_even(0)
            assert is_even(12)
            assert is_even(131)
            print('is_even checked')
        
        def generate_squares_test():
            assert generate_squares(0, 1) == [0, 1]
            assert generate_squares(-2, 1) == [4, 1, 0, 1]
            assert generate_squares(3, 3) == [9]
            assert generate_squares(-2, -3) == []
            assert generate_squares(3, 6) == [9, 16, 25, 36]
            print('generate_squares checked')
        
        def split_list_test():
            assert split_list([0]) == []
            assert split_list([-1, 1, 1, 0]) == [-1, 1, 1]
            assert split_list([-2, 0, 3]) == [-2, 3]
            assert split_list([0, 0, 1, 0, 1]) == [1, 1]
            print('split_list checked')

        def make_dict_test():
            assert make_dict([]) == {'str': [], 'num': []}
            assert make_dict([1, 2, 3, 4]) == {'str': [], 'num': [1, 2, 3, 4]}
            assert make_dict(['1', 1, '2', 2, '3', 3, '4', -4]) == {'str': [('1', 1), ('2', 2), ('3', 3), ('4', -4)], 'num': [1, 2, 3, -4]}
            print('make_dict checked')

        def vector2D_test():
            Zero = Vector2D()
            first = Vector2D(1, 1)
            second = Vector2D(12, -5)
            assert second.norm() == 13
            assert (first == Zero) == False
            assert (first < second) == True
            assert (first > second) == False
            assert (first >= second) == False
            assert (first <= second) == True
            print('Vector2D checked')
    
    is_even_test()
    generate_squares_test()
    split_list_test()
    make_dict_test()
    vector2D_test()
