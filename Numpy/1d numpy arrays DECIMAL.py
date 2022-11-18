from decimal import Decimal, getcontext

import numpy as np
import math
import scipy.special
import matplotlib.pyplot as plt


# Векторизованное преобразование
@np.vectorize
def float2decimal(x):
    return Decimal(x)


# Распределение Пуассона
def poisson_distribution(lambda_, N):
    if lambda_ <= 0:
        raise Exception("Incorrect lambda value")
    if N < 0:
        raise Exception("Incorrect N value")

    N = np.int64(N)  # введено для корректной работы дисперсии
    m = np.arange(N+1, dtype=float)
    P = float2decimal(pow(lambda_, m))*Decimal(math.exp(-lambda_)) / \
        float2decimal(scipy.special.factorial(np.arange(N+1)))
    return P


# Момент случайной величины
def moment_of_rv(P, k):
    if type(k) != int:
        raise Exception("Incorrect k type")
    if type(P) != np.ndarray and type(P) != np.array:
        raise Exception("Incorrect P type")

    P = P/P.sum()  # нормировка вероятности
    n = float2decimal(pow(np.arange(P.size, dtype=float), k))*P
    return n.sum()


# Среднее значение случайной величины
def mean_value(P):
    return moment_of_rv(P, 1)


# Дисперсия случайной величины
def dispersion(P):
    return moment_of_rv(poisson_distribution(lambda_, \
                                             P.size-1-mean_value(P)), 2)


if __name__ == '__main__':
    # lambda_ = float(input("Введите значение lambda: "))
    # N = int(input("Введите значение N: "))
    lambda_ = 4
    N = 20
    getcontext().prec = 6

    P = poisson_distribution(lambda_, N)
    plt.plot(P)
    plt.show()
    # print(P)
    print("Mean value =", mean_value(P))
    print("Dispersion =", dispersion(P))
