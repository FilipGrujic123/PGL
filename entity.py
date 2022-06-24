from copyreg import remove_extension
import pygame
from math import *
from pgl.physics import *

LINE_TYPE = 0
CIRCLE_TYPE = 1
TRIAGLE_TYPE = 2
SQUARE_TYPE = 3
PENTAGON_TYPE = 4
HEXAGON_TYPE = 5
IMAGE_TYPE = 6

class Entity():
    def __init__(self, type, pos, scale, color=(255, 255, 255), thickness=0, sprite=None, rot=0, mass=1, rotX=False, rotY=False):
        self.type = type
        self.pos = pos
        self.sprite = sprite
        self.jerk = [0, 0]
        self.acceleration = [0, 0]
        self.speed = [0, 0]
        self.pos = pos
        self.scale = scale
        self.enabled = True
        self.color = color
        self.thickness = thickness
        self.rot = rot
        self.mass = mass
        self.rotX = rotX,
        self.rotY = rotY
    
    def apply_force(self, forceX, forceY, dt):
        self.acceleration[0] += forceX / self.mass * dt
        self.acceleration[1] += forceY / self.mass * dt
    
    def flip(self, flipX, flipY):
        self.rotX = flipX
        self.rotY = flipY

    def main(self, win, dt):
        if self.enabled:
            # Physics
            self.acceleration[0] += self.jerk[0] * dt
            self.acceleration[1] += self.jerk[1] * dt

            self.speed[0] += self.acceleration[0] * dt
            self.speed[1] += self.acceleration[1] * dt

            self.pos[0] += self.speed[0] * dt
            self.pos[1] += self.speed[1] * dt

            self.apply_force(0, Physics.get_gravity() * self.mass, dt)

            if not self.speed[0] == 0:
                self.speed[0] -= (self.speed[0] / abs(self.speed[0])) * FRICTION * dt
            if not self.speed[1] == 0:
                self.speed[1] -= (self.speed[1] / abs(self.speed[1])) * FRICTION * dt

            # Drawing
            win.draw(self)