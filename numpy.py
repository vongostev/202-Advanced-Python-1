import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sci

def Poisson(la, n):
    if la < 0:
        raise ValueError("invalid λ, please enter λ⩾0")
    numpy_arr = np.arange(n)
    return la ** numpy_arr * np.exp(-la) / sci.factorial(numpy_arr)

def Raw_Moment(arr, k):
    if k < 0:
        raise ValueError('invalid k, please enter k⩾0')
    elif k % 1:
        raise ValueError('invalid k, please enter integer k')
    elif not isinstance(arr, np.ndarray):
        raise ValueError('invalid array format')
    return np.sum(arr * np.arange(len(arr)) ** k)

def Mean(arr):
    return Raw_Moment(arr, 1)

def Dispersion(arr):
    return Raw_Moment(arr, 2) - Raw_Moment(arr, 1) ** 2

def Test(x, answer, error = 0.5):
    if abs(x - answer) <= error:
        return "coincides within the error " + str(error)
    return "doensn't coincide within the error " + str(error)

if __name__ == '__main__':
    print("please enter λ")
    la = float(input())
    print("please enter N")
    N = float(input())
    arr = Poisson(la, N)
    print("mean equals ", Mean(arr), "and ", Test(Mean(arr), la), "with theoretical value ", la)
    print("dispersion of a distribution equals ", Dispersion(Poisson(la, N)), "and ", Test(Dispersion(arr), la), "with theoretical value ", la)
