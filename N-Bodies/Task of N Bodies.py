# Программа для численного решения задачи N тел.
# Версия 1.0 (альфа).

# На вход принимает 2 сsv-файла и адрес вывода:
# первый отвечает за конфигурацию видео,
# второй -- за входные данные рассчёта.
# При запуске сначала производит расчёт и выводит данные по шагам в csv-файл
# по адресу вывода. Затем производит визуализацию из файла.
# Сначала прокручивает анимацию, затем выводит траектории.
# Перед свёртыванием окна траекторий и переходам к следующим инструкциям
# ЖДЁТ 20 СЕКУНД -- подождите, это задумано.

# Проводит тесты на то, что объект вообще создаётся, что уничтожается и что
# взаимодействие имеет правильный знак. Также предлагает тест-видео и
# основную анимацию.

# О правильном завершении программы свидетельствует несколько
# провакационная фраза в самом конце сообщений в консоль.

# Программа также пытается настроить размер тел на соответствующий радиусу колизии
# и размерам окна. Делает она это, вероятно, слишком грубо, в связи с чем, прошу
# не измдеваться над ней масштабами по осям, отличающимися более двух порядков  --
# -- результат будет не очень правдоподобный.


import time
import matplotlib.pyplot as plt
import csv
import numpy as np
import matplotlib
matplotlib.use("TkAgg")

# Class for Planets, ... having the F~1/r^2 interaction law


class Particle ():
    # Переменные основные
    name: str
    m: float  # μ = Gm -> m
    R: float  # Collision radius
    t_0: int  # Activation STEP
    r: np.ndarray  # (r1, r2, r3)^T -- coordinaates
    v: np.ndarray  # (v1, v2, v3)^T -- speed
    # Переменные служебные
    a: np.ndarray  # (a1, a2, a3)^T -- acceleration
    is_active: bool  # Activation key
    is_destroyed: bool  # Destruction key
    # Инициализация

    def __init__(self, Name: str, mass: float, Rad: float, time_0: float, rad: np.ndarray, vel: np.ndarray):
        self.name = Name
        self.m = mass
        self.R = Rad
        self.t_0 = time_0
        self.r = rad
        self.v = vel
        self.a = np.array([float(0), float(0), float(0)])
        self.is_active = False
        self.is_destroyed = False
    # IO4

    def data(self, s: str):
        if s == 'name':
            return self.name
        if s == 'm':
            return self.mass
        if s == 'R':
            return self.R
        if s == 't_0':
            return self.t_0
        if s == 'r':
            return self.r
        if s == 'v':
            return self.v

    def output(self, l: list):
        if self.is_active == True:
            l.append([self.name, self.R, self.r[0], self.r[1], self.r[2]])
        return l
    # Service

    def rho(self, b):
        return np.dot(self.r-b.r, self.r - b.r)**0.5
    # Creation

    def create(self, n: int):
        if (self.is_active == False) and (n == self.t_0):
            self.is_active = True
    # Destruction

    def mark_for_destroy(self, b):
        if (self.is_active == True) and (b.is_active == True) and (b != self) and (self.rho(b) <= (self.R + b.R)):
            self.is_destroyed = True

    def destroy(self):
        if (self.is_active == True) and (self.is_destroyed == True):
            self.is_active = False
    # Dynamic

    def enforce(self, b):
        if (self.is_active == True) and (b.is_active == True) and (b != self):
            self.a += b.m*(b.r - self.r)/self.rho(b)**3
    # Kinematic

    def move(self, T: float):
        if self.is_active == True:
            self.r += T*self.v + 0.5*T*T*self.a
            self.v += T*self.a
            self.a[0] = 0
            self.a[1] = 0
            self.a[2] = 0
# The system of previous class objects. Turns on interactions, collision, etc.


