import numpy as np
from scipy.special import factorial


def generate_distribution(lbd, N):
    if lbd < 0 or N < 0:
        raise ValueError
    n = np.arange(N+1)
    return np.float_power(lbd, n)*np.exp(-lbd)/factorial(n)


def moment(distribution, k, values=0):
    if not isinstance(distribution, np.ndarray) or not isinstance(k, int):
        raise ValueError
    if not isinstance(values, np.ndarray) or values.size != distribution.size:
        values = np.arange(distribution.size)
    return np.sum(values**k*distribution)


def average(distribution, values=0):
    if not isinstance(distribution, np.ndarray):
        raise ValueError
    return moment(distribution, 1, values)


def dispersion(distribution):
    if not isinstance(distribution, np.ndarray):
        raise ValueError
    return average(distribution, (np.arange(distribution.size) - average(distribution)) ** 2)


def test_correct_values():
    for lbd in np.arange(2, 105, step=10):
        for N in np.arange(10, 151, step=10):
            print(
                f'lambda = {lbd}, N = {N}, average = {average(generate_distribution(lbd, N))}, dispersion = {dispersion(generate_distribution(lbd, N))}')


def test_incorrect_values():
    try:
        generate_distribution(-1, 10)
    except ValueError:
        print('Lambda must be positive')
    try:
        moment(1, 1)
    except ValueError:
        print('Distribution must be np.ndarray')
    try:
        moment(generate_distribution(2, 25), 0.5)
    except ValueError:
        print('Moment power must be integer')


if __name__ == "__main__":
    test_correct_values()
    test_incorrect_values()
