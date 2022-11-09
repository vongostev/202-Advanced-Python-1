# -*- coding: utf-8 -*-
import numpy as np
import scipy.special
import matplotlib.pyplot as plt


def poisson(l, N):
    if l < 0:
        raise Exception('l>0')
    n = np.arange(0, N+1)
    p = np.power(l, n)*np.exp(-l)/scipy.special.factorial(n)
    return p


def inital_moment(n, p, k):
    if isinstance(n, np.ndarray) and isinstance(k, int) and isinstance(p, np.ndarray):
        n_k = np.sum((n**k)*p)
        return n_k
    else:
        raise Exception('n_p - np.array and k - int')


def mean(n, p):
    l = inital_moment(n, p, 1)
    return l


def dispersion(n, p):
    l = mean(n, p)
    diff = (n-l)**2
    disp = inital_moment(diff, p, 1)
    return disp


def test(x, x_ans, err):
    if abs(x_ans - x) <= err:
        print(
            f"{x:.3g} совпадает с реальным значением {x_ans:.3g} в пределах погрешности.")
    else:
        print(
            f"{x:.3g} не совпадает с реальным значением {x_ans:.3g} в пределах погрешности.")


if __name__ == '__main__':
    p2 = poisson(2, 1000)[:11]
    p4 = poisson(4, 1000)[:11]
    p10 = poisson(10, 1000)[:11]
    plt.grid(which='major',
             color='k')
    plt.minorticks_on()
    plt.grid(which='minor',
             color='gray',
             linestyle=':')
    plt.plot(p2, label='l=2')
    plt.plot(p4, label='l=4')
    plt.plot(p10, label='l=10')
    plt.xlabel('Значение случайной величины', fontsize=14)
    plt.ylabel('Вероятность', fontsize=14)
    plt.legend()
    plt.show()
    l = int(input("Введите значение среднего случайно величины: "))
    n = int(input("Введите максимальное значение случайной величины: "))
    p = poisson(l, n)
    n_row = np.arange(0, n+1)
    l2 = inital_moment(n_row, p, 2)
    l_mean = mean(n_row, p)
    d = dispersion(n_row, p)
    print(f"Начальный момент 2-го порядка - {l2:.3g}")
    print(f"Среднее значение - {l_mean:.3g}")
    print(f"Дисперсия - {d:.3g}")
    err = float(input("Введите точность сравнения: "))
    test(l_mean, l, err)
    test(d, l, err)
