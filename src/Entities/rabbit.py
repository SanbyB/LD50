from physics import Physics
from configs import RABBIT_WIDTH, RABBIT_HEIGHT, RABBIT_VEL, RABBIT_HOLE_WIDTH, RABBIT_HOLE_HEIGHT
from Items.droppedItems import DroppedDeadRabbit
import pygame
import os.path
import numpy as np


class Rabbit(Physics):
    def __init__(self, x, y, world, hole):
        super().__init__(x, y, RABBIT_WIDTH, RABBIT_HEIGHT)
        self.hole = hole
        self.hp = 5
        img = pygame.image.load(os.path.join("src", "Graphics", "Rabbit.png"))
        self.img = pygame.transform.scale(img, (RABBIT_WIDTH, RABBIT_HEIGHT))
        self.clock = 0
        self.world = world

    def update(self, world):
        super().update()
        self.clock +=1
        self.hide()
        if self.hp <= 0:
            self.alive = False
            self.world.removeEntity(self)
            self.world.addEntity(DroppedDeadRabbit(self.x, self.y))

    def move(self):
        pass
        #TODO


    def takeDamage(self, amount):
        self.hp -= amount
    

    def hide(self):
        '''
        go back to rabbit hole
        '''
        if (self.x - self.hole.x)**2 + (self.y - self.hole.y)**2 < 30**2:
            self.world.removeEntity(self)
        else:
            signX = np.sign(self.x - self.hole.x)
            signY = np.sign(self.y - self.hole.y)
            x = abs(self.x - self.hole.x)
            y = abs(self.y - self.hole.y)

            theta = np.arctan(y/x)

            self.vx = -signX * RABBIT_VEL * np.cos(theta)
            self.vy = -signY * RABBIT_VEL * np.sin(theta)




class RabbitHole:
    def __init__(self, x, y, world):
        self.x, self.y = x, y
        self.width, self.height = RABBIT_HOLE_WIDTH, RABBIT_HOLE_HEIGHT
        self.world = world
        self.hp = 10000000
        self.alive = False
        self.clock = 0
        img = pygame.image.load(os.path.join("src", "Graphics", "RabbitHole.png"))
        self.img = pygame.transform.scale(img, (RABBIT_HOLE_WIDTH, RABBIT_HOLE_HEIGHT))

    def update(self, world):
        self.hp = 10000000
        self.clock += 1
        if self.clock == 100:
            self.clock = 0
            self.spawn()

    def spawn(self):
        self.world.addEntity(Rabbit(self.x + np.random.randint(-200, 200), self.y + np.random.randint(-200, 200), self.world, self))
