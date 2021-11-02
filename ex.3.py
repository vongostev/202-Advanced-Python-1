# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:13:28 2021

@author: grego
"""
import numpy as np

def function_poisson(lam, n):
    return lam ** n / np.math.factorial(n) * np.exp ** (-lam)

def poisson(lam, N):
    return np.fromfunction(function_poisson, (lam, N))

pois = poisson(4, 5)
    
print(np.ones(5))
    