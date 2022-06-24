from abc import abstractclassmethod
import pygame
from pgl.entity import *
import os 

def draw_regular_polygon(surface, color, vertex_count, radius, position, width=0):
    n, r = vertex_count, radius
    x, y = position
    pygame.draw.polygon(surface, color, [
        (x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n))
        for i in range(n)
    ], width)

class Window:
    def __init__(self, dimensions, title, icon=pygame.image.load(f'{os.path.dirname(os.path.realpath(__file__))}/icon.png'), flags=0, depth=0, display=0, vsync=0):
        self.win = pygame.display.set_mode(dimensions, flags, depth, display, vsync)
        pygame.display.set_caption(title)
        pygame.display.set_icon(icon)
        
    def draw(self, entity):
        type = entity.type

        if type == LINE_TYPE:
            pygame.draw.line(self.win, entity.color, entity.pos, (entity.pos[0] + entity.scale[0], entity.pos[1] + entity.scale[1]), entity.thickness)
        if type == CIRCLE_TYPE:
            pygame.draw.circle(self.win, entity.color, entity.pos, entity.scale, entity.thickness)
        if type == SQUARE_TYPE:
            pygame.draw.rect(self.win, entity.color, pygame.Rect(entity.pos, entity.scale), entity.thickness)
        if type == PENTAGON_TYPE:
            draw_regular_polygon(self.win, entity.color, 5, entity.scale, entity.pos, entity.thickness)
        if type == HEXAGON_TYPE:
            draw_regular_polygon(self.win, entity.color, 6, entity.scale, entity.pos, entity.thickness)
        if type == IMAGE_TYPE:
            rotated_image = pygame.image.flip(pygame.transform.rotate(pygame.transform.scale(entity.sprite, entity.scale), entity.rot), (entity.rotX, entity.rotY))
            new_rect = rotated_image.get_rect(center = entity.sprite.get_rect(center = (entity.pos[0], entity.pos[1])).center)
            self.win.blit(rotated_image, new_rect)
        
    def fill(self, color):
        self.win.fill(color)
    
    @abstractclassmethod
    def update(self):
        pygame.display.update()