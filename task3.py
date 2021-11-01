#task3
import matplotlib.pyplot as plt
import numpy as np


def poisson_gen(lm, N):
    if (lm < 0 or N < 1):
        raise ValueError
    n = np.arange(0, N)
    return (n + 1, np.cumproduct(lm / (n + 1))*np.exp(-lm))


def moment(arr, k):
    if (not isinstance(k, int) or not isinstance(arr, tuple) or not isinstance(arr[0], np.ndarray) or not isinstance(arr[1], np.ndarray)):
        raise ValueError
    return np.sum(arr[0]**k * arr[1])


def average_and_dispersion(arr):
    aver = moment(arr, 1)
    return aver, moment(arr, 2) - aver ** 2


def average(arr):
    return moment(arr, 1)


def dispersion(arr):
    return moment(((arr[0] - average(arr)), arr[1]), 2)
    


if __name__ == "__main__":

    lam = [0.005, 0.15, 1, 2, 5, 6, 10, 11]
    i = 0
    arr = []

    for lm in lam:
        arr.append(poisson_gen(lm, 15))
        aver, disp = average_and_dispersion(poisson_gen(lm, 1000000))
        assert np.isclose(aver, lm)
        assert np.isclose(disp, lm)
        
    for ar in arr:
        plt.plot(ar[1])

    plt.show()
   
    for i in range(0, len(lam)):
        print("Лямбда =", lam[i])
        print("\tДисперсия:\t", dispersion(arr[i]), "+-", abs(lam[i] - dispersion(arr[i]))) 
        print("\tСреднее:\t", average(arr[i]), "+-", abs(lam[i] - average(arr[i])))
       
