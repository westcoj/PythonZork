"""
 * The following module contains the player class which holds relevant information. When the player 
 * has no more health the game ends.
 *
 * @author Cody West
 * @version Zork Clone
 * @date 11/08/2017
"""
import random
from Weapon import *
class Player(object):
    '''
    Player class that interacts with the map and monsters as needed. When health is 0, the game ends.
    '''


    def __init__(self):
        '''
        Constructor that sets up player with random values
        '''
        self.__health = random.randint(500,750)
        self.__inventory = [Kisses()]
        self.__attack = random.randint(30,55)
        for i in range(0,9):
            num = random.randint(0,2)
            if num==0:
                self.__inventory.append(Straws())
            if num==2:
                self.__inventory.append(Bars())
            if num==1:
                self.__inventory.append(Bombs())
                
    
    
    def hit(self, val):
        """Removes health from player

        Args:
            val: Number of hitpoints to remove

        """
        self.__health -= val
        
    def getBag(self):
        """Gets player's inventory

        Returns:
            Player's list of weapons

        """
        return self.__inventory
        
    def checkItems(self, weapon):
        """Checks player's invetory for specific item
        
        Args:
            weapon: Item to look for

        Returns:
            True if found, else False

        """
        for x in self.__inventory:
            if(x.getName() == weapon):
                return True
        return False
    
    def getItem(self, weapon):
        """Gets a specific item from player's inventory

        Returns:
            Specific item to get

        """
        for x in self.__inventory:
            if(x.getName() == weapon):
                return x
            
    def getHP(self):
        """Gets player's health

        Returns:
            Player's health

        """
        return self.__health
    
    def getATK (self):
        """Gets player's attack value 
            Non-Gui supports documented criticals but gui does not. 

        Returns:
            Player's attack value

        """
        critDesc = []
        critDesc.append("Critical! The weaponized candy fills you with determination, and you strike")
        critDesc.append("Critical! You feel your body surge with heat, and you throw your fist forward with a shout, \"FALCON PUNCH\"")
        critDesc.append("Critical! You foolishly drink a beer while working, but its a homebrew, so you get +2 attack")
        critDesc.append("Critical! Tired of halloween, you muster the spirit of Thanksgiving and attack")
        critDesc.append("Critical! You draw in newfound strength and shout \"This is my ultimate technique!\", however it takes half a season to charge up")
        val = random.randint(0,4)
        val2 = random.randint(0,9)
        if(val2>=8):
            """Criticals Not Available in GUI"""
            #print(critDesc[val])
            return self.__attack+20
            
        return self.__attack