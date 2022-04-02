import pygame
import numpy as np
from physics import Physics
from inventory import Inventory
from configs import *
import os.path



class Player(Physics):
    def __init__(self):
        super().__init__(0, 0, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.inventory = Inventory()
        self.hp = 20 # player health, when =< 0 the game is over
        '''
        when the hunger is bellow 3 the player will start to lose health
        at a faster rate for lower values, the player can find food to eat to replenish health
        '''
        self.hunger = 10
        self.clock = 0
        self.attackRange = 130
        self.attackStrength = 3
        

    def update(self):
        super().update()
        if self.hp <= 0: # check if player has died
            self.alive = False
        self.move()
        self.clock += 1 # update the players clock
        if self.clock == 1000:
            self.updateHunger()
            self.clock = 0



    def render(self, surface):
        img = pygame.image.load(os.path.join("src", "Graphics", "Player.png"))
        img = pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT))
        surface.blit(img, ((SCREEN_WIDTH-PLAYER_WIDTH)/2, (SCREEN_HEIGHT-PLAYER_HEIGHT)/2, PLAYER_WIDTH, PLAYER_HEIGHT))
        self.inventory.render(surface)


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vx -= WALK_ACC
        
        if keys[pygame.K_d]:
            self.vx += WALK_ACC
        
        if keys[pygame.K_w]:
            self.vy -= WALK_ACC

        if keys[pygame.K_s]:
            self.vy += WALK_ACC

        if abs(self.vx) > WALK_VEL:
            self.vx = np.sign(self.vx) * WALK_VEL
        
        if abs(self.vy) > WALK_VEL:
            self.vy = np.sign(self.vy) * WALK_VEL

        if self.vx**2 + self.vy**2 > WALK_VEL**2:
            self.vx = self.vx/1.3
            self.vy = self.vy/1.3

    
    def updateHunger(self):
        self.hunger -= 1
        # Lose hp at faster rate when hunger is less than 3
        if self.hunger < 3:
            self.hp -= 0.5
        if self.hunger < 2:
            self.hp -= 0.25
        if self.hunger < 1:
            self.hp -=0.25


    def attack(self, event, entities, world):
        '''
        Also works as a pick up function for dead entities
        '''
        for ent in entities:
            
            if ent.alive: # attack
                if (self.x - ent.x)**2 + (self.y - ent.y)**2 < self.attackRange**2: # if entity in attack range
                    '''
                    check if event click lands on entity
                    '''
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: # left click
                            xClick, yClick = pygame.mouse.get_pos()

                            if ent.x - ent.width/2 < xClick + self.x - SCREEN_WIDTH/2 < ent.x + ent.width/2: # check x bounding box
                                if ent.y - ent.height/2 < yClick + self.y - SCREEN_HEIGHT/2 < ent.y + ent.height/2: # check y bounding box
                                    ent.takeDamage(self.attackStrength)
            else: # pick up item
                if self.inventory.inventoryFull: # if inventory is full ignore
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: # left click
                            xClick, yClick = pygame.mouse.get_pos()

                            if ent.x - ent.width/2 < xClick + self.x - SCREEN_WIDTH/2 < ent.x + ent.width/2: # check x bounding box
                                if ent.y - ent.height/2 < yClick + self.y - SCREEN_HEIGHT/2 < ent.y + ent.height/2: # check y bounding box
                                    if (self.x - ent.x)**2 + (self.y - ent.y)**2 < 130**2:
                                        self.inventory.addToInventory(ent.item)
                                        world.removeEntity(ent)
