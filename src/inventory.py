import pygame

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
                self.selectedItem += 1
            elif event.button == 5:
                self.selectedItem -= 1
        if self.selectedItem < 0: # loop round
            self.selectedItem = len(self.storedItems) - 1
        if self.selectedItem >= len(self.storedItems):
            self.selectedItem = 0        


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
