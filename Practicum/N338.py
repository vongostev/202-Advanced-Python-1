import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

"""МНК"""
def LSM(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    vopt, vcov = curve_fit(lambda x, A, B: A*x+B, X, Y)
    sv = np.sqrt(np.diag(vcov))
    return (vopt[0], vopt[1], sv[0], sv[1])


"""считываем данные эксперимента и готовим график"""
df = pd.read_csv('C:/py/202-Advanced-Python-1/Practicum/338_1.txt', sep='\t').astype(float)
diamagnetic = ['cu', 'al', 'br']
ferramagnetic = ['fe', 'pb', 'ti']
colour = ['r', 'g', 'b']
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid(axis='both')
ax.set(
    title='Зависимость $tg(\phi)$ от $f$',
    ylabel='$tg(\phi)$',
    xlabel='$f, Hz$')
n = 85
cl = 0
pr = []
spr = []
for m in diamagnetic:
    x = df.tail(n).values
    y = np.tan(df.tail(n).values/180.*3.1416)
    plt.plot(x, y, 'o', color=colour[cl])
    plt.plot(x, LSM(x, y)[0]*x+LSM(x, y)[1],  '-', color=colour[cl], label=m)
    pr.append(LSM(x, y)[0])
    spr.append(LSM(x, y)[2])
    cl += 1
ax.legend()
fig.savefig('N338_0.png', dpi=400)
plt.show()
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid(axis='both')
ax.set(
    title='Зависимость $tg(\phi)$ от $f$',
    ylabel='$tg(\phi)$',
    xlabel='$f, Hz$')
n = 14
cl = 0
for m in ferramagnetic:
    x = df['Hz'+m].head(19).tail(n).values
    y = np.tan(df['deg'+m].head(19).tail(n).values/180.*3.1416)
    plt.plot(x, y, 'o', color=colour[cl])
    plt.plot(x, LSM(x, y)[0]*x+LSM(x, y)[1],  '-', color=colour[cl], label=m)
    pr.append(LSM(x, y)[0])
    spr.append(LSM(x, y)[2])
    cl += 1
ax.legend()
fig.savefig('N338_1.png', dpi=400)
plt.show()
spr = np.abs(np.array(spr)/np.array(pr))
for t in range(1, len(pr)):
    pr[t] *= 60/pr[0]
pr[0] = 60
print(pr)
print(np.array(pr)*spr)
fr = np.arange(100, 1000, 10)
mus = [1, 1, 1, 1000, 1, 1]


def skin_effect(f, si, mu):
    return 1/(np.sqrt(3.1416*f*4*3.1416e-7*si*mu))


colour += ['cyan', 'black', 'yellow']
cl = 0
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.grid(axis='both')
ax.set(
    title='Зависимость толщины скин-слоя от частоты',
    ylabel='$\delta , мм$',
    xlabel='$f, Hz$')
for i in range(6):
    sk = skin_effect(fr, pr[i]*1e6, mus[i])
    plt.plot(fr, 1e3*sk, '.', color=colour[cl], label=(diamagnetic+ferramagnetic)[i])
    cl += 1
ax.legend()
fig.savefig('N338_2.png', dpi=400)
plt.show()
