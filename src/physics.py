from configs import FRICTION
import numpy as np

class Physics:
    '''
    Object constrained to the Physics of the game
    '''
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y # position of object
        self.vx, self.vy = 0, 0 # velocity 
        self.width, self.height = width, height # width and height of object
        self.alive = True # Physics only acts on things that are alive


    def update(self):
        self.applyVel()
        self.bounds()


    def applyVel(self): # allows the movement of the objects
        self.x += self.vx
        self.y += self.vy
        self.vx = self.vx * FRICTION
        self.vy = self.vy * FRICTION
    
    def bounds(self):
        if abs(self.x) > 2000:
            self.x = np.sign(self.x) * 2000
        if abs(self.y) > 1600:
            self.y = np.sign(self.y) * 1600
        

    