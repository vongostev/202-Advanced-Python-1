import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import math
from decimal import Decimal, getcontext

getcontext().prec = 10

@np.vectorize
def Puas(n, liam):
    if liam<0:
        raise ValueError("liambda<0")
    g1=np.arange(n)
    g2=liam**g1
    g3=math.exp(-liam)
    g4=scipy.special.factorial(g1)
    return g2*g3/g4
def srednk(k, Pu):
    if isinstance(k, int) and isinstance(Pu, np.ndarray):
        nk=np.arange(len(Pu))**k
        return np.sum(nk*Pu)
    else:
        raise ValueError("k или Пуассон имеют не тот тип")
def dispersia(Pu):
     b=(np.arange(len(Pu))-srednk(1,Pu))**2
     return np.sum(b*Pu)
    
def dec_Puas(n,liam):
    if liam<0:
        raise ValueError("liambda<0")
    lm=Decimal(liam)
    g1=np.arange(n, dtype="float64")
    g2=(scipy.special.factorial((g1.astype(int)))).astype(float)
    g11=np.asarray([Decimal(i) for i in g1])
    g22=np.asarray([Decimal(i) for i in g2])
    g3=lm**g11
    g4=(-lm).exp()
    return g3*g4/g22

def dec_srednk(k, Pu):
    if isinstance(k, int) and isinstance(Pu, np.ndarray):
        nk1=np.arange(len(Pu), dtype="float64")
        nk2=np.asarray([Decimal(i) for i in nk1])
        return np.sum((nk2**k)*Pu)
    else:
        raise ValueError("k или Пуассон имеют не тот тип")
    
def dec_dispersia(Pu):
    b=(np.arange(len(Pu), dtype="float64" ))
    b1=np.asarray([Decimal(i) for i in b])
    return np.sum(((b1-dec_srednk(1, Pu))**2)*Pu)
    
def test(n, liambda, d):
    Puasson=Puas(n,liambda)
    sr=srednk(1, Puasson)
    disp=dispersia(Puasson)
    dec_Puasson=dec_Puas(n, liambda)
    dec_sr=dec_srednk(1, dec_Puasson)
    dec_disp=dec_dispersia(dec_Puasson)
    liambd=Decimal(liambda)
    k=liambd*Decimal(d)
    if abs(sr-liambda)<liambda*d and abs(disp-liambda)<liambda*d:
        print(f"Puasson({n},{liambda}): True")
    else:
        print(f"Puasson({n},{liambda}): False")
    if abs(dec_sr-liambd)<k and abs(dec_disp-liambd)<k:
        print(f"dec_Puasson({n},{liambda}): True")
    else: 
        print(f"dec_Puasson({n},{liambda}): False")
    plt.plot(Puasson[:101], label="P(n)")
    plt.plot(dec_Puasson[:101], label="dec_P(n)")
    plt.title(f"Puasson({n},{liambda})")
    plt.xlabel("n")
    plt.ylabel("P(n)")
    plt.grid()
    plt.show()
    
for i in range(1,30,3):
    test(100, i, 0.01)