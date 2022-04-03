import pygame
import numpy as np
from Items.items import CookedRabbit
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
        self.foodClock = 0
        self.attackClock = 0
        self.attackRange = 130
        self.attackStrength = 3
        self.attackSpeed = 50
        self.hand = None
        

    def update(self):
        super().update()
        self.inventory.update()
        if self.hp <= 0: # check if player has died
            self.hp = 0
            self.alive = False
        self.move()
        self.checkHand()
        self.eat()
        self.cook()
        self.foodClock += 1 # update the players food clock
        self.attackClock += 1
        if self.foodClock == 823:
            self.updateHunger()
            self.foodClock = 0

    def checkHand(self):
        index = self.inventory.selectedItem
        item = self.inventory.storedItems[index]
        
        if item != None:
            item = item.id
            self.hand = item
            if item == "spear":
                self.attackRange = 200
                self.attackStrength = 5
            if item == "axe":
                self.attackStrength = 7.5
                self.attackSpeed = 80
            if item != "spear":
                if item != "axe":
                    self.attackRange = 130
                    self.attackStrength = 3
                    self.attackSpeed = 50
        else:
            self.attackRange = 130
            self.attackStrength = 3
            self.attackSpeed = 50
    
    def cook(self):
        if self.hand == "deadRabbit":
            pos = None
            for index, item in enumerate(self.inventory.storedItems):
                if item != None:
                    if item.id == "campfire":
                        pos = index
            if pos != None:
                keys = pygame.key.get_pressed()

                if keys[pygame.K_f]:
                    i = self.inventory.selectedItem
                    self.inventory.storedItems[i] = CookedRabbit()
                    self.inventory.storedItems[pos].uses -= 1
                    if self.inventory.storedItems[pos].uses <= 0:
                        self.inventory.storedItems[pos] = None
                        self.inventory.inventoryFull = False
    
    def eat(self):
        if self.hand == "deadRabbit" or self.hand == "cookedRabbit":
            keys = pygame.key.get_pressed()

            if keys[pygame.K_r]:
                index = self.inventory.selectedItem
                self.hunger += self.inventory.storedItems[index].hunger
                self.hunger = min(self.hunger, 10)
                self.inventory.storedItems[index] = None
                self.hand = None
                self.inventory.inventoryFull = False



    def render(self, surface):
        img = pygame.image.load(os.path.join("src", "Graphics", "Player1.png"))
        img = pygame.transform.scale(img, (PLAYER_WIDTH, PLAYER_HEIGHT))
        surface.blit(img, ((SCREEN_WIDTH-PLAYER_WIDTH)/2, (SCREEN_HEIGHT-PLAYER_HEIGHT)/2, PLAYER_WIDTH, PLAYER_HEIGHT))
        self.inventory.render(surface)
        self.statusBars(surface)


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
            self.vx = self.vx * 0.85
            self.vy = self.vy * 0.85

    
    def updateHunger(self):
        self.hunger -= 1
        # Lose hp at faster rate when hunger is less than 3
        if self.hunger < 3:
            self.hp -= 0.5
        if self.hunger < 2:
            self.hp -= 0.5
        if self.hunger < 1:
            self.hp -=0.25
        if self.hunger < 0:
            self.hunger = 0


    def attack(self, event, entities, world):
        '''
        Also works as a pick up function for dead entities
        '''
        if self.attackClock < self.attackSpeed:
            return
        
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
                                    self.attackClock = 0
                                    if self.hand == "spear" or self.hand == "axe":
                                        index = self.inventory.selectedItem
                                        self.inventory.storedItems[index].uses -= 1
                                        if self.inventory.storedItems[index].uses <= 0:
                                            self.inventory.storedItems[index] = None
                                            self.hand = None
                                            self.inventory.inventoryFull = False
            elif ent.hp <= 0: # pick up item
                if not self.inventory.inventoryFull: # if inventory is full ignore
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1: # left click
                                xClick, yClick = pygame.mouse.get_pos()

                                if ent.x - ent.width/2 < xClick + self.x - SCREEN_WIDTH/2 < ent.x + ent.width/2: # check x bounding box
                                    if ent.y - ent.height/2 < yClick + self.y - SCREEN_HEIGHT/2 < ent.y + ent.height/2: # check y bounding box
                                        if (self.x - ent.x)**2 + (self.y - ent.y)**2 < 130**2:
                                            if ent.item != None:
                                                self.inventory.addToInventory(ent.item)
                                                world.removeEntity(ent)
            elif ent.hp > 0:
                if self.hand == "axe":
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: # left click
                            xClick, yClick = pygame.mouse.get_pos()

                            if ent.x - ent.width/2 < xClick + self.x - SCREEN_WIDTH/2 < ent.x + ent.width/2: # check x bounding box
                                if ent.y - ent.height/2 < yClick + self.y - SCREEN_HEIGHT/2 < ent.y + ent.height/2: # check y bounding box
                                    ent.takeDamage(self.attackStrength)
                                    index = self.inventory.selectedItem
                                    self.inventory.storedItems[index].uses -= 1
                                    if self.inventory.storedItems[index].uses <= 0:
                                        self.inventory.storedItems[index] = None
                                        self.hand = None
                                        self.inventory.inventoryFull = False


    def statusBars(self, screen):
        heart = pygame.image.load(os.path.join("src", "Graphics", "Heart.png"))
        heart = pygame.transform.scale(heart, (48, 51))

        food = pygame.image.load(os.path.join("src", "Graphics", "Food.png"))
        food = pygame.transform.scale(food, (69, 45))

        knife = pygame.image.load(os.path.join("src", "Graphics", "Knife.png"))
        knife = pygame.transform.scale(knife, (39, 46))

        screen.blit(heart, (679, 184))
        screen.blit(food, (733, 184))
        screen.blit(knife, (620, 184))

        pygame.draw.rect(screen, (240, 0, 0), (690, 180-6.5*self.hp, 26, 6.5*self.hp))
        pygame.draw.rect(screen, (136, 0, 21), (750, 180-13*self.hunger, 26, 13*self.hunger))
        pygame.draw.rect(screen, (0, 162, 232), (630, 180 - (130/self.attackSpeed) * min(self.attackClock, self.attackSpeed), 26, (130/self.attackSpeed) * min(self.attackClock, self.attackSpeed)))