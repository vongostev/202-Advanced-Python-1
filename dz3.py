# переделал функции в понятную форму, но мое прошлое решение валидно,
# прикрепил доказательство этого в pdf документе

import numpy as np
import scipy.special


def poiss(l, N):
    assert l >= 0
    x = np.arange(N)
    y = l ** x * np.exp(-l) / scipy.special.factorial(x)
    return np.array([x, y])


def moment(n, k):
    assert k % 1 == 0
    assert type(n) == np.ndarray
    return (n[0] ** k * n[1]).sum()


def mean(n):
    return moment(n, 1)


def std(n):
    return mean(np.array([(n[0] - mean(n)) ** 2, n[1]]))


if __name__ == '__main__':
    l = 4
    arr = poiss(l, 1000)

    def test_mean():
        assert abs(mean(arr) - l) < 0.1
        print('mean_is_correct')

    def test_std():
        assert abs(std(arr) - l) < 0.1
        print('std_is_correct')

    test_mean()
    test_std()
