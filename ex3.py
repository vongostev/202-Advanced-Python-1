# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:07:38 2021

@author: OGL (Egor Liakhov)
"""

import numpy as np
import scipy.special as scis
import matplotlib.pyplot as plt

def poison_dist(alpha, N):
    if alpha < 0 or N < 0: raise ValueError
    
    arr = np.array([i for i in range(N+1)], dtype = int)
    return (arr, np.float_power(alpha, arr)/scis.factorial(arr) * np.exp(-alpha))

def initial_moment(arr, p, k):
    if not isinstance(k, int) or not isinstance(arr, np.ndarray) or not isinstance(p, np.ndarray):
            raise ValueError
            
    return np.sum(np.power(arr, k)*p)

def average(arr, p):
    return initial_moment(arr, p, 1)

def dispertion(arr, p):
    return average((arr - average(arr, p))**2, p)
    
if __name__ == '__main__':
    alpha = 6
    N = 66
    k = 3
    
    arr, p = poison_dist(alpha, N)
    print("Input data: lambda = {l}, N = {n}, k = {k}".format(l=alpha, n=N, k=k))
    print("Initial momemt (k = {k}): {x}".format(k=k, x=initial_moment(arr, p, k)))
    print("Average(arr, p) = {x}".format(x=average(arr, p)))
    print("Dispertion(arr, p) = {x}".format(x=dispertion(arr, p)))
    plt.plot(arr, p)
    plt.show()