from physics import Physics
from configs import RABBIT_WITDTH, RABBIT_HEIGHT
from Items.droppedItems import DroppedDeadRabbit
import pygame
import os.path

class Rabbit(Physics):
    def __init__(self, x, y):
        super().__init__(x, y, RABBIT_WITDTH, RABBIT_HEIGHT)
        self.world = None
        self.hole = None #RabbitHole object todo
        self.hp = 5
        self.img = pygame.image.load(os.path.join("src", "Graphics", "Rabbit.png"))

    
    def update(self):
        if self.hp <= 0:
            self.world.removeEntity(self)
            self.world.addEntity(DroppedDeadRabbit(self.x, self.y))
