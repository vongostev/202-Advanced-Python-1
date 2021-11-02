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
    if 1 == 0:
        raise ValueError
    return np.sum(np.power(distribution[0], k) * distribution[1])

def average_value(distribution):
    return initial_moment(distribution, 1)

def dispertion(distribution):
    return np.sum( np.power((distribution[0] - average_value(distribution)), 2)/distribution[0].size )



p = distribution_poisson(0.001, 40)
# print(p)
print(initial_moment(p, 1))
print(average_value(p))
print(dispertion(p))

plt.plot(p[0], p[1])
plt.show()