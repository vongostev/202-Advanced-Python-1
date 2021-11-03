import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial



def poiss(lbd, N):
    if lbd < 0:
        raise ValueError("Function undefiend for negative lambda ")
    n = np.arange(N + 1)
    #return np.array([(lbd ** n) * np.exp(-lbd) / factorial(n), n]) #ощутить разницу (пройдет только первый assert)
    return np.array([(np.float_power(lbd, n)) * np.exp(-lbd) / factorial(n), n])


def momentum(arr, k):
    if k < 0 or not isinstance(k, int) or not isinstance(arr, np.ndarray):
        raise ValueError("Incorrect data format")
    #return np.sum((arr[1] ** k) * arr[0]) #ощутить разницу, но тут, как и далее - не особо
    return np.sum(np.float_power(arr[1],k) * arr[0])   



def mean(arr):
    if not isinstance(arr, np.ndarray):
        raise ValueError("Incorrect data format")
    return momentum(arr, 1)



def dispersion(arr):
    if not isinstance(arr, np.ndarray):
        raise ValueError("Incorrect data format")
    #return mean(np.array([arr[0], ((arr[1] - mean(arr)) ** 2)])) #ощутить разницу
    return mean(np.array([arr[0], np.float_power((arr[1] - mean(arr)), 2)]))
     


if __name__ == '__main__':
   
    array1 = poiss(4, 100)
    print(mean(array1))
    print(dispersion(array1))
    assert np.allclose(mean(array1), 4, 1e-10)
    assert np.allclose(dispersion(array1), 4, 1e-10)
    
    array2 = poiss(7, 100)
    print(mean(array2))
    print(dispersion(array2))
    assert np.allclose(mean(array2), 7, 1e-10)
    assert np.allclose(dispersion(array2), 7, 1e-10)
    
    array3 = poiss(10, 100)
    print(mean(array3))
    print(dispersion(array3))
    assert np.allclose(mean(array3), 10, 1e-10)
    assert np.allclose(dispersion(array3), 10, 1e-10)
    
    

    plt.plot(array1[0], label='λ = 4')
    plt.plot(array2[0], label='λ = 7')
    plt.plot(array3[0], label='λ = 10')
    plt.xlim(0, 25)
    plt.legend(fontsize = 10)
    plt.show()

