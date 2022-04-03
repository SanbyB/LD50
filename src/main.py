import sys
import pygame
from camera import Camera
from window import Window
from player import Player
from world import World
from Entities.rabbit import Rabbit

class Game:
    def __init__(self):
        self.window = Window() # The screen var is what everything is to be rendered on
        self.player = Player()
        self.cam = Camera()
        self.world = World(self.player)

    def updateEvent(self, event):
        self.player.inventory.selectItem(event)
        self.player.attack(event, self.world.entities, self.world)

    def update(self):
        '''
        Updates game based on physics,
        game mechanics and player input
        '''
        self.player.update()
        if self.player.alive == False:
            self.gameOver()
        self.world.update(self.player)
        self.cam.move(self.player)

    def render(self):
        '''
        Draws everything that is supposed
        to be seen by the player
        '''
        self.window.clear(self.player.x, self.player.y) # clears the screen before
        self.window.background(self.cam)
        self.world.renderEntities(self.window.screen, self.cam, self.player)
        self.player.render(self.window.screen)
        self.window.update()
    
    def gameOver(self):
        # delete all entities
        # display end screen
        pass
        


game = Game()

pygame.init()

clock = pygame.time.Clock()

while True: # Main game loop
    dt = clock.tick(60)
    game.update()
    game.render()
    for event in pygame.event.get():
        game.updateEvent(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
