from configs import FRICTION

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


    def applyVel(self): # allows the movement of the objects
        self.x += self.vx
        self.y += self.vy
        self.vx = self.vx * FRICTION
        self.vy = self.vy * FRICTION

    