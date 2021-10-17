import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial


def poisson(lambda1, N):
    if lambda1 < 0:
        raise IOError("Лямбда меньше 0")
    n = np.arange(0, N + 1)
    p = (lambda1 ** n) * np.exp(-lambda1) / factorial(n)
    return np.array([p, n])


def moment(arr, k):
    if k < 0 or not isinstance(k, int) or not isinstance(arr, np.ndarray):
        raise IOError("Несоответствие данных на входе")
    return np.sum((arr[1] ** k) * arr[0])


def average(arr):
    if not isinstance(arr, np.ndarray):
        raise IOError("На входе НЕ массив numpy")
    return moment(arr, 1)


def dispersion(arr):
    if not isinstance(arr, np.ndarray):
        raise IOError("На входе НЕ массив numpy")
    return average(np.array([arr[0], ((arr[1] - average(arr)) ** 2)]))


if __name__ == '__main__':
    p1 = poisson(5, 1000)
    p2 = poisson(7, 1000)
    p3 = poisson(10, 1000)

    assert np.allclose(average(p1), 5, 1e-10)
    assert np.allclose(dispersion(p1), 5, 1e-10)

    assert np.allclose(average(p2), 7, 1e-4)
    assert np.allclose(dispersion(p2), 7, 1e-4)

    assert np.allclose(average(p3), 10, 1e-1)
    assert np.allclose(dispersion(p3), 10, 1e-1)

    plt.plot(p1[0], label='lambda = 5')
    plt.plot(p2[0], label='lambda = 7')
    plt.plot(p3[0], label='lambda = 10')
    plt.title('Распределение Пуассона', fontsize=18)
    plt.xlim(0, 20)
    plt.legend(fontsize=12)
    plt.show()
