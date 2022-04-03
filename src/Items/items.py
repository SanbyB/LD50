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
        self.id = "stick"


class Rock(Item):
    def __init__(self) -> None:
        super().__init__()
        self.width, self.height = ROCK_WIDTH, ROCK_HEIGHT
        img = pygame.image.load(os.path.join("src", "Graphics", "Rock.png"))
        self.img = pygame.transform.scale(img, (ROCK_WIDTH, ROCK_HEIGHT))
        self.id = "rock"


class Log(Item):
    def __init__(self) -> None:
        super().__init__()
        self.width, self.height = LOG_WIDTH, LOG_HEIGHT
        img = pygame.image.load(os.path.join("src", "Graphics", "Log.png"))
        self.img = pygame.transform.scale(img, (LOG_WIDTH, LOG_HEIGHT))
        self.id = "log"


class Axe(Item):
    def __init__(self) -> None:
        super().__init__()
        self.width, self.height = AXE_WIDTH, AXE_HEIGHT
        img = pygame.image.load(os.path.join("src", "Graphics", "Axe.png"))
        self.img = pygame.transform.scale(img, (AXE_WIDTH, AXE_HEIGHT))
        self.id = "axe"
        self.uses = 10


class Spear(Item):
    def __init__(self) -> None:
        super().__init__()
        self.width, self.height = SPEAR_WIDTH, SPEAR_HEIGHT
        img = pygame.image.load(os.path.join("src", "Graphics", "Spear.png"))
        self.img = pygame.transform.scale(img, (SPEAR_WIDTH, SPEAR_HEIGHT))
        self.id = "spear"
        self.uses = 10

class Torch(Item):
    def __init__(self) -> None:
        super().__init__()


class Campfire(Item):
    def __init__(self) -> None:
        super().__init__()
        self.width, self.height = CAMPFIRE_WIDTH, CAMPFIRE_HEIGHT
        img = pygame.image.load(os.path.join("src", "Graphics", "Campfire.png"))
        self.img = pygame.transform.scale(img, (CAMPFIRE_WIDTH, CAMPFIRE_HEIGHT))
        self.uses = 3
        self.id = "campfire"


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
        self.id = "deadRabbit"
        self.hunger = 1.5


class CookedRabbit(Item):
    def __init__(self) -> None:
        super().__init__()
        self.width, self.height = 69, 45
        img = pygame.image.load(os.path.join("src", "Graphics", "Food.png"))
        self.img = pygame.transform.scale(img, (69, 45))
        self.id = "cookedRabbit"
        self.hunger = 5




