# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 11:09:13 2021

@author: Егор
"""

import numpy as np

import matplotlib.pyplot as plt



def random_puasson(l, N):
    
    if (l < 0 or N < 1):
        raise ValueError
        
    n = np.arange(0, N)
    
    return (n + 1, np.cumproduct(l / (n + 1))*np.exp(-l))


def moment(arr, k):
    if (not isinstance(k, int) or not isinstance(arr, tuple) or not isinstance(arr[0], np.ndarray) or not isinstance(arr[1], np.ndarray)):
        raise ValueError
    return np.sum(arr[0]**k * arr[1])

def average(arr):
    return moment(arr, 1)


def dispersion(arr):
    return moment(((arr[0] - average(arr)), arr[1]), 2)



if __name__ == "__main__":
    
    lams = [10, 20, 30, 40, 50]
    
    arr = []
    
    for lam in lams:
        arr.append(random_puasson(lam, 75))
    
    for ar in arr:
        plt.plot(ar[1])
        
    plt.show()
    
    i = 0
    for i in range(0, len(lams)):
        print("Lammbda =", lams[i])
        print("\tAverage:\t", average(arr[i]), "-", abs(lams[i] - average(arr[i])))
        print("\tDispersion:\t", dispersion(arr[i]), "-", abs(lams[i] - dispersion(arr[i])))