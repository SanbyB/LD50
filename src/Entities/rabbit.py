from physics import Physics
from configs import RABBIT_WITDTH, RABBIT_HEIGHT
from Items.droppedItems import DroppedDeadRabbit
import pygame
import os.path

class Rabbit(Physics):
    def __init__(self, x, y):
        super().__init__(x, y, RABBIT_WITDTH, RABBIT_HEIGHT)
        self.hole = None #RabbitHole object todo
        self.hp = 5
        img = pygame.image.load(os.path.join("src", "Graphics", "Rabbit.png"))
        self.img = pygame.transform.scale(img, (RABBIT_WITDTH, RABBIT_HEIGHT))

    def update(self, world):
        if self.hp <= 0:
            self.alive = False
            world.removeEntity(self)
            world.addEntity(DroppedDeadRabbit(self.x, self.y))

    def movement(self):
        pass
        #TODO

    def takeDamage(self, amount):
        self.hp -= amount