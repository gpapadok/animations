import pygame
import numpy as np
import pyximport

pyximport.install()

from purplerain_obj import *


# PURPLE = 0x800080 # RGB  (128, 0, 128)
BG_COLOR = 0xafafaf

pygame.display.init()

screen = pygame.display.set_mode(size=SIZE)
pygame.display.set_caption("Purple Rain")
screen.fill(BG_COLOR)

rain = PurpleRain(screen)
pygame.display.flip()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(BG_COLOR)
    rain.fall()
    pygame.display.flip()

pygame.quit()
