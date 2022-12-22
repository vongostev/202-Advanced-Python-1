import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal


def exp(x):
    return x.exp()

@np.vectorize
def fact(n):
    f = Decimal('1')
    while n > Decimal('1'):
        f = f * n
        n = n - Decimal('1')
    return f

def poisson(aver, N):
    n = np.arange(N+1)
    p = ((aver**n)*exp(-aver))/fact(n)
    if aver >= 0:
        return p
    else:
        return 0

def initial_moment(n, k):
    arr = np.arange(np.size(n))
    m = n*arr*k
    if isinstance(k, int) == False or not(np.size(np.array(n)) > 1):
        return 0
    else:
        return m.sum()

def average(n):
    m = initial_moment(n, 1)
    return m

def dispersion(n):
    m = initial_moment(n, 2) - initial_moment(n, 1)**2
    return m

def test(aver, N):
    a = poisson(aver, N)
    b = average(a)
    c = dispersion(a)
    plt.plot(a)
    b1 = poisson(b, b)
    plt.scatter(b, b1[np.size(b1)-1])
    plt.show()

#test
a = poisson(Decimal('3'), Decimal('100'))
b = average(a)
c = dispersion(a)
print('a = ', Decimal('3'))
print('b = ', b)
print('c = ', c)
test(Decimal('3'), Decimal('100'))