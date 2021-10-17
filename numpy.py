import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.special as SCS

def Pyasson(L, N):
    if L < 0:
        print("Error L < 0")
        return None
    else:
        x = np.arange(0, N)
        #x = np.random.uniform(0, N, N)
        #x = np.random.poisson(L, N)
        #x = np.sort(x)
        y = L ** x * np.exp(-L) / SCS.factorial(x)
        #y = np.random.poisson(L, N)
        #y = np.sort(y)
        return np.array([x, y])

def Sr(my_array, k):
    if (type(k) == int):
        if (type(my_array) == np.ndarray):
            return (my_array[0] ** k * my_array[1]).sum()
        else:
            print("Error my_array != massive")
            return None
    else:
        print("Error k != int")
        return None
def Sr_n(my_array):
    return Sr(my_array, 1)
def Dispers(my_array):
    my_array[0] = (my_array[0] - Sr_n(my_array)) ** 2
    return Sr_n(my_array)
    

L = 4
my_array = Pyasson(L, 40)
print(Sr_n(my_array))
print(Dispers(my_array))
plt.plot(my_array[1])
plt.show()

