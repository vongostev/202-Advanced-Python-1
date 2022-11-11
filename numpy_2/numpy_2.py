# Пуассон, задания, тесты. Decimal.
import decimal
import numpy as np
import matplotlib.pyplot as plt


@np.vectorize
def int2d(x):
    y = float(x)
    return decimal.Decimal(y)
# int --> Decimal


@np.vectorize
def power(x, l):
    return decimal.Context().power(l, x)
# Decimal x Decimal --> Decimal


@np.vectorize
def factorial(x):
    if x == 0:
        return decimal.Decimal(1)
    else:
        k = decimal.Decimal(1)
        for i in range(1, x+1, 1):
            k = k*decimal.Decimal(i)
        return k
# int --> Decimal


def poi(l, N):
    if l < 0:
        raise ValueError("l<0")
    X = np.arange(N+1)
    return (power(int2d(X), decimal.Decimal(l))/factorial(X))*decimal.Context().exp(-decimal.Decimal(l))
# float x int --> np.ndarray(decimal.Decimal)


def moment(Y, a):
    if type(Y) != np.ndarray:
        raise TypeError("Не массив")
    if type(a) != int:
        raise TypeError("Порядок не целый")
    X = int2d(np.arange(Y.size))
    X = power(decimal.Decimal(a), X)*Y
    return np.sum(X)
# np.ndarray(decimal.Decimal) x int --> decimal.Decimal


def average(Y):
    return moment(Y, 1)


def dispersion(Y):
    return moment(Y, 2)-moment(Y, 1)**2


def function_to_test(l, N, d):
    Y = poi(l, N)
    A = average(Y)
    D = dispersion(Y)
    if (A > decimal.Decimal(l*(1-d))) and (A < decimal.Decimal(l*(1+d))) and (D > decimal.Decimal(l*(1-d))) and (D < decimal.Decimal(l*(1+d))):
        return True
    else:
        return False
# float x int x float --> bool
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
    assert function_to_test(3, 1000, 0.01) == True
    assert function_to_test(4, 100, 0.01) == True
    assert function_to_test(5, 100, 0.01) == True
    assert function_to_test(5, 6, 0.01) == False  # Мало точек
    assert function_to_test(6, 100, 0.01) == True  # Переполнения нет !!!
    assert function_to_test(500, 1000, 0.01) == True
    plt.plot(poi(500, 1000))
    plt.show()
    assert function_to_test_poi(14, 814) == False
    assert function_to_test_poi(-14505, 89767) == True
    assert function_to_test_moment(poi(5, 100), 2) == False
    assert function_to_test_moment(poi(5, 100), 2.164) == True
    assert function_to_test_moment("Poisson", 2) == True
