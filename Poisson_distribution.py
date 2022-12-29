# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import math
from decimal import Decimal, getcontext


getcontext().prec = 10

@np.vectorize
def decfact(x):
    return Decimal(scipy.special.factorial(int(x)))


def poisson_distribution(n, lmbd):
    if lmbd < 0:
        raise ValueError("limbda < 0")
    num = np.asarray([Decimal(i) for i in range (n)])
    arr = Decimal(lmbd) ** num
    arr = arr * Decimal(-lmbd).exp() / decfact(num)
    return arr


def initial_moment(k, arr1):
    if not isinstance(arr1, np.ndarray):
        raise ValueError("wrong type of array")
    elif not isinstance(k, int):
        raise ValueError("k must be integer")
    else:
        arr = np.arange(len(arr1))**k
        return np.sum(arr*arr1)
        
    
def diviation(arr):
    a = (initial_moment(1, arr)**2 - initial_moment(1, arr*arr))
    return np.sum(a*arr)


if __name__ == "__main__":
    print(1)
    n = int(input())
    lmbd = int(input())
    k = int(input())
    p = (poisson_distribution(n, lmbd))
    plt.plot(p)
    plt.show()
    print("initial_moment = ", initial_moment(k, p))
    print("mean = ", initial_moment(1, p))
    print("diviation = ", diviation(p))
    