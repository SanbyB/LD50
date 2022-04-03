import pygame
import os.path
from configs import HOTBAR_WIDTH, HOTBAR_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT

class Inventory:
    def __init__(self):
        self.storedItems = [None, None, None, None, None, None, None, None] # list of 8 items stored in inventory
        self.inventoryFull = False
        self.selectedItem = 0 # index of the item in hand

    def update(self):
        pass

    def addToInventory(self, item):
        if self.inventoryFull:
            return 1 # inventroy full
        for index, slot in enumerate(self.storedItems):
            if slot == None:
                self.storedItems[index] = item
                if index + 1 == len(self.storedItems):
                    self.inventoryFull = True
                return 0 # successful addition
        return 1 # overflowed inventory

    
    def removeFromInventory(self, item):
        for index, slot in enumerate(self.storedItems):
            if slot == item: # might need to change this to a type or id
                self.storedItems[index] = None
                return 0 # succesful remove
        return 1 # item not in inventory

    
    def selectItem(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.selectedItem -= 1
            elif event.button == 5:
                self.selectedItem += 1
        if self.selectedItem < 0: # loop round
            self.selectedItem = len(self.storedItems) - 1
        if self.selectedItem >= len(self.storedItems):
            self.selectedItem = 0


    def render(self, screen):
        img = pygame.image.load(os.path.join("src", "Graphics", f"Hotbar{self.selectedItem + 1}.png"))
        img = pygame.transform.scale(img, (HOTBAR_WIDTH, HOTBAR_HEIGHT))
        screen.blit(img, ((SCREEN_WIDTH - HOTBAR_WIDTH)/2, SCREEN_HEIGHT - HOTBAR_HEIGHT*1.1))

        pos = [(235, 548), (277, 549), (318, 547), (367, 545), (422, 543), (467, 539), (508, 536), (553, 531)]

        boxWidth = 50

        for index, item in enumerate(self.storedItems):
            if item != None:
                w, h = item.width, item.height
                scale = boxWidth / w
                img = item.img
                img = pygame.transform.scale(img, (boxWidth, int(h * scale)))
                screen.blit(img, (pos[index][0] - boxWidth/2, pos[index][1] - (h * scale)/2))





if __name__ == "__main__":
    inv = Inventory()
    inv.addToInventory(5)
    print(inv.storedItems)
    for i in range(5):
        inv.addToInventory(i)
    inv.removeFromInventory(2)
    print(inv.storedItems)
    for i in range(4):
        inv.addToInventory(i)
        print(inv.inventoryFull)
    print(inv.storedItems)
    for i in range(3):
        inv.removeFromInventory(i)
    print(inv.storedItems)
