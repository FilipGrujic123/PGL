import pygame
from math import *
from physics import *

LINE_TYPE = 0
CIRCLE_TYPE = 1
TRIAGLE_TYPE = 2
SQUARE_TYPE = 3
PENTAGON_TYPE = 4
HEXAGON_TYPE = 5
IMAGE_TYPE = 6

def draw_regular_polygon(surface, color, vertex_count, radius, position, width=0):
    n, r = vertex_count, radius
    x, y = position
    pygame.draw.polygon(surface, color, [
        (x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n))
        for i in range(n)
    ], width)

class Entity():
    def __init__(self, type, pos, scale, color=(255, 255, 255), thickness=0, sprite=None, rot=0, mass=1):
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
    
    def apply_force(self, forceX, forceY, dt):
        self.acceleration[0] += forceX / self.mass * dt
        self.acceleration[1] += forceY / self.mass * dt

    def main(self, win, dt):
        if self.enabled:
            # Physics
            self.acceleration[0] += self.jerk[0] * dt
            self.acceleration[1] += self.jerk[1] * dt

            self.speed[0] += self.acceleration[0] * dt
            self.speed[1] += self.acceleration[1] * dt

            self.pos[0] += self.speed[0] * dt
            self.pos[1] += self.speed[1] * dt

            self.apply_force(0, get_gravity() * self.mass, dt)

            # Drawing
            if self.type == LINE_TYPE:
                pygame.draw.line(win, self.color, self.pos, (self.pos[0] + self.scale[0], self.pos[1] + self.scale[1]), self.thickness)
            if self.type == CIRCLE_TYPE:
                pygame.draw.circle(win, self.color, self.pos, self.scale, self.thickness)
            if self.type == SQUARE_TYPE:
                pygame.draw.rect(win, self.color, pygame.Rect(self.pos, self.scale), self.thickness)
            if self.type == PENTAGON_TYPE:
                draw_regular_polygon(win, self.color, 5, self.scale, self.pos, self.thickness)
            if self.type == HEXAGON_TYPE:
                draw_regular_polygon(win, self.color, 6, self.scale, self.pos, self.thickness)
            if self.type == IMAGE_TYPE:
                win.blit(pygame.transform.rotate(pygame.transform.scale(self.sprite, self.scale), self.rot), self.pos)