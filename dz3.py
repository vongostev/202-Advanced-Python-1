import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial


def Poiss(l, N):
    assert l > 0
    return np.random.poisson(lam=l, size=N)


def moment(k, n):
    assert k % 1 == 0
    assert type(n) == np.ndarray
    prob = np.array(list(map(lambda x: (n == x).sum() / n.size, n)))
    d = dict(zip(n, prob))
    return (np.array(list(d.keys()))**k * np.array(list(d.values()))).sum()


def mean(n):
    return moment(1, n)


def std(n):
    return moment(2, n - moment(1, n))


if __name__ == '__main__':

    def test_mean():
        assert abs(mean(Poiss(5, 100000)) - 5) < 0.1
        assert abs(mean(Poiss(10, 100000)) - 10) < 0.1
        print('mean_is_correct')

    def test_std():
        assert abs(std(Poiss(5, 100000)) - 5) < 0.1
        assert abs(std(Poiss(10, 100000)) - 10) < 0.1
        print('std_is_correct')

    test_mean()
    test_std()
