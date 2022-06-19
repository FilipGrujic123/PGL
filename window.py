from abc import abstractclassmethod
import pygame
from entity import *

class Window:
    def __init__(self, dimensions, flags=0, depth=0, display=0, vsync=0):
        self.win = pygame.display.set_mode(dimensions, flags, depth, display, vsync)
        
    def draw(self, entity):
        pass
    
    @abstractclassmethod
    def update(self):
        pygame.display.update()