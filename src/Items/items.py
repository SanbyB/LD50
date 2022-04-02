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


class Rock(Item):
    def __init__(self) -> None:
        super().__init__()


class Log(Item):
    def __init__(self) -> None:
        super().__init__()


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
        self.width, self.height = RABBIT_HEIGHT, RABBIT_WITDTH
        img = pygame.image.load(os.path.join("src", "Graphics", "DeadRabbit.png"))
        self.img = pygame.transform.scale(img, (RABBIT_HEIGHT, RABBIT_WITDTH))


class CookedRabbit(Item):
    def __init__(self) -> None:
        super().__init__()




