# Пуассон, задания, тесты. Проблема переполнения НЕ исправлена.
import numpy as np
import math
from scipy.special import factorial
import matplotlib.pyplot as plt


def poi(l, N):
    if l < 0:
        raise ValueError
    X = np.arange(N+1)
    Y = l**X/factorial(X)*math.exp(-l)
    return Y
# Пуассон от l, N точек.


def moment(Y, a):
    if (type(Y) != np.ndarray) or (type(a) != int):
        raise TypeError
    X = np.arange(Y.size)
    X = (X**a)*Y
    return np.sum(X)
# Момент от Y порядка a.


def average(Y):
    return moment(Y, 1)


def dispersion(Y):
    return moment(Y, 2)-moment(Y, 1)**2


def function_to_test(l, N, d):
    Y = poi(l, N)
    A = average(Y)
    D = dispersion(Y)
    if (A > l*(1-d)) and (A < l*(1+d)) and (D > l*(1-d)) and (D < l*(1+d)):
        return True
    else:
        return False
# Возвращает истину, если среднее и дисперсия распределения
# отклоняются от правильных с относительной погрешностью менее d.


def function_to_test_poi(l, N):
    try:
        poi(l, N)
    except ValueError:
        return True
    else:
        return False


def function_to_test_moment(Y, a):
    try:
        moment(Y, a)
    except TypeError:
        return True
    else:
        return False
# Возвращают истину, если есть нужное исключение.


# Тесты
if __name__ == '__main__':
    assert function_to_test(1, 100, 0.01) == True
    assert function_to_test(2, 100, 0.01) == True
    assert function_to_test(3, 100, 0.01) == True
    assert function_to_test(3, 1000000, 0.01) == True
    assert function_to_test(4, 100, 0.01) == True
    assert function_to_test(5, 100, 0.01) == True
    assert function_to_test(5, 6, 0.01) == False
    assert function_to_test(6, 100, 0.01) == False  # Переполнение
    assert function_to_test(6, 100, 0.1) == True
    plt.plot(poi(6, 30))
    plt.show()
    assert function_to_test_poi(14, 814) == False
    assert function_to_test_poi(-14505, 89767) == True
    assert function_to_test_moment(poi(5, 100), 2) == False
    assert function_to_test_moment(poi(5, 100), 2.164) == True
    assert function_to_test_moment("Poisson", 2) == True
