import numpy as np
import pygame

DT = .15
SIZE = (1024, 640)
SIZE = [dim * 2/3 for dim in SIZE]

class PurpleDrop(object):
    purple = 0x800080
    min_length = 10
    max_length = 30

    def __init__(self, rng):
        self.xpos = rng.uniform(0, SIZE[0])
        self.len = rng.uniform(self.min_length, self.max_length)
        self.ypos = -self.len
        self.thick = int(
            (self.len - self.min_length) * 4 / (self.max_length - 10) + 1
        )
        self.gravity = \
            (self.len - self.min_length) * 15 / (self.max_length + 10) + 1
        self.time = 0

    def render(self, screen):
        pygame.draw.line(
            screen, 
            self.purple, 
            [self.xpos, self.ypos], 
            [self.xpos, self.ypos+self.len], 
            self.thick
        )
        return self

    def fall(self, screen):
        self.ypos += self.gravity * (self.time + DT) ** 2
        self.render(screen)
        
class PurpleRain(object):
    def __init__(self, screen):
        self.display = screen
        self.rng = np.random.default_rng()
        self.drops = [PurpleDrop(self.rng).render(self.display)]

    def fall(self):
        for i in range(len(self.drops))[::-1]:
            self.drops[i].fall(self.display)
            if self.drops[i].ypos > SIZE[1]:
                del self.drops[i]
        if self.rng.random() > .95: 
            self.drops.append(PurpleDrop(self.rng).render(self.display))
