import sys
import pygame
from camera import Camera
from configs import SCREEN_WIDTH, SCREEN_HEIGHT
from window import Window
from player import Player
from world import World
from craft import Craft
import os.path

class Game:
    def __init__(self):
        self.window = Window() # The screen var is what everything is to be rendered on
        self.player = Player()
        self.cam = Camera()
        self.world = World(self.player)
        self.craft = Craft(self.player.inventory)
        self.notStarted = True

    def updateEvent(self, event):
        self.player.inventory.selectItem(event)
        self.player.attack(event, self.world.entities, self.world)
        self.craft.buy(event)

    def update(self):
        '''
        Updates game based on physics,
        game mechanics and player input
        '''
        if self.notStarted:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_RETURN]:
                self.notStarted = False
        else:
            self.player.update()
            if self.player.alive == False:
                self.gameOver()
            self.world.update(self.player)
            self.cam.move(self.player)
            self.craft.update()
            

    def render(self):
        '''
        Draws everything that is supposed
        to be seen by the player
        '''
        self.window.clear(self.player.x, self.player.y) # clears the screen before
        self.window.background(self.cam)
        self.world.renderEntities(self.window.screen, self.cam, self.player)
        self.player.render(self.window.screen)
        self.craft.openWindow(self.window.screen)

        if self.player.alive == False:
            screen = self.window.screen

            img = pygame.image.load(os.path.join("src", "Graphics", "Gameover.png"))
            img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))

            screen.blit(img, (0,0))

        if self.notStarted:
            screen = self.window.screen

            img = pygame.image.load(os.path.join("src", "Graphics", "Start.png"))
            img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))

            screen.blit(img, (0,0))

        self.window.update()
        
    
    def gameOver(self):

        self.world.entities = []
        


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

    
