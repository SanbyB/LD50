import pygame
import os.path
from configs import TREE_WIDTH, TREE_HEIGHT
import numpy as np
from Items.items import Log

class Tree:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.pos = x, y
        self.width, self.height = TREE_WIDTH, TREE_HEIGHT
        img = pygame.image.load(os.path.join("src", "Graphics", f"Tree{np.random.randint(1, 5)}.png"))
        self.img = pygame.transform.scale(img, (TREE_WIDTH, TREE_HEIGHT))
        self.hp = 20
        self.alive = False
        self.item = Log()

    def update(self, world):
        pass