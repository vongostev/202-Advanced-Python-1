import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


class Star:
    def __init__(self, mass: float):
        self.mass = mass
        self.vec_P = np.array([[0.0, 0.0, 0.0],])


class CosmicBody:
    G = 6.67430e-11
    sec_in_day = 86400

    def __init__(self, mass: float, vec_v: np.ndarray, vec_P: np.ndarray):
        self.mass = mass
        self.vec_v = vec_v
        self.vec_P = vec_P

    def gravitate(self, bodys: list, t0: float):
        v = self.vec_v[-1]
        v_delt = np.array([[0.0, 0.0, 0.0]])

        for affect_bod in bodys:
            r_vec = self.vec_P[-1] - affect_bod.vec_P[-1]
            r = sum(r_vec**2)**0.5

            v_delt += (-self.G * self.mass *
                    affect_bod.mass  *
                    r_vec / r**3) * self.sec_in_day * t0 / self.mass
            
        r_new = self.vec_P[-1] + (v + v_delt) * self.sec_in_day * t0
        self.vec_P = np.append(self.vec_P, r_new, axis=0)
        self.vec_v += v_delt

    def destroy(self, bodys):
        for affect_bod in bodys:
            if sum(((self.vec_P[-1] - affect_bod.vec_P[-1])**2))**0.5 < 1.75e9:
                return True, affect_bod


def random_vec():
    neg_or_pos = [1 if np.random.random() > 0.5 
                    else -1 for _ in range(3)]

    return np.random.rand(1, 3) * neg_or_pos

Sun = Star(2.5e31)

first_body = CosmicBody(np.random.random() * 1.0e29,
                        random_vec()*1.0e4,
                        random_vec()*5.0e11)

all_bodyes = [Sun, first_body]
bodyes_for_plot = [{first_body: 1}]

t0 = 0.0
delta_t = 1.0
t = 365

while t0 < t and len(all_bodyes) > 1:
    for i, body in enumerate(all_bodyes[1:], start=1):
            affect_bodyes = all_bodyes[:i] + all_bodyes[i+1:]
            body.gravitate(affect_bodyes, delta_t)
            destroy = body.destroy(affect_bodyes)
            if destroy:
                all_bodyes.remove(body)
                if destroy[1] is not Sun:
                    all_bodyes.remove(destroy[1])
    bodyes_for_plot += [{body: body.vec_P.shape[0] for body in all_bodyes[1:]}]
    if np.random.random() > 0.9:
        new_body = CosmicBody(np.random.random() * 1.0e29,
                        random_vec()*5.0e4,
                        random_vec()*5.0e11)
        all_bodyes.append(new_body)
    

    t0 += delta_t



fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(projection="3d")


ploted_bodyes = {}
def animate(i):
    global ploted_bodyes
    for body in bodyes_for_plot[i]:
        index = bodyes_for_plot[i][body]
        coord = body.vec_P
        if body not in ploted_bodyes:
            ploted_bodyes[body] = (ax.plot(coord[index-1][0], coord[index-1][1], coord[index-1][2],
                                            marker='o', 
                                            markersize=6,
                                            markeredgecolor="black", 
                                            markerfacecolor="black")[0],
                                   ax.plot([], [], [], '-g',
                                            lw=0.2, 
                                            c="blue")[0])
        else:
            ploted_bodyes[body][0].set_data_3d(coord[index-1][0], coord[index-1][1], coord[index-1][2])
            ploted_bodyes[body][1].set_data_3d(coord[:index, 0], coord[:index, 1], coord[:index, 2])

        for remove_el in set(ploted_bodyes) - set(bodyes_for_plot[i]):
            remove_plot = ploted_bodyes.pop(remove_el)
            remove_plot[0].remove()
            remove_plot[1].remove()
            
    sun_point = ax.plot([0], [0], [0],
                    marker='o', 
                    markersize=10, 
                    markeredgecolor="black",
                    markerfacecolor="yellow")[0]

    ax.set(xlim3d=(-1.2*5.0e11, 1.2*5.0e11), xlabel='X')
    ax.set(ylim3d=(-1.2*5.0e11, 1.2*5.0e11), ylabel='Y')
    ax.set(zlim3d=(-1.2*5.0e11, 1.2*5.0e11), zlabel='Z')
    return (sun_point,) + tuple(ploted_bodyes.values())


solar_system_anim = animation.FuncAnimation(fig, 
                                            func=animate,
                                            frames = len(bodyes_for_plot), 
                                            interval=1)

plt.show()