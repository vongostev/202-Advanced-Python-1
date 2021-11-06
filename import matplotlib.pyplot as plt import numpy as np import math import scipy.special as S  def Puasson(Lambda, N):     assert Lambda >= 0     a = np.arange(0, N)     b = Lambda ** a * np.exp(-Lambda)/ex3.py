import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.special as S

def Puasson(Lambda, N):
    assert Lambda >= 0
    a = np.arange(0, N)
    b = Lambda ** a * np.exp(-Lambda) / S.factorial(a)
    return np.array([a, b])

def Moment(array, k):
    assert isinstance(k, int)
    assert isinstance(array, np.ndarray)
    return (my_array[0] ** k * my_array[1]).sum()

def Avg(array):
    return Moment(array, 1)

def Disp(my_array):
    array[0] = (array[0] - Avg(array)) ** 2
    return Average(my_array)

if __name__ == '__main__':
    Lambda = 7
    my_array = Puasson(Lambda, 100)
    print(Average(my_array))
    print(Dispersion(my_array))
    plt.plot(my_array[1])
    plt.show()
