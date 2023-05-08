#!/usr/bin/env python
# coding: utf-8

# In[19]:


import random
import numpy as np
import matplotlib.pyplot as plt
import math
import itertools


class Cell:           
#класс клетка, в котором хранится количество и характеристики дроплетов
    bodies = []
    Dt = 0.1    
    T=180 
    def J(t):         
#метод, определяющий поток, который попал в клетку в момент времени t
        J0=5 
        alpha=0.1  
        return J0*np.sin(t*alpha)
    def formula(t):     
#метод, считающий производную обьема каждого дроплета в момент времени t
        dV_dt = np.zeros(len(Cell.bodies),dtype=float)
        v=[] 
        for i in Cell.bodies:
            v.append(i.volume)
        v=np.array(v)
        for j in range(len(Cell.bodies)):
            dV_dt[j]=Cell.J(t)*np.power(Cell.bodies[j].volume,0.7)/np.sum(np.power(v,0.7))
        return dV_dt
    def add_body(body):
#метод добавления дроплета в клетку. он вызывается, когда мы инициализируем новый дроплет
        Cell.bodies.append(body)
    def merge():
#метод, определяющий слились ли какие-то два дроплета за промежуток времени dt
        p=np.random.uniform(0,0.0225)   #random probability 
        m=np.random.randint(len(Cell.bodies), size=2)  #which of them merged
        if(m[0]!=m[1] and len(Cell.bodies)>1):
            if random.choices([True,False],weights = [p,1-p])[0]:
                if Cell.bodies[m[0]].volume>Cell.bodies[m[1]].volume:
                    Cell.bodies[m[0]].volume=Cell.bodies[m[0]].volume+Cell.bodies[m[1]].volume
                    Cell.bodies.pop(m[1])
                else:
                    Cell.bodies[m[1]].volume=Cell.bodies[m[0]].volume+Cell.bodies[m[1]].volume
                    Cell.bodies.pop(m[0])
    def add():
#метод, определяющий появились ли новые дроплета за промежуток времени dt
        p=np.random.uniform(0,0.005)   #random probability 
        if random.choices([True,False],weights = [p,1-p])[0]:
            Droplets(5)
    def check():
#метод, который вызывается каждую итерацию chаnge() чтобы проверить, 
#что все обьемы положительны и при необходимости удалить отрицательные
        ind=[]
        for i, v in enumerate(Cell.bodies):
            if v.volume<=0: Cell.bodies.pop(i)
      
    def change():
#метод, считающий, как изменились обьемы дроплетов за dt
        n_steps = int(round((Cell.T)/Cell.Dt))
        t_arr = np.zeros(n_steps + 1)  
        for i in range (1, n_steps + 1):
            t = t_arr[i-1]
            dVdt = Cell.formula(t) 
            V0=np.zeros(len(Cell.bodies)+1)
            for idx,val in np.ndenumerate(Cell.bodies):
                V0[idx]=val.volume
            for idx,val in np.ndenumerate(Cell.bodies):
                val.volume=V0[idx] +Cell.Dt*dVdt[idx] 
            t_arr[i] = t + Cell.Dt
            Cell.check()
            Cell.merge()
            Cell.add()
            T=np.zeros(len(Cell.bodies))+t  
            v=[] 
            col=[]
            for i in Cell.bodies:
                v.append(i.volume)
                col.append(i.colour)
            v=np.array(v)
            plt.xlabel('t (in miliseconds)', fontsize = 12)
            plt.ylabel('V(t)', fontsize = 12)
            plt.scatter(T, v, s=5 ,c=col)
   
        
class Droplets:
    
    colours = itertools.cycle(['#3366CC','#DD4477','#009292','#FF6DB6','#DC3912','#FF9900','#109618','#990099',
                               '#0099C6','#004949','#7E0021','#314004','#7375B5','#4B1F6F','#6B452B','#A89985','#370335',
                               '#A50E82'])
    def __init__(
        self,
        volume
    ):
        self.volume = volume
        self.colour = next(Droplets.colours)
        Cell.add_body(self)
        
#инициализируем 7 дроплетов. их число ограниченно размерами клетки 
#(то есть суммарный обьем не должен быть больше клетки, подробнее - в тз)
Droplets(20)
Droplets(20)
Droplets(20)
Droplets(20)
Droplets(20)
Droplets(20)
Droplets(20)
Droplets(20)
Droplets(20) 
Cell.change()


# In[20]:


import unittest

class TestCell(unittest.TestCase):
  def setUp(self):
    self.cell = Cell()
  
  def test_J(self):   #тестируем метод, выдающий обьем
    self.assertEqual(Cell.J(7), 3.2210884361884555)
    
unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:





# In[ ]:




