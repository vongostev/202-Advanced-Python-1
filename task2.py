import numpy as np
from scipy.stats import poisson
from math import exp
from math import pow
from math import sqrt
import scipy.special
#Задание1


def poisson_fun(lamda, N):
    try:
        z = np.arange(0, N, 1)
        x = poisson.pmf(z, lamda)
        #print(x)
        return x
        if lamda < 0:
            raise ValueError
    except ValueError:
        print("Lambda must be positittve")

#Задание2
def moments(arr, k):
    try:
        indexes = np.arange(arr.size)
        indexes = np.power(indexes, k)
        a = np.dot(indexes, arr)
        #res = a.sum()
        return a
    except:
        print('Incorrect data')

#Задание3

def average(new_arr):    #new_arr заменить на array для тстирования с моментами
    #new_arr = np.moments(array, k)
    #avg = 0
    #num = 0
    #for i in new_arr:
        #avg += i
        #num += 1

    #print(avg)
    #avg = avg / num
    avg = moments(new_arr, 1)

    #res_arr = np.power(new_arr - avg, 2)

    #disp = 0
    #for i in res_arr:
        #disp += i

    #disp = disp / res_arr.size
    #print(res_arr)
    #disp = moments(res_arr, k)

    return avg

def dispers(new_arr, N):
    avg = average(new_arr)
    res_arr = np.power(new_arr - avg, 2)
    #disp = moments(res_arr, 1)
    disp = np.dot(res_arr, poisson_fun(new_arr, N))
    return sqrt(disp)


#Задание4

lamda = float(input())
N = int(input())
k = int(input())
pois_arr = poisson_fun(lamda, N)
#pois_arr = moments(pois_ar, k)
aver = average(pois_arr)
disper = dispers(pois_arr, N)

#print(moments(pois_arr, k))

print(aver)
print(disper)


