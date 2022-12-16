import numpy as np
from dataclasses import dataclass
import matplotlib.pyplot as plt
import time
from tqdm import tqdm
import math
import imageio
G = 6.67*10**-1
dt = 5e-2
eps = 10e-1

def remove_arr(arr, a):
    for i in range(len(arr)):
        if np.array_equal(arr[i], a):
            arr.pop(i)
            break
    return arr

@dataclass
class CosmicBody:
    mass: float
    v: np.ndarray
    r: np.ndarray
    t0: float

    def gravitate(self, bodys: list):
        dv = 0
        for i in range(len(bodys)):
            dr = bodys[i].r- self.r
            if np.all(dr!=0):
                dv += np.dot(G*dt*bodys[i].mass/(np.linalg.norm(dr)**3), dr)
        self.v += dv
        self.r += self.v*dt+(dv*dt**2)/2        
        return self
                    
    def print1(self):
        print(self.v, self.r)
    
    def orbit_type(self, bodys: list):
        E = self.mass*np.linalg.norm(self.v)**2/2
        for i in range(len(bodys)):
            dr = dr = bodys[i].r- self.r
            if np.all(dr!=0):
                E -= G*self.mass*bodys[i].mass/np.linalg.norm(dr)
        if E > 0:
            print('Hyperbola')
            #return 'Hyperbola'
        elif E == 0:
            print('Parabola')
            #return 'Parabola'
        elif E < 0:
            print('Ellipse')
            #return 'Ellipse'
            
        
    
class System:
    def __init__(self, path):
        syst = np.loadtxt(path, delimiter=' ', dtype=float)
        bodys1 = []
        bodys2 = []
        for i in range(1, len(syst)):
            if syst[i][7]==0:
                bodys1.append(CosmicBody(syst[i][0], syst[i][1:4], syst[i][4:7], syst[i][7]))
            if syst[i][7]>0:
                bodys2.append(CosmicBody(syst[i][0], syst[i][1:4], syst[i][4:7], syst[i][7]))
        self.exist = bodys1
        self.not_exist = bodys2   
        self.t = syst[0][0]
        self.dt = syst[0][1]
    
    def add(self, t):
        a = self.not_exist.copy()
        for i in a:
            if i.t0 <= t:
                self.exist.append(i)
                remove_arr(self.not_exist, i)
        return self
    
    def destroy(self):
        a = self.exist.copy()
        for i in range(len(a)):
            for j in range(len(a)):
                if i != j and np.all(np.abs(a[i].r - a[j].r)<eps):
                    remove_arr(self.exist, a[i])
                    remove_arr(self.exist, a[j])
        return self
    
    def step(self, t):
        self.add(t)
        self.destroy()
        for j in range(len(self.exist)):
            self.exist[j].gravitate(self.exist)
        return self.exist
    
    def print2(self):
        print(self.exist)
    
    def animation(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        x = []
        y = []
        z = []
        for i in self.exist:
            x.append(abs(i.r[0]))
            y.append(abs(i.r[1]))
            z.append(abs(i.r[2]))

        ax.axes.set_xlim3d(-max(x)-10, max(x)+10)
        ax.axes.set_ylim3d(-max(y)-10, max(y)+10)
        ax.axes.set_zlim3d(-max(z)-10, max(z)+10)

        length = len(self.exist)
        dt1 = self.dt
        t0 = self.t
        n = int(t0/dt1)
        count = -1
        line_x = np.array([0.0]*n*len(self.exist)).reshape(len(self.exist), n)
        line_y = np.array([0.0]*n*len(self.exist)).reshape(len(self.exist), n)
        line_z = np.array([0.0]*n*len(self.exist)).reshape(len(self.exist), n)
        
        for t in tqdm(np.arange(0., t0, dt1)):
            ax.clear()
            count += 1
            ax.axes.set_xlim3d(-max(x)-10, max(x)+10)
            ax.axes.set_ylim3d(-max(y)-10, max(y)+10)
            ax.axes.set_zlim3d(-max(z)-10, max(z)+10)
            
            try:
                for i in range(len(self.exist)):
                    line_x[i][count] = (self.exist[i].r[0])
                    line_y[i][count] = (self.exist[i].r[1])
                    line_z[i][count] = (self.exist[i].r[2])
                    ax.scatter(self.exist[i].r[0], self.exist[i].r[1], self.exist[i].r[2], s=150)
                    t1 = int(self.exist[i].t0/dt1+1)
                    plt.plot(line_x[i][t1:count], line_y[i][t1:count], line_z[i][t1:count])
                
                self.step(t)
            except:
                print('Error')
                
            b = int(abs(len(self.exist)-length))
            c = np.zeros((b, n))
            line_x = np.concatenate((line_x, c))
            line_y = np.concatenate((line_y, c))
            line_z = np.concatenate((line_z, c))
            length = len(self.exist)
            ax.view_init(30, 60)

            fig.canvas.draw()
            # plt.savefig(f'planet\{t}.png', 
            #   transparent = False,  
            #   facecolor = 'white'
            # )
            plt.pause(0.005)
    
                
                

if __name__ == '__main__':
    a = System('planet.txt')
    a.animation()

