import pygame
import os.path
from configs import TREE_WIDTH, TREE_HEIGHT
import numpy as np

class Tree:
    def __init__(self, x, y):
        self.pos = x, y
        img = pygame.image.load(os.path.join("src", "Graphics", f"Tree{np.random.randint(1, 5)}.png"))
        self.img = pygame.transform.scale(img, (TREE_WIDTH, TREE_HEIGHT))
        self.hp = 20
