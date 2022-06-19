# PGL is a game library for python based on the module pygame, but designed to be easier to use
import pygame
import entity
from window import *
from physics import *
from time import time

win = pygame.display.set_mode((600, 600))

entity1 = entity.Entity(entity.IMAGE_TYPE, [100, 100], [100, 100], (0, 0, 0), 0, pygame.image.load('img.png'), 0)

old_time = time()
while True:
    dt = time() - old_time
    old_time = time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    win.fill((255, 255, 255))

    entity1.main(win, dt)

    Window.update()