from physics import Physics
from configs import SCREEN_WIDTH, ENEMY_VEL
import numpy as np


class Enemy(Physics):
    def __init__(self, x, y, width, height, player):
        super().__init__(x, y, width, height)
        self.player = player
        self.vel = ENEMY_VEL
        self.attackRange = 150
        self.attackStrength = 4
        self.attackSpeed = 100
        self.clock = 0

    def update(self):
        self.clock += 1
        self.move()

    def move(self):
        if self.attack():
            pass
        else:
            self.idle()

    def attack(self):
        dist = (self.player.x - self.x)**2 + (self.player.y - self.y)**2
        if dist < SCREEN_WIDTH**2:
            if dist < self.attackRange**2:
                if self.clock > self.attackSpeed:
                    self.player.hp -= self.attackStrength
                    self.clock = 0
            signX = np.sign(self.x - self.player.x)
            signY = np.sign(self.y - self.player.y)
            x = abs(self.x - self.player.x)
            y = abs(self.y - self.player.y)

            theta = np.arctan(y/x)

            self.vx = -signX * self.vel * np.cos(theta)
            self.vy = -signY * self.vel * np.sin(theta)
            return True
        return False

    def idle(self):
        if self.clock % 100 == 0:
                self.vx = np.random.uniform(-self.vel, self.vel)
                self.vy = np.random.uniform(-self.vel, self.vel)