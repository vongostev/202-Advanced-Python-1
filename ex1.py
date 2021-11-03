def is_even(n):
    if (n<0): print("Warning! The given number {a} is negative".format(a=n))
    return n%2 == 0
    
def generate_squares(min_num, max_num):
    return [i*i for i in range(min_num, max_num+1)]

def split_list(arr):
    return [i for i in arr if i]

def make_dict(arr):
    nums, strs = [], []
    for i in arr:
        if isinstance(i, int): nums.append(i)
        else: strs.append((i, len(i)))
    return {"str": strs, "num": nums}

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def norm(self):
        return (self.x**2 + self.y**2)**0.5
    
    def __str__(self):
        return  "({x}, {y})".format(x=self.x, y=self.y)
    
    def __lt__(self, vec):
        return self.norm() < vec.norm()
            
    def __le__(self, vec):
        return self.norm() <= vec.norm()
    
    def __eq__(self, vec):
        return self.norm() == vec.norm()
    
    def __ne__(self, vec):
        return not self.norm() == vec.norm()
    
    def __gt__(self, vec):
        return self.norm() > vec.norm()
    
    def __ge__(self, vec):
        return self.norm() >= vec.norm()

def test_is_even():
    test_arr = [-240, -17, 0, 12, 131]
    test_ans = [1, 0, 1, 1, 0]
    for i, n in enumerate(test_arr):
        assert is_even(n) == test_ans[i]
        
def test_generate_squares():
    assert generate_squares(2, 2) == [4]
    assert generate_squares(-1, 1) == [1, 0, 1]
    assert generate_squares(-3, -3) == [9]
    assert generate_squares(-1, -9) == []
    assert generate_squares(1, 4) == [1, 4, 9, 16]
    
def test_split_list():
    assert split_list([0, 0, 0]) == []
    assert split_list([0.]) == []
    assert split_list([1, -5, 6, 7]) == [1, -5, 6, 7]
    assert split_list([1, -0, 5, -2, 0, 4]) == [1, 5, -2, 4]
    
def test_make_dict():
    assert make_dict([1, 2, 3, 4]) == {"str": [], "num": [1, 2, 3, 4]}
    assert make_dict(["Hello, World!", 1, 2]) ==\
        {"str": [("Hello, World!", len("Hello, World!"))], "num": [1, 2]}
    assert make_dict([]) == {"str": [], "num": []}

def test_vector2D():
    zero = Vector2D()
    a = Vector2D(2, 1)
    b = Vector2D(3, -4)
    assert (str(zero) == '(0, 0)')
    assert (b.norm() == 5)
    assert (a == Vector2D(2, 1)) == True
    assert (a == b) == False
    assert (a < b) == True
    assert (a > b) == False
    assert (a >= b) == False
    assert (a <= b) == True
    
if __name__ == "__main__":
    test_is_even()
    test_generate_squares()
    test_split_list()
    test_make_dict()
    test_vector2D()