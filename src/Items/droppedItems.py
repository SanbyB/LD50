import pygame
import os.path

class DroppedItem:
    def __init__(self, x, y):
        self.x, self.y = x, y


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
        
