# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci


def Puasson(la, N):
    if la < 0:
        raise ValueError("Lambda must be positive")
    numpy_arr = np.arange(N)
    return la ** numpy_arr * np.exp(-la) / sci.factorial(numpy_arr)


def Moment(arr, k=1):
    if k < 0:
        raise ValueError('"k" must be positive')
    elif k % 1:
        raise ValueError('"k" must be integer')
    elif not isinstance(arr, np.ndarray):
        raise ValueError('Wrong array format')
    return np.sum(arr * np.arange(len(arr)) ** k)


def Mean(arr):
    return Moment(arr, 1)


def Diviation(arr):
    return Moment(arr, 2) - Moment(arr, 1) ** 2


def Plotter(arr):
    plt.plot(arr)
    plt.show()


def Test(x, answer, error=0.1):
    if abs(x - answer) <= error:
        return "cовпадает в пределах погрешности " + str(error)
    return "не cовпадает в пределах погрешности " + str(error)


if __name__ == '__main__':
    la = 10  # int(input())
    N = 20  # int(input())
    k = 2  # int(input())
    error = 0.1  # float(input())
    arr = Puasson(la, N)
    Plotter(arr)
    print("Начальный момент случайной великичны для k =",
          k, "равен", Moment(arr, k))
    print("Среднее значение равно", Mean(arr), "и",
          Test(Mean(arr), la), "с реальным значением", la)
    print("Дисперсия случайной величины равна", Diviation(Puasson(la, N)),
          "и", Test(Diviation(arr), la), "с реальным значением", la)
