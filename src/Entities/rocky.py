from Entities.enemy import Enemy
import pygame
from configs import ROCKY_WIDTH, ROCKY_HEIGHT
import os.path
from Items.droppedItems import DroppedRock

class Rocky(Enemy):
    def __init__(self, x, y, player):
        super().__init__(x, y, ROCKY_WIDTH, ROCKY_HEIGHT, player)
        img = pygame.image.load(os.path.join("src", "Graphics", "Rocky.png"))
        self.img = pygame.transform.scale(img, (ROCKY_WIDTH, ROCKY_HEIGHT))
        self.attackRange = 100
        self.attackSpeed = 130
        self.attackStrength = 5
        self.vel = 2.5
        self.hp = 15

    def update(self, world):
        super().update(world)
        if self.hp <= 0:
            world.addEntity(DroppedRock(self.x, self.y))