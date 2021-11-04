import numpy as np
import math
import matplotlib.pyplot as plt
# print('😅')


def Pois(N, la):
    assert N == int(N)
    assert la > 0

    N = int(N)
    la = float(la)
    if N < 7:
        n1 = np.linspace(0, N, N + 1)
        return math.exp(-la)*la**n1/np.vectorize(math.factorial)(n1)
    else:
        n = np.linspace(7, N, N-6)
        n1 = np.linspace(0, 6, 7)
        # return np.array([math.exp(-la)]+list(math.exp(-la)*(la*math.e/n)**n/ np.sqrt(2 * math.pi * n) ))
        an = list(math.exp(- la)*la**n1/np.vectorize(math.factorial)(n1))
        an += list(np.exp(- la + n*np.log(la*math.e/n)) / np.sqrt(2*math.pi*n))
        # промежуточные вычисления не должны содержать больших чисел,
        # поэтому возведение в степень больших и маленьких чисел стоит объединить
        return np.array(an)
    # маленькие числа лучше считать в лоб, для больших использовать приближение


def Moment(k, P):
    try:
        pp = np.array(P)
        k = int(k)
    except:
        raise ValueError
    n = np.linspace(0, len(pp) - 1, len(pp))
    ans = np.sum(pp*(n**k))
    #print("Moment", k, ans)
    return ans


def Mid(p):
    return Moment(1, p)


def Disp(p):
    # return - Moment(1, p)**2 + Moment(2, p) # низкая точность вычислений
    n = np.linspace(0, len(p) - 1, len(p))
    return np.sum(p*(n - Moment(1, p))**2)


def dis2(nm, p):
    s = 0
    for i in range(len(p)):
        s += p[i] * (nm - i)**2
    return s


n = 100000
la = 5200
p = Pois(n, la)
print('n =', n, 'la =', la)
print('первый момент', Moment(1, p), 'дисперсия без цикла',
      Disp(p), 'дисперсия с циклом', dis2(Moment(1, p), p))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid(axis='both')

print('суммарная вероятность', sum(p))
plt.plot(np.linspace(0, n, n + 1), p,  '-', color='b')
plt.show()
