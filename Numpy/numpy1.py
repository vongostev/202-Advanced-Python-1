import numpy as np
import sys


def gen(lam, N):
    if (lam < 0 or N < 0):
        raise ValueError
    n = np.arange(0, N + 1)
    return (n, np.exp(n * np.log(lam) - np.cumsum(np.log(n + 1)) - lam) * (n + 1))


def moment(arr, k):
    if (not isinstance(k, int) or not isinstance(arr, tuple) or not isinstance(
            arr[0], np.ndarray) or not isinstance(arr[1], np.ndarray)):
        raise ValueError
    return np.sum(arr[0]**k * arr[1])


def average(arr):
    return moment(arr, 1)


def dispersion(arr):
    return moment(((arr[0] - average(arr)), arr[1]), 2)


def test_correct_argument():
    for lam in [1, 5, 100, 100000]:
        sys.stderr.write(f'lambda = {lam}\n')
        for N in [1, 10, 100, 100000, 1000000]:
            s = gen(lam, N)
            sys.stderr.write(
                f'	N = {N}, <N> = {average(s)}, <(N - <N>)**2> = {dispersion(s)}\n')


def test_incorrect_argument():
    try:
        gen(-1, 1)
    except ValueError:
        sys.stderr.write(f'lam < 0 OK\n')
    else:
        sys.stderr.write(f'lam < 0 KO\n')
    try:
        average(1)
    except ValueError:
        sys.stderr.write(f'average bad argument OK\n')
    else:
        sys.stderr.write(f'average bad argument KO\n')
    try:
        moment(np.arange(2), 'bad_argument')
    except ValueError:
        sys.stderr.write('moment bad argument OK\n')
    else:
        sys.stderr.write(f'moment bad argument - 1 KO\n')


if __name__ == "__main__":
    test_correct_argument()
    test_incorrect_argument()
