import pygame
from physics import Physics
from configs import PLAYER_WIDTH, PLAYER_HEIGHT

class Player(Physics):
    def __init__(self):
        super().__init__(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)


    def render(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (250, 200), 30)