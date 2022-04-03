from Entities.enemy import Enemy
import pygame
from configs import STICKY_WIDTH, STICKY_HEIGHT
import os.path
from Items.droppedItems import DroppedStick

class Sticky(Enemy):
    def __init__(self, x, y, player):
        super().__init__(x, y, STICKY_WIDTH, STICKY_HEIGHT, player)
        img = pygame.image.load(os.path.join("src", "Graphics", "Sticky.png"))
        self.img = pygame.transform.scale(img, (STICKY_WIDTH, STICKY_HEIGHT))
        self.attackStrength = 2
        self.attackSpeed = 80
        self.hp = 10

    def update(self, world):
        super().update(world)
        if self.hp <= 0:
            world.addEntity(DroppedStick(self.x, self.y))