import pygame
import os.path
from configs import *
from Items.items import *

'''
These are entities, which can be added and removed from the world
'''

class DroppedItem:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.alive = False


class DroppedStick(DroppedItem):
    def __init__(self, x, y):
        super().__init__(x, y)


class DroppedRock(DroppedItem):
    def __init__(self, x, y):
        super().__init__(x, y)

class DroppedLog(DroppedItem):
    def __init__(self, x, y):
        super().__init__(x, y)

class DroppedCampfire(DroppedItem):
    def __init__(self, x, y):
        super().__init__(x, y)


class DroppedDeadFrog(DroppedItem):
    def __init__(self, x, y):
        super().__init__(x, y)


class DroppedDeadRabbit(DroppedItem):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width, self.height = RABBIT_HEIGHT, RABBIT_WITDTH
        img = pygame.image.load(os.path.join("src", "Graphics", "DeadRabbit.png"))
        self.img = pygame.transform.scale(img, (RABBIT_HEIGHT, RABBIT_WITDTH))
        self.item = DeadRabbit()

    def update(self, world):
        pass
        
