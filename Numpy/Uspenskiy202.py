import numpy as np
import matplotlib.pyplot as plt
import scipy.special


def poisson(лямбда, N):
    assert лямбда >= 0, 'Lambda should not be negative'
    x = np.arange(N)
    y = лямбда ** x * np.exp(-лямбда) / scipy.special.factorial(x)
    return np.array([x, y])


def moment(array, k):
    assert isinstance(k, int), 'k is not int'
    assert isinstance(array, np.ndarray)
    return (array[0] ** k * array[1]).sum()


def average(array):
    return moment(array, 1)


def dispersion(array):
    return average(np.array([(array[0] - average(array)) ** 2, array[1]]))


лямбда = 3
k = 2

arr = poisson(лямбда, 150)

plt.plot(arr[0], arr[1])
plt.title("Poisson distribution")
plt.show()

print(f'Moment with k = {k} :', moment(arr, k))
print('Average: ', average(arr))
print('Dispersion: ', dispersion(arr))

assert np.allclose([average(arr), dispersion(arr)], [лямбда, лямбда], 0.1)
