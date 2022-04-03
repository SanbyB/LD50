from Entities.enemy import Enemy
import pygame
from configs import LOGGY_WIDTH, LOGGY_HEIGHT
import os.path
from Items.droppedItems import DroppedLog

class Loggy(Enemy):
    def __init__(self, x, y, player):
        super().__init__(x, y, LOGGY_WIDTH, LOGGY_HEIGHT, player)
        img = pygame.image.load(os.path.join("src", "Graphics", "Loggy.png"))
        self.img = pygame.transform.scale(img, (LOGGY_WIDTH, LOGGY_HEIGHT))
        self.vel = 3

    def update(self, world):
        super().update(world)
        if self.hp <= 0:
            world.addEntity(DroppedLog(self.x, self.y))