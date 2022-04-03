from physics import Physics
from configs import RABBIT_WIDTH, RABBIT_HEIGHT, RABBIT_VEL, RABBIT_HOLE_WIDTH, RABBIT_HOLE_HEIGHT
from Items.droppedItems import DroppedDeadRabbit
import pygame
import os.path
import numpy as np


class Rabbit(Physics):
    def __init__(self, x, y, world, hole, player):
        super().__init__(x, y, RABBIT_WIDTH, RABBIT_HEIGHT)
        self.hole = hole
        self.hp = 5
        img = pygame.image.load(os.path.join("src", "Graphics", "Rabbit.png"))
        self.img = pygame.transform.scale(img, (RABBIT_WIDTH, RABBIT_HEIGHT))
        self.world = world
        self.player = player
        self.clock = 0

    def update(self, world):
        super().update()
        self.clock += 1
        if self.clock == 5000:
            self.world.removeEntity(self)
        self.move()
        if self.hp <= 0:
            self.alive = False
            self.world.removeEntity(self)
            self.world.addEntity(DroppedDeadRabbit(self.x, self.y))

    def move(self):
        self.vx = self.vx * 1.05
        self.vy = self.vy * 1.05
        if (self.player.x - self.x)**2 + (self.player.y - self.y)**2 < 150**2:
            self.hide()
        else:
            if self.clock % 100 == 0:
                self.vx = np.random.uniform(-RABBIT_VEL, RABBIT_VEL)
                self.vy = np.random.uniform(-RABBIT_VEL, RABBIT_VEL)


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

            theta = 90

            if x > 1:
                theta = np.arctan(y/x)

            self.vx = -signX * RABBIT_VEL * np.cos(theta)
            self.vy = -signY * RABBIT_VEL * np.sin(theta)




class RabbitHole:
    def __init__(self, x, y, world, player):
        self.x, self.y = x, y
        self.width, self.height = RABBIT_HOLE_WIDTH, RABBIT_HOLE_HEIGHT
        self.world = world
        self.hp = 10000000
        self.alive = False
        self.clock = 0
        img = pygame.image.load(os.path.join("src", "Graphics", "RabbitHole.png"))
        self.img = pygame.transform.scale(img, (RABBIT_HOLE_WIDTH, RABBIT_HOLE_HEIGHT))
        self.player = player

    def update(self, world):
        self.hp = 10000000
        self.clock += 1
        if self.clock == 1000:
            self.clock = 0
            self.spawn()

    def spawn(self):
        self.world.addEntity(Rabbit(self.x + np.random.randint(-200, 200), self.y + np.random.randint(-200, 200), self.world, self, self.player))

    def takeDamage(self, amount):
        pass