class System ():
    # Переменные основные
    T: float  # Step time
    n: int  # Current step
    N: int  # End step
    particles: list  # Content

    def __init__(self, path_data: str):
        self.n = 0
        self.particles = []
        with open(path_data, newline='') as file:
            reader = csv.reader(file)
            k_0 = False
            k_1 = False
            k_2 = False
            for row in reader:
                if k_0 == False:
                    k_0 = True
                elif k_1 == False:
                    k_1 = True
                    self.T = float(row[0])
                    self.N = int(round(float(row[1])/self.T))
                elif k_2 == False:
                    k_2 = True
                else:
                    if (row[0] == '@Step_start'):
                        raise ValueError(
                            'Name "@Step_start" is reserved and not allowed.')
                    if (row[0] == '@Step_end'):
                        raise ValueError(
                            'Name "@Step_end" is reserved and not allowed.')
                    self.particles.append(
                        Particle(
                            row[0],
                            float(row[1]),
                            float(row[2]),
                            int(float(row[3])/self.T),
                            np.array(
                                [float(row[4]), float(row[5]), float(row[6])]),
                            np.array(
                                [float(row[7]), float(row[8]), float(row[9])])
                        )
                    )

    def output(self):
        l = []
        for p in self.particles:
            l = p.output(l)
        return l

    def create(self, n: int):
        for p in self.particles:
            p.create(n)

    def destroy(self):
        for a in self.particles:
            for b in self.particles:
                a.mark_for_destroy(b)
        for p in self.particles:
            p.destroy()

    def enforce(self):
        for a in self.particles:
            for b in self.particles:
                a.enforce(b)

    def move(self):
        for p in self.particles:
            p.move(self.T)
        self.n += 1

    def movement(self, path_out):
        with open(path_out, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['@Step_start', str(0*self.T)])
            self.create(0)
            self.destroy()
            for p in self.output():
                writer.writerow(p)
            writer.writerow(['@Step_end'])
            for n in range(1, self.N+1, 1):
                self.enforce()
                self.move()
                self.create(n)
                self.destroy()
                writer.writerow(['@Step_start', str(n*self.T)])
                for p in self.output():
                    writer.writerow(p)
                writer.writerow(['@Step_end'])
# The main class


