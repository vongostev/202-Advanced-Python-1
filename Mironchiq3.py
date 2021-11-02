import matplotlib.pyplot as plt
import numpy as np
import scipy.special as SCS

def Puass(L, N):
    if L < 0:
        print("Error L < 0")
        return None
    else:
        x = np.arange(0, N)
        y = L ** x * np.exp(-L) / SCS.factorial(x)
        return np.array([x, y])

def Sr(my_array, d):
    if (type(d) == int):
        if (type(my_array) == np.ndarray):
            return (my_array[0] ** d * my_array[1]).sum()
        else:
            print("Error my_array != massive")
            return None
    else:
        print("Error d != int")
        return None
def Sr_n(my_array):
    return Sr(my_array, 1)
def Dispers(my_array):
    my_array[0] = (my_array[0] - Sr_n(my_array)) ** 2
    return Sr_n(my_array)


L = 4
my_array = Puass(L, 40)
print(Sr_n(my_array))
print(Dispers(my_array))
plt.plot(my_array[1])
plt.show()
