import numpy as np
import math
import scipy.special
import matplotlib.pyplot as plt


# Распределение Пуассона
def poisson_distribution(lambda_, N):
    if lambda_ <= 0:
        raise Exception("Incorrect lambda value")
    if N < 0:
        raise Exception("Incorrect N value")

    N = np.int64(N)  # введено для корректной работы дисперсии
    m = np.arange(N+1, dtype=np.float128)
    P = pow(lambda_, m)*math.exp(-lambda_) / \
        scipy.special.factorial(np.arange(N+1))
    return P


# Момент случайной величины
def moment_of_rv(P, k):
    if type(k) != int:
        raise Exception("Incorrect k type")
    if type(P) != np.ndarray and type(P) != np.array:
        raise Exception("Incorrect P type")

    P = P/P.sum()  # нормировка вероятности
    n = pow(np.arange(P.size, dtype=np.int64), k)*P
    return n.sum()


# Среднее значение случайной величины
def mean_value(P):
    return moment_of_rv(P, 1)


# Дисперсия случайной величины
def dispersion(P):
    return moment_of_rv(poisson_distribution(lambda_, \
                                             P.size-1-mean_value(P)), 2)


if __name__ == '__main__':
    lambda_ = float(input("Введите значение lambda: "))
    N = int(input("Введите значение N: "))
    # lambda_ = 200
    # N = 2000

    P = poisson_distribution(lambda_, N)
    plt.plot(P)
    plt.show()
    # print(P)
    print("Mean value =", mean_value(P))
    print("Dispersion =", dispersion(P))
