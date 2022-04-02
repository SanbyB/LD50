import pygame
from configs import SCREEN_WIDTH, SCREEN_HEIGHT

class Window:
    def __init__(self):
        self.width, self.height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('LD50')

    def clear(self):
        self.screen.fill((0,0,0))

    def grid(self, x=0 , y=0):
        for i in range(0, self.width, 40):
            pygame.draw.rect(self.screen, (255,255,255), (i + x, 0, 2, self.height))
        for i in range(0, self.height, 40):
            pygame.draw.rect(self.screen, (255,255,255), (0, i + y, self.width, 2))

    def background(self, cam):
        self.grid(cam.x, cam.y)

    def update(self):
        pygame.display.update()