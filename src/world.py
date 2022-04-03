from configs import SCREEN_WIDTH, SCREEN_HEIGHT

class World:
    def __init__(self):
        self.entities = [] # list of entities in the world

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