import pygame
from Items.items import *

class Craft:
    def __init__(self, inventory):
        self.invetory = inventory
        self.open = False

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_e]:
            self.open = True
        else:
            self.open = False

    def openWindow(self, screen):
        if self.open:
            axe, spear, fire = Axe(), Spear(), Campfire()
            stick, rock, log = Stick(), Rock(), Log()
            pygame.draw.rect(screen, (40, 40, 40), (100, 100, 600, 400))
            screen.blit(spear.img, (250-spear.width/2, 250-spear.height/2))
            screen.blit(axe.img, (550-axe.width/2, 250-axe.height/2))
            screen.blit(fire.img, (400-fire.width/2, 400-fire.height/2))


    def buy(self, event):
        axe, spear, fire = Axe(), Spear(), Campfire()
        if self.open:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click
                    xClick, yClick = pygame.mouse.get_pos()
                    if 250-spear.width/2 < xClick < 250+spear.width/2:
                        if 250-spear.height/2 < yClick < 250+spear.height/2:
                            self.buySpear()
                    elif 550-axe.width/2 < xClick < 550+axe.width/2:
                        if 250-axe.height/2 < yClick < 250+axe.height/2:
                            self.buyAxe()
                    elif 400-fire.width/2 < xClick < 400+fire.width/2:
                        if 400-fire.height/2 < yClick < 400+fire.height/2:
                            self.buyCampfire()
    

    def buySpear(self):
        rock = None
        stick = None
        for index, item in enumerate(self.invetory.storedItems):
            if item != None:
                if item.id == "rock":
                    rock = index
                if item.id == "stick":
                    stick = index
        if rock == None or stick == None:
            return
        self.invetory.storedItems[rock] = None
        self.invetory.storedItems[stick] = Spear()
        self.invetory.inventoryFull = False


    def buyAxe(self):
        rock = None
        stick = None
        for index, item in enumerate(self.invetory.storedItems):
            if item != None:
                if item.id == "rock":
                    rock = index
                if item.id == "stick":
                    stick = index
        if rock == None or stick == None:
            return
        self.invetory.storedItems[rock] = None
        self.invetory.storedItems[stick] = Axe()
        self.invetory.inventoryFull = False

    
    def buyCampfire(self):
        log = None
        stick = None
        for index, item in enumerate(self.invetory.storedItems):
            if item != None:
                if item.id == "log":
                    log = index
                if item.id == "stick":
                    stick = index
        if log == None or stick == None:
            return
        self.invetory.storedItems[log] = None
        self.invetory.storedItems[stick] = Campfire()
        self.invetory.inventoryFull = False