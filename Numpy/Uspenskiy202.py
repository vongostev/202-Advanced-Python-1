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


def poisson(lmbd, N):
    assert lmbd >= 0, 'Lambda should not be negative'
    x = np.arange(0, N, 0.8)
    y = lmbd ** x * math.exp(-lmbd) / scipy.special.factorial(x)
    return np.array([x, y])


def moment(array, k):
    assert isint(k), 'k is not int'
    assert isinstance(array, (list, tuple, np.ndarray))
    return np.sum(np.array(array[0] ** k * array[1]))


def average(array):
    return moment(array, 1)


def dispersion(array):
    return average((array[0] - average(array)) ** 2)


lmbd = 0.5
arr = poisson(lmbd, 10)

plt.plot(arr[0], arr[1])
print(moment(arr, 2))
print(average(arr))
print(dispersion(arr))
plt.title("Poisson distribution")
plt.show()
assert np.allclose([average(arr), dispersion(arr)], [lmbd, lmbd], 1)
