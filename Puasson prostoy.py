import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import math

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
def test(n, liambda, d):
    Puasson=Puas(n,liambda)
    sr=srednk(1, Puasson)
    disp=dispersia(Puasson)
    if abs(sr-liambda)<liambda*d and abs(disp-liambda)<liambda*d:
        print(f"Puasson({n},{liambda}): True")
    else:
        print(f"Puasson({n},{liambda}): False")
    plt.plot(Puasson[:100], label="P(n)")
    plt.title(f"Puasson({n},{liambda})")
    plt.xlabel("n")
    plt.ylabel("P(n)")
    plt.grid()
    plt.show()
    
for i in range(1,30,3):
    test(100, i, 0.01)