class Model ():
    # Переменные основные
    T_visual: float  # Slide time
    path_out: str  # Output path for simulation data
    # Переменные служебные
    fig: plt.figure
    ax: plt.axes
    limits: list = [-1., 1., -1., 1., -1., 1.]
    time_accuracy: int
    s_0: float

    def __init__(self, path_config: str, path_output: str):
        with open(path_config, newline='') as file:
            reader = csv.reader(file)
            k = False
            for row in reader:
                if k == False:
                    k = True
                else:
                    self.T_visual = 1/float(row[0])
                    self.time_accuracy = int(row[3])
                    self.s_0 = 3.1416/4 * \
                        (min(float(row[1]), float(row[2]))/2.54*72.0)**2
                    self.fig = plt.figure(
                        figsize=(float(row[1])/2.54, float(row[2])/2.54))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.path_out = path_output

    def limit_axes(self):
        with open(self.path_out, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if (row[0] != '@Step_start') and (row[0] != '@Step_end'):
                    if self.limits[0] > float(row[2]):
                        self.limits[0] = float(row[2])
                    if self.limits[1] < float(row[2]):
                        self.limits[1] = float(row[2])
                    if self.limits[2] > float(row[3]):
                        self.limits[2] = float(row[3])
                    if self.limits[3] < float(row[3]):
                        self.limits[3] = float(row[3])
                    if self.limits[4] > float(row[4]):
                        self.limits[4] = float(row[4])
                    if self.limits[5] < float(row[4]):
                        self.limits[5] = float(row[4])
            self.s_0 = self.s_0 / \
                ((self.limits[1]-self.limits[0]+self.limits[3] -
                 self.limits[2]+self.limits[5]-self.limits[4])/3)**2

    def simulate(self, path_data: str):
        system = System(path_data)
        system.movement(self.path_out)
        self.limit_axes()

    def show_motion(self):
        with open(self.path_out, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == '@Step_start':
                    self.ax.clear()
                    legend = []
                    t = float(row[1])
                elif row[0] == '@Step_end':
                    self.ax.axes.set_xlim3d(self.limits[0], self.limits[1])
                    self.ax.axes.set_ylim3d(self.limits[2], self.limits[3])
                    self.ax.axes.set_zlim3d(self.limits[4], self.limits[5])
                    self.ax.legend(legend)
                    self.fig.suptitle(f'Motion. t ={t:.{self.time_accuracy}f}')
                    self.fig.canvas.draw()
                    self.fig.canvas.flush_events()
                    time.sleep(self.T_visual)
                else:
                    self.ax.scatter(float(row[2]), float(row[3]), float(
                        row[4]), s=self.s_0*float(row[1]))
                    legend.append(row[0])

    def show_trajectories(self):
        self.ax.clear()
        legend = []
        with open(self.path_out, newline='') as file:
            names = set()
            reader = csv.reader(file)
            for row in reader:
                names.add(row[0])
        names.remove('@Step_start')
        names.remove('@Step_end')
        while(len(names) > 0):
            name = names.pop()
            with open(self.path_out, newline='') as file:
                reader = csv.reader(file)
                x = []
                y = []
                z = []
                for row in reader:
                    if row[0] == name:
                        k = float(row[1])
                        x.append(float(row[2]))
                        y.append(float(row[3]))
                        z.append(float(row[4]))
                x = np.array(x)
                y = np.array(y)
                z = np.array(z)
                self.ax.scatter(x, y, z, s=self.s_0*k)
                legend.append(name)
        self.ax.axes.set_xlim3d(self.limits[0], self.limits[1])
        self.ax.axes.set_ylim3d(self.limits[2], self.limits[3])
        self.ax.axes.set_zlim3d(self.limits[4], self.limits[5])
        self.ax.legend(legend)
        self.fig.suptitle('Trajectories')
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


def show(path_config: str, path_data: str, path_output: str):
    print(
        f'Simulation {path_config}-{path_data}-{path_output} has been started.')
    model = Model(path_config, path_output)
    model.simulate(path_data)
    model.fig.show()
    time.sleep(1)
    model.show_motion()
    time.sleep(1)
    model.show_trajectories()
    time.sleep(20)
    plt.close(model.fig)
    print(
        f'Simulation {path_config}-{path_data}-{path_output} has been ended.')


def creation_test():
    p = Particle('Gostev', 10, 1, 0, np.array(
        [1., 1., 1.]), np.array([0., 0., 0.]))
    if p.data('name') == 'Gostev':
        return True
    else:
        return False


def destruction_test(path_out: str):
    with open(path_out, newline='') as file:
        reader = csv.reader(file)
        k_1 = True
        k_2 = True
        for row in reader:
            if (k_1 == True):
                if row[0] == '@Step_start':
                    if float(row[1]) > 3.0:
                        k_1 = False
            elif row[0] == 'Nirn':
                k_2 = False
        return k_2


def interaction_test(path_out: str):
    with open(path_out, newline='') as file:
        reader = csv.reader(file)
        k_1 = True
        k_2 = True
        k_3 = True
        for row in reader:
            if (row[0] == 'Lorkhan') and (k_1 == True):
                k_1 = False
                x_1 = float(row[2])
                y_1 = float(row[3])
                z_1 = float(row[4])
            elif (row[0] == 'Lorkhan') and (k_2 == True):
                k_2 = False
                x_2 = float(row[2])
                y_2 = float(row[3])
                z_2 = float(row[4])
            elif (row[0] == 'Lorkhan') and (k_3 == True):
                k_3 = False
                x_3 = float(row[2])
                y_3 = float(row[3])
                z_3 = float(row[4])
        return (x_1 > x_2) and (x_2 > x_3) and (y_1 > y_2) and (y_2 > y_3) and (z_1 > z_2) and (z_2 > z_3)


if __name__ == '__main__':

    assert creation_test()
    show('./Config.csv', './data-test.csv', './Output-test.csv')
    assert destruction_test('./Output-test.csv')
    assert interaction_test('./Output-test.csv')
    show('./Config.csv', './data.csv', './Output.csv')

    print('Die, heathen!')
