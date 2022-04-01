class Physics:
    '''
    Object constrained to the Physics of the game
    '''
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y # position of object
        self.vx, self.vy = 0, 0 # velocity
        self.ax, self.ay = 0, 0 # acceleration
        self.width, self.height = width, height # width and height of object