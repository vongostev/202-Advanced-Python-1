# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:13:28 2021

@author: grego
"""
import numpy as np
import scipy.special as sci
import matplotlib.pyplot as plt

def distribution_poisson(lam, N):
    if lam < 0 or N < 0:
        raise ValueError
    n = np.arange(N+1)
    return (n, np.float_power(lam, n) / sci.factorial(n) * np.exp(-lam))

def initial_moment(distribution, k):
    if not isinstance(k, int) or not isinstance(distribution[0], np.ndarray) or not isinstance(distribution[1], np.ndarray):
        raise ValueError
    return np.sum(np.power(distribution[0], k) * distribution[1])

def average_value(distribution):
    return initial_moment(distribution, 1)

def dispertion(distribution):
    return average_value([(distribution[0] - average_value(distribution)) ** 2, distribution[1]])

if __name__ == '__main__':
    
    lamba = 4
    N = 130
    k = 3
    p = distribution_poisson(lamba, N)
    print('Initial moment with k = {k} :', initial_moment(p, k))
    print('Average_value :', average_value(p))
    print('Dispertion :', dispertion(p))
    print('lambda :', lamba)
    plt.plot(p[0], p[1])
    plt.show()