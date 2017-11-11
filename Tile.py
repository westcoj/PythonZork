'''
Created on Nov 8, 2017

@author: Cody
'''
from random import random
from Monster import *
import inspect
from Observer import *
class Neighborhood:
    '''
    docs
    '''
    
    def __init__(self):
        self.houseDesc = []
        self.tileDesc = []
        self.houseDesc.append("A looming two story house")
        self.houseDesc.append("An old colonial style house")
        self.houseDesc.append("A strange looking gothic house, probably decorations")
        self.houseDesc.append("A half-ruined house, you can hear screaming inside")
        self.houseDesc.append("A house literally covered in blood")
        self.houseDesc.append("The biggest house, no really it is")
        self.houseDesc.append("The smallest house, not really but we can pretend")
        self.houseDesc.append("Oh dang it's the secret house, but someone already looted it and filled it with monsters")
        self.houseDesc.append("A cardboard box full of monsters, and a snake?")
        self.houseDesc.append("Your house, but an evil twin of it. It has a goatee so it's obvious")
        self.tileDesc.append("A neighborhood park, completely empty right now")
        self.tileDesc.append("A local well, don't fall in")
        self.tileDesc.append("A bar, seems pretty full of happy people right now")
        self.tileDesc.append("A bar, this one has a rotting smell about it")
        self.tileDesc.append("There might've been a house here once, but its not here right now")
        self.tileDesc.append("A man approaches you and offers a fresh homebrew, you decline because programming while drinking is bad. O_O")
        self.tileDesc.append("You stumble across a box of beers, you want them, but you have too much coding to do. Hey put that down!")
        self.tileDesc.append("This house has already been cleared by someone much better than you")
        self.tileDesc.append("A woman approaches you, demanding you listen to her new vinyl.")
        self.tileDesc.append("IndexError: Variable out of bounds: ... Just kidding, empty tile")
        self.__grid = [[0 for x in range(5)] for y in range(4)]
        for i in range(4):
            self.__grid[i] = []
            for j in range(3):
                descVal = random.randint(0,9)
                tasker = random.randint(0,5)
                if tasker >= 3:
                    self.__grid[i].append(House(self.houseDesc[descVal]))
                else:
                    self.__grid[i].append(Tile(self.tileDesc[descVal]))
                    
    def print(self):
        for x in self.__grid:
            for y in x:
                print (y.description)
                if isinstance(y, House):
                    for l in y.__monsterList:
                        print(l)
                        
    def getGrid(self):
        return self.__grid
            
                

    
class Tile(Observer):
    '''
    classdocs
    '''
    def __init__(self, desc):
        '''
        Constructor
        '''
        self.__description = desc;
        #self.__monsterList= [];
        
    def getDesc(self):
        return self.__description

class House(Tile):
    '''
    classdocs
    '''
    
    def __init__(self,desc):
        super().__init__(desc)
        self.__monsterList = []
        iVal = random.randint(1,10)
        for i in range(iVal):
            jVal = random.randint(0,4)
            if jVal == 0:
                self.__monsterList.append(Person())
            if jVal == 1:
                self.__monsterList.append(Zombie())
            if jVal == 2:
                self.__monsterList.append(Ghoul())
            if jVal == 3:
                self.__monsterList.append(Vampire())
            if jVal == 0:
                self.__monsterList.append(Werewolf())
        
        for y in self.__monsterList:
            y.add_observer(self)
                
    def clear(self):
        for x in self.__monsterList:
            if not isinstance(x,Person):
                return False
            
        return True
    
    def update(self,health, monster):
        if health <= 0:
            print(monster.getName() + " has died")
            inX = self.__monsterList.index(monster)
            self.__monsterList.remove(monster)
            self.__monsterList.insert(inX, Person())
            
    def getList(self):
        return self.__monsterList
            

    
        