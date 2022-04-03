from html import entities
from configs import SCREEN_WIDTH, SCREEN_HEIGHT
import numpy as np
from Entities.tree import Tree
from Entities.rabbit import RabbitHole
from Items.droppedItems import DroppedStick, DroppedRock


class World:
    def __init__(self):
        self.entities = [] # list of entities in the world
        for i in range(-2, 3, 1):
            for j in range(-2, 3, 1):
                self.entities.append(Tree(i * 900 + np.random.randint(-80, 80), j * 700 + np.random.randint(-80, 80)))
        for i in range(8):
            self.entities.append(DroppedStick(np.random.randint(-1800, 1800), np.random.randint(-1400, 1400)))
        for i in range(4):
            self.entities.append(DroppedRock(np.random.randint(-1800, 1800), np.random.randint(-1400, 1400)))
        for i in range(4):
            self.entities.append(RabbitHole(np.random.randint(-1800, 1800), np.random.randint(-1400, 1400), self))

        self.clock = 0
        

    def update(self, player):            
        for ent in self.entities:
            if ent.alive and self.rangeCheck(ent, player):
                self.removeEntity(ent)
            ent.update(self)

    def rangeCheck(self, ent, player):
        if (ent.x - player.x)**2 + (ent.y - player.y)**2 > SCREEN_WIDTH**2:
            return True
        return False
    
    def addEntity(self, entity):
        self.entities.append(entity)
    
    def removeEntity(self, entity):
        for index, ent in enumerate(self.entities):
            if ent == entity:
                del self.entities[index] # might be better to use remove function?
    
    def renderEntities(self, screen, cam, player):
        for ent in self.entities:
            if not self.rangeCheck(ent, player):
                screen.blit(ent.img, (ent.x + cam.x + (SCREEN_WIDTH - ent.width)/2, ent.y + cam.y + (SCREEN_HEIGHT - ent.height)/2))