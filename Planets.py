#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(1)


# In[4]:


import numpy as np
import math
import time
from tqdm import tqdm
from matplotlib import pyplot as plt
g = 1


class Planet():
    def __init__(self, m, p, s, r):
        self.mass = m
        self.speed = s
        self.point = p
        self.lspeed = [0, 0, 0]
        self.size = r
        self.color = "b"

    def gravitate(self, obj, dt=1):
        dpx = obj.point[0]-self.point[0]
        dpy = obj.point[1]-self.point[1]
        dpz = obj.point[2]-self.point[2]
        r = round(dpx*dpx+dpy*dpy+dpz*dpz, 5)
        if (r == 0):
            del self
        else:
            self.speed[0] += round((g*obj.mass*dpx/pow(r, 1.5)*dt), 5)
            self.speed[1] += round((g*obj.mass*dpy/pow(r, 1.5)*dt), 5)
            self.speed[2] += round((g*obj.mass*dpz/pow(r, 1.5)*dt), 5)

    def move(self, dt):
        self.point[0] += round(self.lspeed[0]*dt + dt*dt*(self.speed[0] - self.lspeed[0])/2, 5)
        self.point[1] += round(self.lspeed[1]*dt + dt*dt*(self.speed[1] - self.lspeed[1])/2, 5)
        self.point[2] += round(self.lspeed[2]*dt + dt*dt*(self.speed[2] - self.lspeed[2])/2, 5)

    def show(self):
        print(self.point, "    ", self.speed)

    def take(self, a):
        return self.point[a]

    def __del__(a):
        pass


class Syst():
    def __init__(self, dt=0.001, n=100, t=0):
        self.planets = []
        self.dt = dt
        self.n = n
        self.t = t
        self.data = np.array([[], [], []])

    def add(self, Planet):
        self.planets.append(Planet)

    def st_move(self):
        for pl in self.planets:
            pl.move(self.dt)

    def step(self):
        lenght = len(self.planets)
        a = [self.planets[i].point for i in range(lenght)]
        for i in range(lenght):
            for p in range(lenght):
                if (p != i):
                    self.planets[i].gravitate(self.planets[p], self.dt)

        self.st_move()
        self.t += self.dt
        for pl in self.planets:
            pl.lspeed = pl.speed
        return(a)

    def show(self):
        for i in range(len(self.planets)):
            self.planets[i].show()

    def takepl(self):
        self.planets[0].take(0)


sun = Planet(10000000, [0, 0, 0], [0, 0, 0], 150)
earth = Planet(10, [9, 0, 0], [0, 800, 0], 35)
moon = Planet(10, [0, 0, 10], [0, -1000, 0], 50)
com = Planet(1, [10, 20, 0], [-800, 0, 0], 10)
st = Syst()
st.add(sun)
st.add(earth)
st.add(moon)
st.add(com)
print("")

for i in range(10):
    data = [[], [], []]
    d = st.step()
    print(d)
    for pl in d:
        data[0].append(pl[0])
        data[1].append(pl[1])
        data[2].append(pl[2])


get_ipython().run_line_magic('matplotlib', 'notebook')
fig = plt.figure(figsize=(5, 5))
axis = fig.add_subplot(111, projection='3d')
axis.axes.set_xlim3d(-10, 10)
axis.axes.set_ylim3d(-10, 10)
axis.axes.set_zlim3d(-8, 8)
fig.show()
fig.canvas.draw()

dt = 2e-2
t0 = 10

for t in tqdm(np.arange(0., t0, dt)):
    angle = 60 + 60 * t / t0
    axis.clear()
    axis.axes.set_xlim3d(-10, 10)
    axis.axes.set_ylim3d(-10, 10)
    axis.axes.set_zlim3d(-8, 8)
    axis.scatter(data[0], data[1], data[2],
                 s=[st.planets[i].size for i in range(len(st.planets))],
                 c=['r', 'm', 'g', 'b'])
    data = [[], [], []]
    d = st.step()
    for pl in d:
        data[0].append(pl[0])
        data[1].append(pl[1])
        data[2].append(pl[2])
    axis.view_init(30 - angle * 0.2, angle)
    fig.canvas.draw()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




