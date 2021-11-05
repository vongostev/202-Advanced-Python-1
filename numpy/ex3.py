# Grigoriev Semyon
import numpy
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial


def distribution(lmbda, N):
    if lmbda < 0 or N < 0:
        raise ValueError
    n = np.arange(0, N + 1)
    with numpy.errstate(all='ignore'):
        p = np.nan_to_num((pow(lmbda, n)) * np.exp(-lmbda) / factorial(n))
    return np.array([p, n], dtype='float128')

def moment(distribution, k):
    if not isinstance(distribution, np.ndarray) or not isinstance(k, int):
        raise ValueError
    return np.sum((distribution[1] ** k) * distribution[0])


def mean(distribution):
    if not isinstance(distribution, np.ndarray):
        raise ValueError
    return moment(distribution, 1)


def variabiblity(distribution):
    if not isinstance(distribution, np.ndarray):
        raise ValueError
    return mean(np.array([distribution[0], ((distribution[1] - mean(distribution)) ** 2)]))


if __name__ == '__main__':
    d1 = distribution(float(4), 1000)
    d2 = distribution(float(7), 1000)
    d3 = distribution(float(10), 1000)
    d0 = distribution(float(2), 1000)

    # Tests
    assert np.allclose(mean(d0), 2, 1e-16)
    assert np.allclose(variabiblity(d0), 2, 1e-16)

    assert np.allclose(mean(d1), 4, 1e-10)
    assert np.allclose(variabiblity(d1), 4, 1e-10)

    assert np.allclose(mean(d2), 7, 1e-4)
    assert np.allclose(variabiblity(d2), 7, 1e-4)

    assert np.allclose(mean(d3), 10, 1e-1)
    assert np.allclose(variabiblity(d3), 10, 1e-1)

plt.plot(d0[0], label='λ = 2')
plt.plot(d1[0], label='λ = 4')
plt.plot(d2[0], label='λ = 7')
plt.plot(d3[0], label='λ = 10')
plt.title('Распределения Пуассона для разных λ', fontsize=14)
plt.xlim(0, 19)
plt.legend(fontsize=14)
plt.show()
