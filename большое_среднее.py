# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext


getcontext().prec = 10


"""@np.vectorize
def np_decimal(n):
    np_dec = np.asarray([Decimal(y) for y in n])
    return np_dec"""


def factorial(n):
    pr = Decimal('1')
    fact = np.array([1])
    for x in n[1:]:
        pr *= x
        fact = np.append(fact, pr)
    return fact


def poisson(l, N):
    if l < 0:
        raise Exception('l>0')
    n_float = np.arange(0, N+1, dtype='float64')
    n = np.asarray([Decimal(x) for x in n_float])
    l_decimal = Decimal(l)
    p = (l**n)*((-l_decimal).exp())/factorial(n)
    return p


def inital_moment(n, p, k):
    if isinstance(n, np.ndarray) and isinstance(k, int) and isinstance(p, np.ndarray):
        n_decimal = np.asarray([Decimal(x) for x in n])
        n_k = np.sum((n_decimal**k)*p)
        return n_k
    else:
        raise Exception('n, p - np.array and k - int')


def mean(n, p):
    l = inital_moment(n, p, 1)
    return l


def dispersion(n, p):
    l = mean(n, p)
    n_decimal = np.asarray([Decimal(x) for x in n])
    diff = (n_decimal-l)**2
    disp = inital_moment(diff, p, 1)
    return disp


if __name__ == '__main__':
    p2 = poisson(20, 1000)[:126]
    p4 = poisson(40, 1000)[:126]
    p10 = poisson(100, 1000)[:126]
    plt.grid(which='major',
             color='k')
    plt.minorticks_on()
    plt.grid(which='minor',
             color='gray',
             linestyle=':')
    plt.plot(p2, label='l=20')
    plt.plot(p4, label='l=40')
    plt.plot(p10, label='l=100')
    plt.xlabel('Значение случайной величины', fontsize=14)
    plt.ylabel('Вероятность', fontsize=14)
    plt.legend()
    plt.show()
    n, l = int(input()), int(input())
    p = poisson(l, n)
    n_np = np.arange(0, n+1, dtype='float64')
    n_2 = inital_moment(n_np, p, 2)
    n_mean = mean(n_np, p)
    disp = dispersion(n_np, p)
    print(f"Начальный момент 2-го порядка {n_2:.2g}")
    print(f"Среднее значение - {n_mean:.2g}")
    print(f"Дисперсия - {disp:.2g}")
