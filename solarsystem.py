import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import time
from threading import Thread
import logging

logging.basicConfig(level=logging.WARNING)

G = 10000000  # гравитционная постоянная
dt = 0.0001  # приращение времени
NUMBER_OF_STEPS = 1000  # Колличество шагов
FULL_TIME = NUMBER_OF_STEPS / dt  # все время
FREQUENCY = 0.01  # частота обновления картинки (колличество секунд в анимации на один шаг)


class Body():
    def __init__(self, mass: float, position: np.array, velocity: np.array, size=15, color='orange'):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.color = color
        self.size = size

    def kinematik(self):
        self.position = self.position + dt * self.velocity

    def newton_force(self, body):
        self.velocity = self.velocity + ((dt * G * body.mass * (body.position - self.position)) / pow(
            np.dot((self.position - body.position), (self.position - body.position)), 2))

        logging.debug(repr(self.velocity))

    def iter(self, bodies):
        for body in bodies:
            if body == self:  # проверка, на то, что тело не взаимодействует само с собой
                continue
            self.newton_force(body)
        self.kinematik()

    def paint(self, axes):
        axes.plot3D(self.position[0], self.position[1], self.position[2], marker='o', color=self.color,
                    markersize=self.size)


class Visualisator():
    def __init__(self, bodies):
        self.bodies = bodies
        self.fig = plt.figure()
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


def set_sun_and_earth():
    sun = Body(1000, np.array([0, 0, 0]), np.array([0, 0, 0]))
    earth = Body(1, np.array([0, 0, 100]), np.array([1, 1, 0]), size=2, color='red')
    bodies = [sun, earth]
    return bodies


def next_step(bodies):
    for body in bodies:
        body.iter(bodies)


def loop(bodies, visualisator):
    for i in range(NUMBER_OF_STEPS):
        next_step(bodies)
        time.sleep(FREQUENCY)


def main():
    bodies = set_sun_and_earth()
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
