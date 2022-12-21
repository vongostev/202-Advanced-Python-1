import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation


class B_obj:
    """
    Объект большой массы
    Оказывает влияние на другие объекты
    Не испытывает влияние со стороны других объектов
    """

    def __init__(self, mass, R, c, x, y, z):
        """Constructor"""
        self.mass = mass
        self.radius = R
        self.color = c
        self.x = x
        self.y = y
        self.z = z


class M_obj:
    """
    Объект средней массы
    Оказывает влияние на другие объекты
    Испытывает влияние со стороны других объектов
    """

    def __init__(self, mass, R, c, x, y, z, v_x, v_y, v_z):
        """Constructor"""
        self.last_monent = 0  # Номер последнего мгновения жизни
        self.mass = mass
        self.radius = R
        self.color = c
        self.v_x = v_x
        self.v_y = v_y
        self.v_z = v_z
        self.Track = np.array([[x], [y], [z]], dtype=np.float64)

    def Tr_add(self, sz):
        """Увеличение массива точек траектории"""
        self.Track = np.concatenate((self.Track, np.zeros((3, sz))), axis=1, dtype=np.float64)
        self.last_moment = sz

    def destroy(self, i):
        """Вывод объекта из расчетов"""
        self.last_moment = i
        print(self, 'was destroyed')
        print("last_moment =", self.last_moment)


class S_obj:
    """
    Объект малой массы
    Не оказывает влияние на другие объекты
    Испытывает влияние со стороны других объектов
    """

    def __init__(self, c, x, y, z, v_x, v_y, v_z):
        """Constructor"""
        self.color = c
        self.last_monent = 0
        self.x = x
        self.y = y
        self.z = z
        self.v_x = v_x
        self.v_y = v_y
        self.v_z = v_z
        self.Track = np.array([[x], [y], [z]], dtype=np.float64)

    def Tr_add(self, sz):
        """Увеличение массива точек траектории"""
        self.Track = np.concatenate((self.Track, np.zeros((3, sz))), axis=1, dtype=np.float64)
        self.last_monent = sz

    def destroy(self, i):
        """Вывод объекта из расчетов"""
        self.last_moment = i
        print(self, 'was destroyed')
        print("last_moment =", self.last_moment)


