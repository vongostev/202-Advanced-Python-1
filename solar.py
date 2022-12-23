# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 13:52:40 2022

@author: galin
"""

import numpy as np
import matplotlib.pyplot as plt
import math
import itertools
from matplotlib import animation
from tqdm import tqdm
%matplotlib notebook

class SolarSystem:
    def __init__(self, size):
        self.size = size
        self.bodies = []

        self.fig, self.ax = plt.subplots(
            1,
            1,
            subplot_kw={"projection": "3d"},
            figsize=(self.size / 50, self.size / 50),
        )
        self.fig.tight_layout()

    def add_body(self, body):
        self.bodies.append(body)
        
    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()
    def draw_all(self):
        self.ax.set_xlim((-self.size / 2, self.size / 2))
        self.ax.set_ylim((-self.size / 2, self.size / 2))
        self.ax.set_zlim((-self.size / 2, self.size / 2))
        plt.pause(0.01)
        self.ax.clear()
        
        
    def calculate_all_body_interactions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:
                first.accelerate_due_to_gravity(second)
        
        

class SpaceBody:
    min_display_size = 10
    display_log_base = 1.3
    def __init__(
        self,
        solar_system,
        mass,
        position=(0, 0, 0),
        velocity=[0, 0, 0],
    ):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
        )
        self.colour = "black"
        self.solar_system.add_body(self)
    def move(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
            self.position[2] + self.velocity[2],
        )
    def draw(self):
        self.solar_system.ax.plot(
            *self.position,
            marker="o",
            markersize=self.display_size,
            color=self.colour
        )
    def accelerate_due_to_gravity(self, other):
        distance = other.position - self.position
        distance_mag = distance.get_magnitude()
        force_mag = self.mass * other.mass / (distance_mag ** 2)
        force = distance.normalize() * force_mag
        reverse = 1
        for body in self, other:
            acceleration = force / body.mass
            body.velocity += acceleration * reverse
            reverse = -1
class Sun(SpaceBody):
    def __init__(
        self,
        solar_system,
        mass=10_000,
        position=(0, 0, 0),
        velocity=(0, 0, 0),
    ):
        super(Sun, self).__init__(solar_system, mass, position, velocity)
        self.colour = "yellow"
class Planet(SpaceBody):
    colours = itertools.cycle([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    def __init__(
        self,
        solar_system,
        mass=10,
        position=(0, 0, 0),
        velocity=(0, 0, 0),
    ):
        super(Planet, self).__init__(solar_system, mass, position, velocity)
        self.colour = next(Planet.colours)
        

        
solar_system = SolarSystem(400)
sun = Sun(solar_system)
planets = (
    Planet(
        solar_system,
        position=(60, 50, 0),
        velocity=(0, 5, 5),
    ),
    Planet(
        solar_system,
        mass=20,
        position=(30, 55, 4),
        velocity=(5, 0, 0)
    )
)
t0=4
dt=0.02

for t in tqdm(np.arange(0.,t0,dt)):
    angle=60+60*t/dt
    solar_system.draw_all()
    solar_system.update_all()
    solar_system.fig.canvas.draw()