import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import time
from threading import Thread
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(message)s")

G = 1000  # гравитционная постоянная
dt = 0.01  # приращение времени
NUMBER_OF_STEPS = 10000  # Колличество шагов
FULL_TIME = NUMBER_OF_STEPS / dt  # все время
FREQUENCY = 0.001  # частота обновления картинки (колличество секунд в анимации на один шаг)


class Body():
    def __init__(self, mass: float, position: np.array, velocity: np.array, size=15, color='orange', name='sun'):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.color = color
        self.size = size
        self.acceleration = 0
        self.name = name

    def calculate_delta_position(self):
        self.position = self.position + dt * self.velocity + self.acceleration * dt * dt / 2
        self.acceleration = 0
        logging.debug("позиция" + self.name + repr(self.position))

    def calculate_delta_velocity(self):
        self.velocity = self.velocity + dt * self.acceleration
        logging.debug("скорость" + self.name + repr(self.velocity))

    def calculate_acceleration(self, body):
        r = body.position - self.position
        R = pow(np.dot(r, r), 1.5)
        if R > 0:
            self.acceleration = self.acceleration + (G * body.mass * r) / R

    def iter(self, bodies):
        for body in bodies:
            if body == self:  # проверка, на то, что тело не взаимодействует само с собой
                continue
            self.calculate_acceleration(body)

        logging.debug("ускорение" + self.name + repr(self.acceleration))

        self.calculate_delta_velocity()
        self.calculate_delta_position()

    def paint(self, axes):
        axes.plot3D(self.position[0], self.position[1], self.position[2], marker='o', color=self.color,
                    markersize=self.size)


class Visualisator():
    def __init__(self, bodies):
        self.bodies = bodies
        self.fig = plt.figure()
        self.axes = plt.axes(projection='3d')
        self.axes.set_xlabel('X')
        self.axes.set_ylabel('Y')
        self.axes.set_zlabel('Z')

    def paint(self, i):
        for body in self.bodies:
            body.paint(self.axes)

    def animate(self, interval=FREQUENCY * 1000):
        ani = animation.FuncAnimation(self.fig, self.paint, interval=interval)
        plt.show()


def set_solar_system():
    sun = Body(100000, np.array([0, 0, 0]), np.array([0, 0, 0]))
    earth = Body(1, np.array([0, 0, 1600]), np.array([250, 0, 0]), size=2, color='blue', name='earth')
    mars = Body(1, np.array([2771, 0, 1600]), np.array([129, 0, -75]), size=2, color='red', name='mars')
    nebula = Body(1, np.array([0, 2200, 2200]), np.array([0, 75, -75]), size=2, color='black', name='nebula')
    bodies = [sun, earth, mars, nebula]
    return bodies


def set_two_sun():
    sun1 = Body(1000, np.array([0, 0, 0]), np.array([-55, 10, 0]), size=5, name='sun1')
    sun2 = Body(1000, np.array([0, 0, 200]), np.array([55, 10, 0]), size=5, color='red', name='sun2')
    bodies = [sun1, sun2]
    return bodies


def set_three_planet():
    planet1 = Body(1000, np.array([0, 0, 0]), np.array([-55, 0, 0]), size=5, color='black', name='planet1')
    planet2 = Body(1000, np.array([0, 0, 200]), np.array([55, 0, 0]), size=5, color='blue', name='planet2')
    planet3 = Body(1000, np.array([173, 0, 100]), np.array([0, 60, 30]), size=5, color='red', name='planet3')
    bodies = [planet1, planet2, planet3]
    return bodies


def next_step(bodies):
    for body in bodies:
        body.iter(bodies)


def loop(bodies, visualisator):
    for i in range(NUMBER_OF_STEPS):
        next_step(bodies)
        logging.debug(f"шаг {i}")
        time.sleep(FREQUENCY)


def main():
    #    bodies = set_solar_system()           #тут происходит выбор сценария
    #    bodies = set_two_sun()                  #в каждом сценарии свои конфигурации
    bodies = set_three_planet()  # константы общие (мне лень инкапсулировать это, а вообще каждый сценарий лучше завернуть в класс)

    visualisator = Visualisator(bodies)
    t1 = Thread(target=loop, args=(bodies, visualisator,))
    t2 = Thread(target=visualisator.animate)
    t1.start()
    t2.start()


def test():
    M = set_sun_and_earth()
    logging.debug(repr(M))
    next_step(M)


if __name__ == "__main__":
    main()
# test()
