import numpy as np
from scipy.special import factorial
import matplotlib.pyplot as plt


def gen_poisson(lbd, N):
    if lbd < 0:
        raise ValueError("lambda shouldn't be negative")
    n = np.arange(N + 1)
    return lbd ** n / factorial(n) * np.exp(-lbd)

def momentum(P, k):
    if type(P) != np.ndarray:
        raise TypeError("P should be numpy.ndarray")
    if type(k) != int:
        raise TypeError("k should be int")
    n = np.arange(P.size)
    return np.sum(n ** k * P)

def mean_and_dispersion(P):
    mean = momentum(P, 1)
    return mean, momentum(P, 2) - mean ** 2

if __name__ == "__main__":
    for lbd in [0.01, 0.2, 0.5, 1, 2, 3, 4, 5, 6]:
        mean, disp = mean_and_dispersion(gen_poisson(lbd, 1000000))
        assert np.isclose(mean, lbd)
        assert np.isclose(disp, lbd)
        
    plt.plot(gen_poisson(5, 20))
    plt.show()
