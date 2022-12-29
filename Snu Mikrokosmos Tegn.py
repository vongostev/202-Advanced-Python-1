import numpy as np
from dataclasses import dataclass
import matplotlib.pyplot as plt
import time
from tqdm import tqdm
import math
import imageio
G = 6.67*10**-1
dt = 5e-2
def del_arr(arr, a):
    for i in range(len(arr)):
        if arr[i]==a:
            arr.pop(i)
            break
    return arr
@dataclass
class CelestialBody: 
    time: float
    mass: float
    obj_radius: float
    velocity: np.ndarray
    radius_vector: np.ndarray
    size: float = 10
    def gravitate(self, bodies):             
   
        for i in bodies:
                r_i = i.radius_vector - self.radius_vector
                if np.all(r_i) !=0:
                    self.velocity += np.dot(G*dt/(np.linalg.norm(r_i)**3)*i.mass, r_i)
                
        self.radius_vector += dt*self.velocity
        return self
    def orbit_type(self, bodies):
        E = self.mass*np.linalg.norm(self.velocity)**2/2
        for i in bodies:
            r_i= i.radius_vector-self.radius_vector
            if np.all(r_i!=0):
                E -= G*self.mass*i.mass/np.linalg.norm(r_i)
        if E > 0:
            print('гиперболическая')
            
        elif E == 0:
            print('параболическая')
            
        elif E < 0:
            print('эллиптическая')
            
class System:
    def __init__(self,bodies,t):
        exist_bodies = []
        not_exist_bodies = []
        for i in bodies:
            if i.time == 0:
                exist_bodies.append(i)
            if i.time>0:
                not_exist_bodies.append(i)
        self.exist = exist_bodies
        self.not_exist = not_exist_bodies  
        self.t=t
        
    
    def add(self, t):
        a = self.not_exist.copy()
        for i in a:
            if i.time <= t:
                self.exist.append(i)
                del_arr(self.not_exist, i)
        return self
    def destroy(self):
        a = self.exist.copy()
        for i in a:
            
            for j in a:
                d=i.obj_radius+j.obj_radius
                if i != j and np.linalg.norm(i.radius_vector - j.radius_vector)<d:
                    del_arr(self.exist, i)
                    del_arr(self.exist, j)
        return self
    
    def step(self, t):
        self.add(t)
        self.destroy()
        for j in self.exist:
            j.gravitate(self.exist)
        return self.exist
    
    def animation(self, bodies):
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, projection='3d')
        t0 = 300
        for t in tqdm(np.arange(0., t0)):
            angle = 60 + 60 * t / t0
            ax.clear()
            ax.axes.set_xlabel('x')
            ax.axes.set_ylabel('y')
            ax.axes.set_zlabel('z')
            ax.axes.set_xlim3d(-100, 100)
            ax.axes.set_ylim3d(-100, 100)
            ax.axes.set_zlim3d(-100, 100)
            for i in range(len(bodies)):
                if abs(t - bodies[i].time)<0.00001 and bodies[i] not in self.exist:
                    self.add(bodies[i])
            list_x = [self.exist[i].radius_vector[0] for i in range(len(self.exist))]
            list_y = [self.exist[i].radius_vector[1] for i in range(len(self.exist))]
            list_z = [self.exist[i].radius_vector[2] for i in range(len(self.exist))]
            list_size = [self.exist[i].size for i in range(len(self.exist))]
            ax.scatter(list_x, list_y, list_z, s = list_size)
            ax.view_init(30 - angle * 0.2, angle)
            fig.canvas.draw()
            self.step(self.t)
if __name__ == '__main__':
    star = CelestialBody(0.,1000.,1.,np.array([0.,0.,0.]),np.array([0.,0.,0.]))
    Planet1 = CelestialBody(10.,5.,0.01,np.array([-1.,0.,13.]),np.array([-10.,-10.,8.]))
    Planet2 = CelestialBody(0.,7.,0.03,np.array([-7.,9.,9.]),np.array([9.,4.,6.]))
    s =[star,Planet1,Planet2]
    print("орбита первой планеты")
    Planet1.orbit_type(s)
    print("орбита второй планеты")
    Planet2.orbit_type(s)
    t=3000
    a = System(s,t)
    a.animation(s)