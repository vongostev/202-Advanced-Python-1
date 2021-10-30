import numpy as np
import matplotlib.pyplot as plt
import scipy.special


def poisson(lambda_, n):
    assert lambda_ >= 0, '"Лямбда не должно быть меньше 0"'
    a = np.arange(n)
    b = lambda_ ** a * np.exp(-lambda_) / scipy.special.factorial(a)
    return a, b

def average(a, b):
    return moment(a, b, 1)

def dispersion(a, b):
    return average((a - average(a, b)) ** 2, b)

def moment(a, b, k):
    assert isinstance(k, int), 'k не int'
    assert isinstance(a, np.ndarray)
    assert isinstance(b, np.ndarray)
    return (a ** k * b).sum()

lambda_ = 4
k = 2

n = 50
a, b = poisson(lambda_, n)

plt.plot(a, b)
plt.show()

print(moment(a, b, k))
print(average(a, b))
print(dispersion(a, b))

assert np.allclose([average(a, b), dispersion(a, b)], [lambda_, lambda_], 1e-3)
