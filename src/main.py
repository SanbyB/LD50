import sys
import pygame
from camera import Camera
from window import Window
from player import Player

class Game:
    def __init__(self):
        self.window = Window() # The screen var is what everything is to be rendered on
        self.player = Player()
        self.cam = Camera()

    def update(self):
        '''
        Updates game based on physics,
        game mechanics and player input
        '''
        self.player.update()
        self.cam.move(self.player)

    def render(self):
        '''
        Draws everything that is supposed
        to be seen by the player
        '''
        self.window.clear() # clears the screen before
        #TODO
        self.window.background(self.cam)
        self.player.render(self.window.screen)
        self.window.update()
        


game = Game()

pygame.init()

clock = pygame.time.Clock()

while True: # Main game loop
    dt = clock.tick(60)
    game.update()
    game.render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
