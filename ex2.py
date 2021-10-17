import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial


def Puasson(lambda1, N):
    if lambda1 < 0:
        raise IOError("Лямбда меньше 0")
    n = np.arange(0, N + 1)
    p = (lambda1 ** n) * (np.exp(1) ** (-lambda1)) / factorial(n)
    return np.array([p, n])


def Moment(arr, k):
    if k < 0 or not isinstance(k, int) or not isinstance(arr, np.ndarray):
        raise IOError("Несоответствие данных на входе")
    return np.sum((arr[1] ** k) * arr[0])


def Average(arr):
    if not isinstance(arr, np.ndarray):
        raise IOError("На входе НЕ массив numpy")
    return Moment(arr, 1)


def Dispersion(arr):
    if not isinstance(arr, np.ndarray):
        raise IOError("На входе НЕ массив numpy")
    arr[1] = ((arr[1] - Average(arr)) ** 2)
    return Average(arr)


if __name__ == '__main__':
    p1 = Puasson(5, 1000)
    p2 = Puasson(7, 1000)
    p3 = Puasson(10, 1000)

    assert np.allclose(Average(p1), 5, 1e-10)
    assert np.allclose(Dispersion(p1), 5, 1e-10)

    assert np.allclose(Average(p2), 7, 1e-4)
    assert np.allclose(Dispersion(p2), 7, 1e-4)

    assert np.allclose(Average(p3), 10, 1e-1)
    assert np.allclose(Dispersion(p3), 10, 1e-1)

    plt.plot(p1[0], label='lambda = 5')
    plt.plot(p2[0], label='lambda = 7')
    plt.plot(p3[0], label='lambda = 10')
    plt.title('Распределение Пуассона', fontsize=18)
    plt.xlim(0, 20)
    plt.legend(fontsize=12)
    plt.show()
