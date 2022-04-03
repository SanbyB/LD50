import pygame
from configs import SCREEN_WIDTH, SCREEN_HEIGHT
from Entities.grass import Grass
import numpy as np

class Window:
    def __init__(self):
        self.width, self.height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('LD50')
        self.grassList = self.grass()

    def clear(self, x, y):
        self.screen.fill((145+((x+2000)*50/4000),106+((y+1600)*50/3200),0))

    def grid(self, x=0 , y=0):
        for i in range(0, self.width, 40):
            pygame.draw.rect(self.screen, (255,255,255), (i + x, 0, 2, self.height))
        for i in range(0, self.height, 40):
            pygame.draw.rect(self.screen, (255,255,255), (0, i + y, self.width, 2))

    def background(self, cam):
        for g in self.grassList:
            self.screen.blit(g.img, (g.pos[0] + cam.x, g.pos[1] + cam.y))


    def update(self):
        pygame.display.update()

    def grass(self):
        pos = []
        for i in range(-4, 5, 1):
            for j in range(-4, 5, 1):
                pos.append(Grass(i * 500 + np.random.randint(-80, 80), j * 400 + np.random.randint(-80, 80)))
        return pos