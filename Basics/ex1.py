import typing as tp


def is_even(n: int) -> bool:
    """
    На вход функции is_even подается целое число. Если число четное, то возвращается True, если нет, то False. 
    Проверить работу функции с числами -240, -17, 0, 12, 131. Если число отрицательное, печатается предупреждение.
    """
    if n % 2 == 0:
        return True
    else:
        return False


def generate_squares(min: int, MAX: int):
    """
    На вход функции generate_squares подается два целых числа min_num и max_num. 
    Функция возвращает последовательность квадратов, начиная от min_num и заканчивая max_num в виде списка.
    """
    return [a**2 for a in range(min, MAX + 1)]


def split_list(d: list):
    """
    На вход функции split_list подается неупорядоченный список целых чисел. Возвращается список с удаленными нулевыми значениями.
    """
    return [a for a in d if a != 0]


def make_dict(d: tp.List[tp.Union[str, int]]):
    """
    На вход функции make_dict подается список, состоящий из строк и чисел. На выходе формируется словарь с двумя ключами: str, num. 
    По первому ключу в словаре лежит список пар вида (строка, её длина), 
    по второму ключу в словаре лежит список всех чисел в данном списке.
    """
    st = []
    nu = []
    for a in d:
        if type(a) is str:
            st.append((a, len(a)))
        else:
            nu.append(a)
    r = {'str': st, 'num': nu}
    return r


class Vector2D:
    """
    Создать класс для двухмерного вектора Vector2D с координатами x, y. 
    Реализовать вычисление евклидовой нормы вектора методом norm. 
    Реализовать человеко-читаемое отображение методом __str__. 
    Реализовать сравнение векторов, используя магические методы 
    __lt__, __le__, __eq__, __ne__, __gt__, __ge__.
    """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x} , {self.y})'

    def __repr__(self) -> str:
        return self.__str__()

    def norm(self) -> float:
        return (self.x**2 + self.y**2)**0.5

    def __lt__(self, other: "Vector2D") -> bool:
        return self.norm() < other.norm()

    def __le__(self, other: "Vector2D") -> bool:
        return self.norm() <= other.norm()

    def __eq__(self, other: "Vector2D") -> bool:
        return self.norm() == other.norm()

    def __ne__(self, other: "Vector2D") -> bool:
        return self.norm() != other.norm()

    def __gt__(self, other: "Vector2D") -> bool:
        return self.norm() > other.norm()

    def __ge__(self, other: "Vector2D") -> bool:
        return self.norm() >= other.norm()


if __name__ == "__main__":
    # Test is_even()
    assert is_even(-240) is True
    assert is_even(-17) is False
    assert is_even(0) is True
    assert is_even(12) is True
    assert is_even(131) is False

    assert generate_squares(-1, 5) == [1, 0, 1, 4, 9, 16, 25]
    assert generate_squares(9, 5) == []
    assert generate_squares(9, 15) == [81, 100, 121, 144, 169, 196, 225]

    assert split_list([0, 4, 7, 45, 0, 'as', 8]) == [4, 7, 45, 'as', 8]
    assert split_list([4, 7, 45, 8]) == [4, 7, 45, 8]
    assert split_list([0, 4, 7, 45, 0, 0]) == [4, 7, 45]
    assert split_list([0,  0, 0]) == []

    assert make_dict(['asd', 12, 'sdf', 'asdfsgf', 504]) == \
        {'str': [('asd', 3), ('sdf', 3), ('asdfsgf', 7)], 'num': [12, 504]}
    assert make_dict([12, 504]) == {'str': [], 'num': [12, 504]}
    assert make_dict(['asd', 'sdf', 'asdfsgf']) == \
        {'str': [('asd', 3), ('sdf', 3), ('asdfsgf', 7)], 'num': []}

    assert Vector2D(3, 4).norm() == 5

    print("Tests ok")
