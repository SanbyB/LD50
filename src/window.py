import pygame
from configs import SCREEN_WIDTH, SCREEN_HEIGHT
import os.path

class Window:
    def __init__(self):
        self.width, self.height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('LD50')

    def clear(self):
        self.screen.fill((170,106,0))

    def grid(self, x=0 , y=0):
        for i in range(0, self.width, 40):
            pygame.draw.rect(self.screen, (255,255,255), (i + x, 0, 2, self.height))
        for i in range(0, self.height, 40):
            pygame.draw.rect(self.screen, (255,255,255), (0, i + y, self.width, 2))

    def background(self, cam):
        grassImg = pygame.image.load(os.path.join("src", "Graphics", "grassTuft.png"))
        grassImg = pygame.transform.scale(grassImg, (60, 60))
        self.screen.blit(grassImg, (20 + cam.x, 70 + cam.y))
        # self.grid(cam.x, cam.y)
        pass

    def update(self):
        pygame.display.update()