import pygame
import numpy as np
from physics import Physics
from inventory import Inventory
from configs import *



class Player(Physics):
    def __init__(self):
        super().__init__(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.inventory = Inventory()

    def update(self):
        super().update()
        self.move()


    def render(self, surface):
        pygame.draw.rect(
            surface, (255, 0, 0),
            ((SCREEN_WIDTH-PLAYER_WIDTH)/2, (SCREEN_HEIGHT-PLAYER_HEIGHT)/2, PLAYER_WIDTH, PLAYER_HEIGHT)
            )

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vx -= WALK_ACC
        
        if keys[pygame.K_d]:
            self.vx += WALK_ACC
        
        if keys[pygame.K_w]:
            self.vy += WALK_ACC

        if keys[pygame.K_s]:
            self.vy -= WALK_ACC

        if abs(self.vx) > WALK_VEL:
            self.vx = np.sign(self.vx) * WALK_VEL
        
        if abs(self.vy) > WALK_VEL:
            self.vy = np.sign(self.vy) * WALK_VEL

        if self.vx**2 + self.vy**2 > WALK_VEL**2:
            self.vx = self.vx/1.3
            self.vy = self.vy/1.3
