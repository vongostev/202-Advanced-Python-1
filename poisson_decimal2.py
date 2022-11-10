import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal

def poisson(sr, N):
    if sr<0:
        raise ValueError('sr must be negative')
    else:
        a = np.arange(N+1)
        return ((sr**a)*exp(-sr))/fact(a)
 
def moment(n, k):
    if not(isinstance(k, int) and np.size(np.array(n))>1):
        raise ValueError('Wrong type of parametres')
    else:
        arr = np.arange(np.size(n))
        c = n*arr**k
        return c.sum()

def disp(n):
    return moment(n, 2) - moment(n, 1) ** 2   
    
def exp(x):
    return x.exp()

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
    print('Среднее и дисперсия', b, disp(a))
    plt.plot(a)
    y = poisson(b,b)
    plt.scatter(b, y[np.size(y)-1], label='$r=1.3$')
    plt.show()

if __name__ == '__main__':
    test_graph_func(Decimal('300'), Decimal('2'))
    test_graph_func(Decimal('300'), Decimal('10'))
    test_graph_func(Decimal('300'), Decimal('20'))

