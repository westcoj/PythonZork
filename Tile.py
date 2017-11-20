"""
 * The following module contains the neighborhood class which holds a map of house and
 * tile classes for the player to traverse through
 *
 * @author Cody West
 * @version Zork Clone
 * @date 11/08/2017
"""
from random import random
from Monster import *
import inspect
from Observer import *
class Neighborhood:
    '''
    Class that builds game map from houses and blank tiles based on random numbers, 
    and assigns various descriptions to them.
    '''
    
    def __init__(self):
        """
        Constructer that sets up neighborhood in 2-D list with various descriptions
        """
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
        self.__grid = [[0 for x in range(5)] for y in range(5)]
        for i in range(5):
            self.__grid[i] = []
            for j in range(5):
                descVal = random.randint(0,9)
                tasker = random.randint(0,5)
                if tasker >= 3:
                    self.__grid[i].append(House(self.houseDesc[descVal]))
                else:
                    self.__grid[i].append(Tile(self.tileDesc[descVal]))
                    
    def print(self):
        """
        Prints the monsters in the tile if it is a house
        """
        for x in self.__grid:
            for y in x:
                print (y.description)
                if isinstance(y, House):
                    for l in y.__monsterList:
                        print(l)
                        
    def getGrid(self):
        """Gets the neighborhood map of tiles

        Returns:
            The neighborhood map

        """
        return self.__grid
            
                

    
class Tile(Observer):
    '''
    Blank tile for game map and super for houses
    '''
    def __init__(self, desc):
        '''
        Constructor that adds a description to the tile
        
        Args:
            desc: Description of house
        '''
        self.__description = desc;
        #self.__monsterList= [];
        
    def getDesc(self):
        """Gets tile's description

        Returns:
            Description of tile

        """
        return self.__description

class House(Tile):
    '''
    House for game map that contains a list of monsters and observes them until they perish.
    '''
    
    def __init__(self,desc):
        """
        Constructer that sets up monsters in house
        
        Args:
            desc: Description of house
        """
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
        """Checks to see if any monsters are left in house

        Returns:
            True if all are dead, false if not

        """
        for x in self.__monsterList:
            if not isinstance(x,Person):
                return False
            
        return True
    
    def update(self,health, monster):
        """
        Updates house monster list if a monster dies
        """
        if health <= 0:
            print(monster.getName() + " has died")
            inX = self.__monsterList.index(monster)
            self.__monsterList.remove(monster)
            self.__monsterList.insert(inX, Person())
            
    def getList(self):
        """Gets house's list of monsters

        Returns:
            House's list of monsters

        """
        return self.__monsterList
            

    
        