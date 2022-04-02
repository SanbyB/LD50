import random

class Camera:
    def __init__(self):
        self.x, self.y = 0, 0 # camera position centered around player
        self.shakeAmount = 0

    def move(self, player):
        self.x = -player.x + random.uniform(0, self.shakeAmount)
        self.y = -player.y + random.uniform(0, self.shakeAmount)
        self.shakeAmount = self.shakeAmount * 0.7

    def shake(self, amount):
        self.shakeAmount += amount