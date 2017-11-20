"""
 * The following module contains the weapon classes for the game that the 
 * player uses to attack monsters
 *
 * @author Cody West
 * @version Zork Clone
 * @date 11/08/2017
"""
import random

class Weapon(object):
    '''
    Super class contiaing generic weapon methods for specific inheritors to use
    '''


    def __init__(self, name, atk, uses):
        '''
        Constructor that sets up values of weapon
        
        Args:
            name: Type of weapon
            atk: Attack value of weapon
            uses: Number of times a weapon can be used
        '''
        self.__name = name
        self.__attack = atk
        self.__uses = uses
        
    def getName(self):
        """
        Gets weapon type
        """
        return self.__name
    
    def damage(self):
        """
        Gets weapon attack value
        """
        return self.__attack
    
    def getUses(self):
        """
        Gets weapon number of uses left
        """
        return self.__uses
    
    def setUse(self):
        """
        Sets weapon use down one
        """
        self.__uses -= 1
    
    def __str__(self, *args, **kwargs):
        """
        Gets weapon type (Expirementing with print statements)
        """
        return self.__name
    
    def print(self):
        """
        Gets weapon type (Expirementing with print statements)
        """
        return self.__name  
    
class Kisses(Weapon):
    '''
    Main weapon of player, never runs out of uses
    '''
    
    def __init__(self):
        '''
        Constructer that sets up Herhey's Kisses weapon
        '''
        atk = 1.0
        name = "Hershey's Kisses"
        uses = -1
        super().__init__(name,atk,uses)
        
        
class Straws(Weapon):
    '''
    Weapon of player with 2 uses. 
    '''
    
    def __init__(self):
        '''
        Constructer that sets up Sour Straws weapon
        '''
        atk = random.uniform(1.0,1.75)
        name = "Sour Straws"
        uses = 2
        super().__init__(name,atk,uses)
        
        
class Bars(Weapon):
    '''
    Weapon of player with 4 uses
    '''
    
    def __init__(self):
        '''
        Constructer that sets up Chocolate Bars weapon
        '''
        atk = random.uniform(2.0,2.4)
        name = "Chocolate Bars"
        uses = 4
        super().__init__(name,atk,uses)
        
        
class Bombs(Weapon):
    '''
    Weapon of player with single use
    '''
    
    def __init__(self):
        '''
        Constructer that sets up Nerd Bombs weapon
        '''
        atk = random.uniform(3.5,5.0)
        name = "Nerd Bombs"
        uses = 1
        super().__init__(name,atk,uses)
        
        
        
         
    
        
    
        
        
    