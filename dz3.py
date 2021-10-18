import numpy as np
import scipy.special


def poiss(l, N):
    assert l >= 0
    x = np.arange(N)
    y = l ** x * np.exp(-l) / scipy.special.factorial(x)
    return np.array([x, y])


def moment(k, n):
    assert k % 1 == 0
    assert type(n) == np.ndarray
    return (np.unique(n ** k *
                      np.array([(n == i).sum() / len(n) for i in n]))).sum()


def mean(n):
    return moment(1, n)


def std(n):
    return moment(2, n - moment(1, n))


if __name__ == '__main__':

    def test_mean():
        assert abs(mean(np.random.poisson(5, 100000)) - 5) < 0.1
        assert abs(mean(np.random.poisson(10, 100000)) - 10) < 0.1
        print('mean_is_correct')

    def test_std():
        assert abs(std(np.random.poisson(5, 100000)) - 5) < 0.1
        assert abs(std(np.random.poisson(10, 100000)) - 10) < 0.1
        print('std_is_correct')

    test_mean()
    test_std()
