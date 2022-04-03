import pygame
import os.path

class Grass:
    def __init__(self, x, y):
        self.pos = x, y
        grassImg = pygame.image.load(os.path.join("src", "Graphics", "grassTuft.png"))
        self.img = pygame.transform.scale(grassImg, (60, 60))