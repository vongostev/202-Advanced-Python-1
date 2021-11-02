# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:13:28 2021

@author: grego
"""
import numpy as np
import scipy.special as sci

def poisson(lam, N):
    if lam < 0 or N < 0:
        raise ValueError
    n = np.arange(N+1)
    return np.float_power(lam, n) / sci.factorial(n) * np.exp(-lam)

# def 
print(poisson(-0.5, 4))
# np.array()
# np.