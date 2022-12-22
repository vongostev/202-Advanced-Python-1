import numpy as np
import scipy.special as s
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

getcontext().prec = 8

def toDecimalArray(arr):
    return np.asarray([Decimal(x) for x in arr])

def Poisson(L_, n):
    if L_ < 0:
        raise Exception('L must be non-negative')
    L = Decimal(L_)
    L_pow = toDecimalArray(np.power(L, n))
    # print(L_pow)
    n_fact = toDecimalArray(s.factorial(np.array(n, dtype=np.int64)))
    # print(n_fact)
    exp_pow = Decimal(-L).exp()
    # print(exp_pow)
    P = (L_pow * exp_pow) / n_fact
    return P

def Initial_moment(L, k, n, p):
    if type(n) is  not np.ndarray or type(k) is  not int:
        raise Exception('n must be array and k must be int')
    nk = np.sum(toDecimalArray(np.power(n, k)) * p)
    return Decimal(nk)

def Average(L, n, p):
    average = Initial_moment(L, 1, n, p)
    return Decimal(average)

def Variance(L, n, p):
    element = n - Average(L, n, p)
    variance = Initial_moment(L, 2, element, p)
    return Decimal(variance)

def Compare(x, L, error):
    if abs(x - L) < error:
        print('Values match')
    else:
        print('Values do not match')

#-------------------------------------------------------------------
print('Enter Lamda: ')
L = int(input())
print('Enter N: ')
N = int(input())
n = toDecimalArray(np.arange(0, N + 1, dtype = 'float64'))
p = toDecimalArray(Poisson(L, n))
#print(p)
print('Enter k: ')   
k = int(input())
print('Initial_moment is: ', Initial_moment(L, k, n, p))
print('Average is: ', Average(L, n, p))
print('Variance is: ', Variance(L, n, p))
#print(np.allclose(Average(L, n, p), L ))
#print(np.allclose(Variance(L, n, p), L))
Compare(Average(L, n, p), L, 0.001)
Compare(Variance(L, n, p), L, 0.001)

plt.plot(Poisson(1, n))
plt.plot(Poisson(4, n))
plt.plot(Poisson(10, n))
plt.plot(Poisson(50, n))
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.grid(True)
plt.show()
#print(np.allclose(Average(L, n, p), L ))
#print(np.allclose(Variance(L, n, p), L))




