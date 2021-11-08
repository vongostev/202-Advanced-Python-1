import numpy as np
import math as m 
import matplotlib.pyplot as plt
from scipy.special import factorial


def poission_distribution(l, N):
    if (l < 0):
        raise ValueError('lambda is less than 0')
    if (N<0):
        raise ValueError('N is less than 0')
    index = np.arange(N+1)
    return np.array([np.float_power(l, index) * np.exp(-l) / factorial(index)])

def momentum(distribution, order):
    if (not isinstance(order, int)):
        raise ValueError('order of momentum is not an integer')
    if  (not isinstance(distribution, np.ndarray)):
        raise ValueError('distribution is not a ndarray')
    index = np.arange(distribution.size)
    return sum(np.float_power(index, order) * distribution[0])

def mean(distribution):
    return momentum(distribution, 1)

def dispersion(distribution):
    return momentum(distribution, 2) - (momentum(distribution, 1))**2



if __name__ == '__main__':

    for lbd in np.arange(2, 123, step=20): 
        for N in np.arange(lbd, 151, step=10):
            distr = poission_distribution(lbd, N)
            print(f'lambda = {lbd}, N = {N}, mean = {mean(distr)}, dispersion = {dispersion(distr)}')

    try:
        poission_distribution(-5, 10)
    except ValueError:
        print('lambda must be positive')
    try:
        momentum(5, 5)
    except ValueError:
        print('distribution must be np.ndarray')
    try:
        momentum(poission_distribution(5, 100), 1.5)
    except ValueError:
        print('moment power must be integer')
