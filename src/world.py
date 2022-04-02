from configs import SCREEN_WIDTH, SCREEN_HEIGHT


class World:
    def __init__(self):
        self.entities = [] # list of entities in the world

    def update(self):
        for ent in self.entities:
            ent.update(self)

    
    def addEntity(self, entity):
        self.entities.append(entity)
    
    def removeEntity(self, entity):
        for index, ent in enumerate(self.entities):
            if ent == entity:
                del self.entities[index] # might be better to use remove function?
    
    def renderEntities(self, screen, cam):
        for ent in self.entities:
            screen.blit(ent.img, (ent.x + cam.x + (SCREEN_WIDTH - ent.width)/2, ent.y + cam.y + (SCREEN_HEIGHT - ent.height)/2)) # TODO center the entity