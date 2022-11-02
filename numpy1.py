# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci
import math


def Puasson(la, N):
    if la < 0:
        raise ValueError("Lambda must be positive")
    numpy_arr = np.arange(N)
    lambda_arr = np.power(np.array([la]*N), numpy_arr)
    facto_arr = sci.factorial(numpy_arr)
    e = math.exp(-la)
    return lambda_arr*e/facto_arr


def Moment(arr, k=1):
    if k < 0:
        raise ValueError('"k" must be positive')
    elif k % 1:
        raise ValueError('"k" must be integer')
    elif not isinstance(arr, np.ndarray):
        raise Exception('Wrong array format')
    elem = arr*np.arange(len(arr))**k
    return np.sum(elem)


def Mean(arr):
    return Moment(arr, 1)


def Diviation(arr):
    return np.sum(arr*(np.arange(len(arr))-Moment(arr))**2)


def Plotter(arr):
    plt.plot(arr)
    plt.show()


def Test(x, answer, error=0.1):
    if abs(x - answer) <= error:
        return "cовпадает в пределах погрешности " + str(error)
    else:
        return "не cовпадает в пределах погрешности " + str(error)


if __name__ == '__main__':
    la = 5  # int(input())
    N = 10  # int(input())
    k = 2  # int(input())
    error = 0.1  # float(input())
    arr = Puasson(la, N)
    Plotter(arr)
    print("Начальный момент случайной великичны для k =",
          k, "равен", Moment(arr, k))
    print("Среднее значение равно", Mean(arr), "оно",
          Test(Mean(arr), la), "с реальным значением", la)
    print("Дисперсия случайной величины равна", Diviation(Puasson(la, N)),
          "она", Test(Diviation(arr), la), "с реальным значением", la)
