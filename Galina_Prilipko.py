# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 16:41:37 2022

@author: galin
"""


#from scipy.stats import poisson
from decimal import Decimal

import numpy as np
import matplotlib.pyplot as plt


def poisson_d(N,  mu):
    #n = np.arange(0,N)
   # y = poisson.pmf(n, mu) встроенная функция 
    n1 = np.arange(1,N)
    n_l=np.log(n1)
    Y = -mu+n1*np.log(mu)-np.cumsum(n_l) #берем логарифм от пуассона, чтобы было проще считать
    y = np.exp(Y)
    y = np.insert(y,0,np.exp(-mu)) #добавляет значение в нуле
    #y = np.power(mu,n)*np.exp(-mu)/sp.factorial(n) работает на маленьких N
    return y

   
    
def moments(n,y):
    try:
        N=y.size
        
        x = np.arange(0, N)
        x=np.power(x,n)
        return np.dot(x, y)
    except: print("error: y should be an array")

try:
    N = float(input('enter N '))
    mu = float(input('enter average '))
    assert(mu>0)
    assert(N>0)
    assert(N>mu)
    
except:
    print("N and mu should be int>0 and N>mu")

x = np.arange(0, N)
plt.plot(x,poisson_d(N, mu),'bo')
plt.xlim(0,3*mu)
plt.suptitle('Float')
plt.show()

N_dec=Decimal(N)
mu_dec=Decimal(mu)
y = poisson_d(N,mu)
x = np.asarray([Decimal(i) for i in x])
y = np.asarray([Decimal(i) for i in y])

plt.plot(x,y,'bo')
plt.xlim(0,3*mu)
plt.suptitle('Decimal')
plt.show()
try:
   x1 = np.arange(0, N)
   n=int(input('enter n '))
   assert(n>0)
   Y=poisson_d(N, mu)
   print('moments for floats=',moments(n,Y))
   a=np.dot(x1, poisson_d(N,mu))
   print('theoretical average for floats =', a)
   b = np.power((x1 - a),2)
   k = np.dot(b,poisson_d(N,mu))
   print('dispersion for floats =', k)
   
except: print("n must be an integer>0")
n_dec=Decimal(n)
m = moments(n,Y)
m = Decimal(m)
print('moments for dec=',m)
a=np.dot(x, y)
print('theoretical average for dec =', a)
b = np.power((x - a),2)
k = np.dot(b,y)

print('dispersion for dec =', k)
