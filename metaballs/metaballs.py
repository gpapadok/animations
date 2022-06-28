from turtle import shapesize
import numpy as np
import pygame

SIZE = (640, 384)
N_BALLS = 6
DT = .1
SPEED = 15
RGB = (0.5, 0.5, 1.)

class Metaball:
    def __init__(self, rng):
        self.radius = rng.uniform(20, 40)
        self.xpos = rng.uniform(100, 600)
        self.ypos = rng.uniform(100, 300)
        thetaspeed = rng.uniform(0, 2 * np.pi)
        rspeed = SPEED
        self.xspeed = rspeed * np.cos(thetaspeed)
        self.yspeed = rspeed * np.sin(thetaspeed)
    
    def move(self):
        self.xpos = self.xpos + self.xspeed * DT
        self.ypos = self.ypos + self.yspeed * DT
        if self.xpos <= 0 or self.xpos >= SIZE[0]:
            self.xspeed = -self.xspeed
        if self.ypos <= 0 or self.ypos >= SIZE[1]:
            self.yspeed = -self.yspeed

class Isosurface:
    def __init__(self, size, n_balls):
        rng = np.random.default_rng()
        self.balls = [Metaball(rng) for _ in range(n_balls)]
        self.xx = np.tile(np.arange(size[0]), (size[1], 1)).T
        self.yy = np.tile(np.arange(size[1]), (size[0], 1))

    def get_pixels(self):
        intensity = np.zeros_like(self.xx)
        for b in self.balls:
            d = np.sqrt((self.xx - b.xpos) ** 2 + (self.yy - b.ypos) ** 2)
            intensity = intensity + b.radius / d
        surf = np.stack(
                [intensity*RGB[0], intensity*RGB[1], intensity*RGB[2]], axis=2
            ).clip(0, 1)
        return (surf * 255).astype(np.uint8)

    def update(self):
        for b in self.balls:
            b.move()
        return self.get_pixels()

pygame.display.init()
screen = pygame.display.set_mode(size=SIZE)
pygame.display.set_caption("Metaballs")

isosurf = Isosurface(SIZE, N_BALLS)
pixels = isosurf.get_pixels()
pygame.surfarray.blit_array(screen, pixels)
pygame.display.flip()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pixels = isosurf.update()
    pygame.surfarray.blit_array(screen, pixels)
    pygame.display.flip()

pygame.quit()
