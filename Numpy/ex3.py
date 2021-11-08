import numpy as np
import math


def Puasson(N, lambd):
    N = int(N)
    lambd = float(lambd)
    A = np.linspace(2, N, N-1)
    a = np.linspace(0, 1, 2)
    x = list(math.exp(- lambd)*lambd**a/np.vectorize(math.factorial)(a))
    x += list(np.exp(- lambd + A*np.log(lambd*math.e/A))/np.sqrt(2*math.pi*A))
    return np.array(x)


def Start_moment(k, P):
    try:
        P = np.array(P)
    except:
        raise ValueError
    a = np.linspace(0, len(P) - 1, len(P))
    res = np.sum(P*(a**k))
    return res


def Dispersion(p):
    n = np.linspace(0, len(p) - 1, len(p))
    return np.sum(p*(n - Start_moment(1, p))**2)


N = 555
lambd = 333

p = Puasson(N, lambd)
print('N =', N, '\nlambda =', lambd)
print('первый момент:', Start_moment(1, p), '\nдисперсия:',
      Dispersion(p), '\nсуммарная вероятность:', sum(p))
