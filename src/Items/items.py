"""
Items that have been picked up by the player and placed in the inventory
"""
from configs import *
import pygame
import os.path

class Item:
    def __init__(self) -> None:
        pass


class Stick(Item):
    def __init__(self) -> None:
        super().__init__()
        self.width, self.height = STICK_WIDTH, STICK_HEIGHT
        img = pygame.image.load(os.path.join("src", "Graphics", "Stick.png"))
        self.img = pygame.transform.scale(img, (STICK_WIDTH, STICK_HEIGHT))


class Rock(Item):
    def __init__(self) -> None:
        super().__init__()
        self.width, self.height = ROCK_WIDTH, ROCK_HEIGHT
        img = pygame.image.load(os.path.join("src", "Graphics", "Rock.png"))
        self.img = pygame.transform.scale(img, (ROCK_WIDTH, ROCK_HEIGHT))


class Log(Item):
    def __init__(self) -> None:
        super().__init__()
        self.width, self.height = LOG_WIDTH, LOG_HEIGHT
        img = pygame.image.load(os.path.join("src", "Graphics", "Log.png"))
        self.img = pygame.transform.scale(img, (LOG_WIDTH, LOG_HEIGHT))


class Axe(Item):
    def __init__(self) -> None:
        super().__init__()


class Spear(Item):
    def __init__(self) -> None:
        super().__init__()


class Torch(Item):
    def __init__(self) -> None:
        super().__init__()


class Campfire(Item):
    def __init__(self) -> None:
        super().__init__()


class DeadFrog(Item):
    def __init__(self) -> None:
        super().__init__()


class CookedFrog(Item):
    def __init__(self) -> None:
        super().__init__()


class DeadRabbit(Item):
    def __init__(self) -> None:
        super().__init__()
        self.width, self.height = RABBIT_ICON_WITDTH, RABBIT_ICON_HEIGHT
        img = pygame.image.load(os.path.join("src", "Graphics", "DeadRabbitIcon.png"))
        self.img = pygame.transform.scale(img, (RABBIT_ICON_WITDTH, RABBIT_ICON_HEIGHT))


class CookedRabbit(Item):
    def __init__(self) -> None:
        super().__init__()




