import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


class Star:
    def __init__(self, mass: float):
        self.mass = mass
        self.vec_P = np.array([[0.0, 0.0],])


class CosmicBody:
    G = 6.67430e-11
    sec_in_day = 86400

    def __init__(self, mass: float, vec_v: np.ndarray, vec_P: np.ndarray):
        self.mass = mass
        self.vec_v = vec_v
        self.vec_P = vec_P

    def gravitate(self, bodys: list, delta_t: float):
        v = self.vec_v[-1]
        v_delt = np.array([[0.0, 0.0]])

        for affect_bod in bodys:
            r_vec = self.vec_P[-1] - affect_bod.vec_P[-1]
            r = sum(r_vec**2)**0.5

            v_delt += (-self.G * self.mass *
                    affect_bod.mass  *
                    r_vec / r**3) * self.sec_in_day * delta_t / self.mass
            
        r_new = self.vec_P[-1] + (v + v_delt) * self.sec_in_day * delta_t
        self.vec_P = np.append(self.vec_P, r_new, axis=0)
        self.vec_v += v_delt

    def destroy(self, bodys):
        for affect_bod in bodys:
            dist = sum(((self.vec_P[-1] - affect_bod.vec_P[-1])**2))**0.5 
            if dist < 1.75e9:
                return True, affect_bod

Sun = Star(2.0e30)

Earth = CosmicBody(5.972e24,
                    np.array([[0.0, 29765.0]]),
                    np.array([[1.5e11, 0.0]]))
                    
Mercur =  CosmicBody(3.33022e23,
                    np.array([[0.0, 47360.0]]),
                    np.array([[6.9e10, 0.0]]))

all_bodyes = [Sun, Earth, Mercur]

t0 = 0.0
delta_t = 1.0
t = 1000

while t0 < t and len(all_bodyes) > 1:
    for i, body in enumerate(all_bodyes[1:], start=1):
            affect_bodyes = all_bodyes[:i] + all_bodyes[i+1:]
            body.gravitate(affect_bodyes, delta_t)
    t0 += delta_t

fig, ax = plt.subplots(figsize=(8, 8))

earth_point = ax.plot(Earth.vec_P[0][0], Earth.vec_P[0][1], 
                      marker='o', 
                      markersize=6,
                      markeredgecolor="black", 
                      markerfacecolor="blue")[0]

merk_point = ax.plot(Mercur.vec_P[0][0], Mercur.vec_P[0][1], 
                     marker='o', 
                     markersize=4, 
                     markeredgecolor="black",
                     markerfacecolor="gray")[0]

sun_point = ax.plot(Sun.vec_P[0][0], Sun.vec_P[0][0], 
                    marker='o', 
                    markersize=10, 
                    markeredgecolor="black",
                    markerfacecolor="yellow")[0]




def animate(i):
    merk_point.set_data(Mercur.vec_P[i][0], Mercur.vec_P[i][1])
    earth_point.set_data(Earth.vec_P[i][0], Earth.vec_P[i][1])
    ax.set_xlim(-2*1.5e11,2*1.5e11)
    ax.set_ylim(-2*1.5e11,2*1.5e11)
    return earth_point, merk_point


solar_system_animation = animation.FuncAnimation(fig, 
                                                func=animate,
                                                frames = t, 
                                                interval=1)

plt.show()


