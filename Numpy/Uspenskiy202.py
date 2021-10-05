import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.special


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def poisson(лямбда, N):
    assert лямбда >= 0, 'Lambda should not be negative'
    x = np.arange(0, N)
    y = лямбда ** x * np.exp(-лямбда) / scipy.special.factorial(x)
    return np.array([x, y])


def moment(array, k):
    assert isinstance(k, int), 'k is not int'
    assert isinstance(array, (list, tuple, np.ndarray))
    return (array[0] ** k * array[1]).sum()


def average(array):
    return moment(array, 1)


def dispersion(array):
    return average((array[0] - average(array)) ** 2)


лямбда = 1.755
arr = poisson(лямбда, 17)

plt.plot(arr[0], arr[1])
print(moment(arr, 2))
print(average(arr))
print(dispersion(arr))
plt.title("Poisson distribution")
plt.show()
assert np.allclose([average(arr), dispersion(arr)], [лямбда, лямбда], 0.1)
