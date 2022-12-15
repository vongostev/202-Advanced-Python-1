import numpy as np
import math
import time
from tqdm import tqdm
from matplotlib import pyplot as plt
g = 1


class Planet():
    def __init__(self, m, p, s):
        self.mass = m
        self.speed = s
        self.point = p
        self.lspeed = [0, 0, 0]

    @np.vectorize
    def gravitate(self, obj, dt=1):
        dpx = obj.point[0]-self.point[0]
        dpy = obj.point[1]-self.point[1]
        dpz = obj.point[2]-self.point[2]
        r = round(dpx*dpx+dpy*dpy+dpz*dpz, 5)
        if (r == 0):
            # print("d")
            del self
        else:
            self.speed[0] += (g*obj.mass*dpx/pow(r, 1.5)*dt)
            self.speed[1] += (g*obj.mass*dpy/pow(r, 1.5)*dt)
            self.speed[2] += (g*obj.mass*dpz/pow(r, 1.5)*dt)

    @np.vectorize
    def move(self, dt):
        self.point[0] += self.lspeed[0]*dt + dt*dt*(self.speed[0] -
                                                    self.lspeed[0])/2
        self.point[1] += self.lspeed[1]*dt + dt*dt*(self.speed[1] -
                                                    self.lspeed[1])/2
        self.point[2] += self.lspeed[2]*dt + dt*dt*(self.speed[2] -
                                                    self.lspeed[2])/2

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
            pl.move(pl, self.dt)

    def step(self):
        a = []
        for i in range(len(self.planets)):
            poi = self.planets[i].point
            a.append(poi)
            for p in range(len(self.planets)):
                if (p != i):
                    self.planets[i].gravitate(self.planets[i],
                                              self.planets[p], self.dt)

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


sun = Planet(10000000, [0, 0, 0], [0, 0, 0])
earth = Planet(1, [10, 0, 0], [0, 800, 0])
moon = Planet(1, [0, 0, 10], [0, -1000, 0])
st = Syst()
st.add(sun)
st.add(earth)
st.add(moon)

for i in range(10):
    data = [[], [], []]
    try:
        d = st.step()
        print(d)
        for pl in d:
            data[0].append(pl[0])
            data[1].append(pl[1])
            data[2].append(pl[2])
    except:
        print("error")

%matplotlib notebook
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
    axis.scatter(data[0], data[1], data[2], s=30)
    data = [[], [], []]
    try:
        d = st.step()
        for pl in d:
            data[0].append(pl[0])
            data[1].append(pl[1])
            data[2].append(pl[2])
    except:
        print("error")

    # axis.view_init(30 - angle * 0.2, angle)
    axis.view_init(30, 60)
    fig.canvas.draw()
