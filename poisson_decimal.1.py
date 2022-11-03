import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

def poisson(sr, N):
    if sr<0:
        raise ValueError('sr must be negative')
    else:
        a = np.arange(N+1)
        return ((sr**a)*exp(-sr))/fact(a)
    
def poisson_uni(sr, a):
    if sr<0:
        return 0
    else:
        return ((sr**a)*exp(-sr))/fact(a)
    
def moment(n, k):
    if not(isinstance(k, int) and np.size(np.array(n))>1):
        raise ValueError('Wrong type of parametres')
    else:
        arr = np.arange(np.size(n))
        c = n*arr**k
        return c.sum()

def disp(n):
    if np.size(np.array(n))<1:
        raise ValueError('Parametr must be array')
    else:
        a = (np.arange(np.size(n), 1)-moment(n, 1))**2
        return (n*a).sum()
        
def exp(x):
    i, last, s, fact, num = 0, 0, 1, 1, 1
    while s != last:
        last = s
        i += 1
        fact *= i
        num *= x
        s += num/fact
    return +s

@np.vectorize
def fact(n):
    factorial = Decimal('1')
    while n > Decimal('1'):
        factorial *= n
        n -= Decimal('1')
    return factorial

def test_graph_func(N, sr):
    a = poisson(sr, N)
    b = moment(poisson(sr, N), 1)
    plt.plot(a)
    plt.scatter(b, poisson_uni(b,b), label='$r=1.3$')
    plt.show()

if __name__ == '__main__':
    test_graph_func(Decimal('300'), Decimal('2'))
    test_graph_func(Decimal('300'), Decimal('10'))
    test_graph_func(Decimal('300'), Decimal('20'))
