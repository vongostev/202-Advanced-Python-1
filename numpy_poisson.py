import numpy as np
import scipy.special
import matplotlib.pyplot as plt

def poisson(sr, a):
    if sr<0:
        return 0
    else:
        return ((sr**a)*np.exp(-sr))/scipy.special.factorial(a)

def distr(sr, N):
    if sr < 0:
        return 0
    else:
        a = np.arange(N+1)
        return ((sr**a)*np.exp(-sr))/scipy.special.factorial(a)
 
def moment(n, k, sr):
    if not(isinstance(k, int) and np.size(np.array(n))>1 and sr>=0):
        return 0
    else:
        c = poisson(sr,n)*n**k
        return c.sum()

def disp(n, sr):
    if np.size(np.array(n))<1 and sr<0:
        return 0
    else:
        a = (n-moment(n, 1, sr))**2
        p = poisson(sr, n)
        return (a*p).sum()

N = float(input())
sr = input().split()

a = np.arange(N+1)
for i in sr:
    print(moment(a, 1, int(i)), disp(a, int(i)))
    plt.plot(distr(int(i), N))
    plt.scatter(moment(a, 1, int(i)), poisson(moment(a, 1, int(i)), moment(a, 1, int(i))), label='$r=1.3$')
    plt.show()