if __name__ == '__main__':

    # Значения переменных
    G_CONST = 0.1  # Гравитационная постоянная
    dt = 0.05  # Длина шага по времени
    N = 1000  # Количество шагов

    # Примеры объектов
    sun = B_obj(10000, 5, '#fa5004', 0, 0, 0)
    star_1 = M_obj(1000, 4, '#ff3333', 10, 0, 0, 0, 1.5, 0)
    star_2 = M_obj(1000, 4, '#291b4f', -10, 0, 0, 0, -1.5, 0)
    earth = M_obj(60, 2, '#0000e6', 30, 0, 0, 0, 6, 0)
    moon = M_obj(0.00000005, 0.1, '#808080', 33, 0, 0, 0, 4.5, 0)
    mars = M_obj(30, 1, '#9a0000', 20, 0, 0, 0, 8, 0)
    venus = M_obj(35, 1, '#ff0000', 10, 0, 0, 0, 11, 0)

    # Массивы тел
    B_array = [sun]
    M_array = [earth, mars, moon, venus]
    S_array = []

    # Предварительное изменение массивов
    for sub in M_array:
        sub.Tr_add(N)
    for sub in S_array:
        sub.Tr_add(N)

    # Вычисление траекторий
    start_time = time.time()
    for i in range(N):
        for sub in M_array:
            if (i < sub.last_moment):
                a_x = 0
                a_y = 0
                a_z = 0
                for obj in B_array:
                    x = obj.x-sub.Track[0, i]
                    y = obj.y-sub.Track[1, i]
                    z = obj.z-sub.Track[2, i]
                    r_sq = (x**2)+(y**2)+(z**2)
                    if r_sq**0.5 <= sub.radius+obj.radius:  # условие уничтожения
                        sub.destroy(i)
                    a_by_obj = obj.mass*G_CONST/r_sq
                    a_x += a_by_obj*x/(r_sq**0.5)
                    a_y += a_by_obj*y/(r_sq**0.5)
                    a_z += a_by_obj*z/(r_sq**0.5)
                for obj in M_array:
                    if (obj != sub) and (i < obj.last_moment):
                        x = obj.Track[0, i]-sub.Track[0, i]
                        y = obj.Track[1, i]-sub.Track[1, i]
                        z = obj.Track[2, i]-sub.Track[2, i]
                        r_sq = (x**2+y**2+z**2)
                        if r_sq**0.5 <= sub.radius+obj.radius:
                            sub.destroy(i)
                            obj.destroy(i)
                        a_by_obj = obj.mass*G_CONST/r_sq
                        a_x += a_by_obj*x/(r_sq**0.5)
                        a_y += a_by_obj*y/(r_sq**0.5)
                        a_z += a_by_obj*z/(r_sq**0.5)
                sub.Track[0, i+1] = sub.Track[0, i] + sub.v_x*dt + a_x*dt*dt/2
                sub.Track[1, i+1] = sub.Track[1, i] + sub.v_y*dt + a_y*dt*dt/2
                sub.Track[2, i+1] = sub.Track[2, i] + sub.v_z*dt + a_z*dt*dt/2
                sub.v_x += a_x*dt
                sub.v_y += a_y*dt
                sub.v_z += a_z*dt

        # for sub in S_array:

    # Время вычисления траекторий
    end_time = time.time()
    calc_time = end_time - start_time
    print('calc_time =', calc_time)

    # Построение траекторий
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(projection='3d')
    """
    ax.set_title('3D line plot')
    ax.set(xlim3d=(-30, 30), xlabel='X')
    ax.set(ylim3d=(-30, 30), ylabel='Y')
    ax.set(zlim3d=(-30, 30), zlabel='Z')

    # Линии следа
    lines = [ax.plot([], [], [], c=obj.color, lw=1)[0] for obj in M_array]
    walks = np.array([obj.Track for obj in M_array])

    # Точки объектов большой массы
    B_scat = ax.scatter([obj.x for obj in B_array],
                        [obj.y for obj in B_array],
                        [obj.z for obj in B_array],
                        s=[obj.radius for obj in B_array],
                        c=[obj.color for obj in B_array])

    # Точки объектов средней массы
    M_scat = ax.scatter([obj.Track[0, 0] for obj in M_array],
                        [obj.Track[1, 0] for obj in M_array],
                        [obj.Track[2, 0] for obj in M_array],
                        s=[obj.radius for obj in M_array],
                        c=[obj.color for obj in M_array])

    # Точки объектов малой массы
    """

    def init():
        ax.clear()

    def update(num):
        """
        M_scat.set_offsets([obj.Track[0, num],
                            obj.Track[1, num],
                            obj.Track[2, num]] for obj in M_array)
        for line, walk in zip(lines, walks):
            line.set_data(walk[:2, :num+1])
            line.set_3d_properties(walk[2, :num+1])
        return lines
        """

        ax.clear()
        ax.set_box_aspect(aspect=(1, 1, 1))
        ax.set(xlabel='X')
        ax.set(ylabel='Y')
        ax.set(zlabel='Z')
        k = 3.5  # Имперический коэффициент площади точек scatter'а
        """
        figsize=(8,8) lim = 20   k = 7
        figsize=(8,8) lim = 40   k = 3.5
        """
        lim = 40
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_zlim(-lim, lim)
        ax.scatter([obj.x for obj in B_array],
                   [obj.y for obj in B_array],
                   [obj.z for obj in B_array],
                   s=[3.14*((k*obj.radius)**2) for obj in B_array],
                   c=[obj.color for obj in B_array])
        for obj in M_array:
            if (num <= obj.last_moment):
                ax.scatter(obj.Track[0, num],
                           obj.Track[1, num],
                           obj.Track[2, num],
                           c=obj.color,
                           s=3.14*((k*obj.radius)**2))
                ax.plot(obj.Track[0, :num+1],
                        obj.Track[1, :num+1],
                        obj.Track[2, :num+1],
                        c=obj.color, lw=2)
            else:
                ax.plot(obj.Track[0, :obj.last_moment+1],
                        obj.Track[1, :obj.last_moment+1],
                        obj.Track[2, :obj.last_moment+1],
                        c=obj.color, lw=2)

    ani = FuncAnimation(fig, update,  N, init_func=init, interval=1)
    # ani.save('sistem.gif', dpi=100, fps=60, writer='ffmpeg')
    # plt.close()
