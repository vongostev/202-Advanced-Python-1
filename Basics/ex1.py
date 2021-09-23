# Abramova Marina
# 202 гр.

# Task 1
def is_even(x):
    if x < 0:
        print("WARNING: value is negative.")
    return x % 2 == 0

# Task 2
def generate_squares(min_num, max_num):
    res = []
    for x in range(min_num, max_num + 1):
        res.append(x ** 2)
    return res

# Task 3
def split_list(inp):
    res = []
    for item in inp:
        if item != 0:
            res.append(item)
    return res

# Task 4
def make_dict(inp):
    res = {"str": [], "num": []}
    for item in inp:
        if type(item) == str:
            res["str"].append((item, len(item)))
        else:
            res["num"].append(item)
    return res
    
# Task 5
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __lt__(self, vec):
        return self.norm() < vec.norm()

    def __le__(self, vec):
        return self.norm() <= vec.norm()

    def __eq__(self, vec):
        return self.x == vec.x and self.y == vec.y

    def __ne__(self, vec):
        return self.x != vec.x or self.y != vec.y

    def __gt__(self, vec):
        return self.norm() > vec.norm()

    def __ge__(self, vec):
        return self.norm() >= vec.norm()

# Task 6
    def __add__(self, vec):
        return Vector2D(self.x + vec.x, self.y + vec.y)

    def __sub__(self, vec):
        return Vector2D(self.x - vec.x, self.y - vec.y)
        
    def __mul__(self, a):
        return Vector2D(a * self.x, a * self.y)
        
    def __rmul__(self, a):
        return Vector2D(a * self.x, a * self.y)


if __name__ == "__main__":
# Tests
    # 1
    assert is_even(-240) is True
    assert is_even(-17) is False
    assert is_even(0) is True
    assert is_even(12) is True
    assert is_even(131) is False
    print("Tests for task 1 passed")
    
    # 2
    assert generate_squares(1, 10) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert generate_squares(3, 1) == []
    assert generate_squares(786, 786) == [786 ** 2]
    assert generate_squares(-12, -8) == [144, 121, 100, 81, 64]
    assert generate_squares(-3, 1) == [9, 4, 1, 0, 1]
    print("Tests for task 2 passed")
    
    # 3
    assert split_list([1, 0, 2, 0, 3, 4, 0]) == [1, 2, 3, 4]
    assert split_list([]) == []
    assert split_list([10, 11, 14, 17]) == [10, 11, 14, 17]
    assert split_list([0, 0, 0, 0, 0]) == []
    assert split_list([0, 0, 0, 123, 0]) == [123]
    print("Tests for task 3 passed")
    
    # 4
    assert make_dict([1, 0, 2, 0, 3, 4, 0]) == {'str': [], 'num': [1, 0, 2, 0, 3, 4, 0]}
    assert make_dict([]) == {'str': [], 'num': []}
    assert make_dict(["qwe", "rtyu", "1"]) == {'str': [('qwe', 3), ('rtyu', 4), ('1', 1)], 'num': []}
    assert make_dict(["asd", "zx", "3463", 43, 54, "lkj"]) == {'str': [('asd', 3), ('zx', 2), ('3463', 4), ('lkj', 3)], 'num': [43, 54]}
    print("Tests for task 4 passed")
    
    # 5
    x = Vector2D(1, 2)
    y = Vector2D(2, 3)
    assert x.norm() == 5 ** 0.5
    assert y.norm() == 13 ** 0.5
    assert str(x) == "[1, 2]"
    assert str(y) == "[2, 3]"
    assert x < y
    assert x <= y
    assert (x == y) is False
    assert x != y
    assert (x > y) is False
    assert (x >= y) is False
    print("Tests for task 5 passed")
    
    # 6
    assert x + y == Vector2D(3, 5)
    assert y - x == Vector2D(1, 1)
    assert x * 100 == Vector2D(100, 200)
    assert 5 * y == Vector2D(10, 15)
    print("Tests for task 6 passed")
