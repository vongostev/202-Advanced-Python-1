import numpy as np
import scipy.special
import matplotlib.pyplot as plt

def poisson(aver, N):
    n = np.arange(0, N)
    p = (np.power(aver, n)*np.exp(-aver))/scipy.special.factorial(n)
    if aver >= 0:
        return p
    else:
        return 0

def poisson_1(aver, N):
    p = (np.power(aver, N) * np.exp(-aver)) / scipy.special.factorial(N)
    if aver >= 0:
        return p
    else:
        return 0

def initial_moment(n, k):
    N = np.size(n)
    arr = np.arange(N)
    x = np.power(arr, k)
    y = n
    m = np.dot(y, x)
    if isinstance(k, int) == False or not(np.size(np.array(n)) > 1):
        return 0
    else:
        return m

def average(n):
    m = initial_moment(n, 1)
    return m

def dispersion(n):
    m = initial_moment(n, 2) - initial_moment(n, 1) ** 2
    return m

def test(aver, N):
    a = poisson(aver, N)
    b = average(a)
    c = dispersion(a)
    plt.plot(a)
    plt.scatter(b, poisson_1(b, b))
    plt.scatter(c, poisson_1(c, c))
    plt.show()

#test
a = poisson(3, 100)
b = average(a)
c = dispersion(a)
print('a = ', 3)
print('b = ', b)
print('c = ', c)
test(3, 100)