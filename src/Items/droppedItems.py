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
        self.hp = 0
    
    def update(self, world):
        pass


class DroppedStick(DroppedItem):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width, self.height = STICK_WIDTH, STICK_HEIGHT 
        img = pygame.image.load(os.path.join("src", "Graphics", "Stick.png"))
        self.img = pygame.transform.scale(img, (STICK_WIDTH, STICK_HEIGHT))
        self.item = Stick()


class DroppedRock(DroppedItem):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width, self.height = ROCK_WIDTH, ROCK_HEIGHT 
        img = pygame.image.load(os.path.join("src", "Graphics", "Rock.png"))
        self.img = pygame.transform.scale(img, (ROCK_WIDTH, ROCK_HEIGHT))
        self.item = Rock()

class DroppedLog(DroppedItem):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width, self.height = LOG_WIDTH, LOG_HEIGHT 
        img = pygame.image.load(os.path.join("src", "Graphics", "Log.png"))
        self.img = pygame.transform.scale(img, (LOG_WIDTH, LOG_HEIGHT))
        self.item = Log()

class DroppedCampfire(DroppedItem):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width, self.height = CAMPFIRE_WIDTH, CAMPFIRE_HEIGHT 
        img = pygame.image.load(os.path.join("src", "Graphics", "Campfire.png"))
        self.img = pygame.transform.scale(img, (CAMPFIRE_WIDTH, CAMPFIRE_HEIGHT))
        self.item = Campfire()


class DroppedDeadFrog(DroppedItem):
    def __init__(self, x, y):
        super().__init__(x, y)


class DroppedDeadRabbit(DroppedItem):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width, self.height = RABBIT_HEIGHT, RABBIT_WIDTH
        img = pygame.image.load(os.path.join("src", "Graphics", "DeadRabbit.png"))
        self.img = pygame.transform.scale(img, (RABBIT_HEIGHT, RABBIT_WIDTH))
        self.item = DeadRabbit()
