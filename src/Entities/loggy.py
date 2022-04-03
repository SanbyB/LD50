from Entities.enemy import Enemy
import pygame
from configs import LOGGY_WIDTH, LOGGY_HEIGHT
import os.path

class Loggy(Enemy):
    def __init__(self, x, y, width, height, player):
        super().__init__(x, y, width, height, player)
        img = pygame.image.load(os.path.join("src", "Graphics", "Loggy.png"))
        self.img = pygame.transform.scale(img, (LOGGY_WIDTH, LOGGY_HEIGHT))
        # self.width, self.height = width, height