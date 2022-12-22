import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sci
import math
from decimal import Decimal, getcontext

getcontext().prec = 10


def p(n, la):
    if la < 0:
        raise ValueError("lambda < 0")
    nrange = np.arange(0, n)
    return la**nrange * math.exp(-la) / sci.factorial(nrange)


def m(k, puasson):
    if not(isinstance(puasson, np.ndarray) and isinstance(k, int)):
        raise TypeError("Wrong type")
    arr = np.arange(len(puasson))**k
    return np.sum(arr*puasson)


def sigma(poisson):
    return m(2, poisson) - m(1, poisson) ** 2

@np.vectorize
def dec_factorial(x):
    return Decimal(sci.factorial(x))


def dec_p(n, la):
    if la < 0:
        raise ValueError("lambda < 0")
    arr_fl = np.arange(n, dtype="float64")
    arr_dec = np.asarray([Decimal(x) for x in arr_fl])
    l = Decimal(la)
    return (l**arr_dec)*((-l).exp())/dec_factorial(arr_fl)


def dec_m(k, poisson):
    if not(isinstance(poisson, np.ndarray) and isinstance(k, int)):
        raise ValueError("Wrong type")
    arr_fl = np.arange(len(poisson), dtype="float64")
    arr_dec = np.asarray([Decimal(x) for x in arr_fl])
    return np.sum((arr_dec**k)*poisson)


def dec_sigma(poisson):
    return dec_m(2, poisson) - dec_m(1, poisson) ** 2


def test(n, la, s):
    dec_poisson = dec_p(n, la)
    poisson = p(n, la)
    dec_sr = dec_m(1, dec_poisson)
    dec_std = dec_sigma(dec_poisson)
    sr = m(1, poisson)
    std = sigma(poisson)
    if abs(sr-la) < la*s and abs(std - la) < la*s:
        print(f'Poisson({n},{la}): True')
    else:
        print(f'Poisson({n},{la}): False')
    if abs(dec_sr-la) < la*s and abs(dec_std - la) < la*s:
        print(f'Dec_Poisson({n},{la}): True')
    else:
        print(f'Dec_Poisson({n},{la}): False')
    plt.plot(dec_poisson[:100], label = 'Dec_P(n)')
    plt.plot(poisson[:100], label = "P(n)")
    plt.legend()

if __name__ == "__main__":
    for i in range(1, 20, 4):
        test(100, i, 0.01)
