import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.special as SCS

def Poisson(Lambda, N):
    assert Lambda >= 0
    x = np.arange(0, N)
    y = Lambda ** x * np.exp(-Lambda) / SCS.factorial(x)
    return np.array([x, y])


def Moment(my_array, k):
    assert isinstance(k, int)
    assert isinstance(my_array, np.ndarray)
    return (my_array[0] ** k * my_array[1]).sum()



def Average(my_array):
    return Moment(my_array, 1)



def Dispersion(my_array):
    my_array[0] = (my_array[0] - Average(my_array)) ** 2
    return Average(my_array)
    


if __name__ == '__main__':
    Lambda = 4
    my_array = Poisson(Lambda, 40)
    print(Average(my_array))
    print(Dispersion(my_array))
    plt.plot(my_array[1])
    plt.show()
