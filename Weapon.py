'''
Created on Nov 8, 2017

@author: Cody
'''
import random

class Weapon(object):
    '''
    classdocs
    '''


    def __init__(self, name, atk, uses):
        '''
        Constructor
        '''
        self.__name = name
        self.__attack = atk
        self.__uses = uses
        
    def getName(self):
        return self.__name
    
    def damage(self):
        return self.__attack
    
    def getUses(self):
        return self.__uses
    
    def setUse(self):
        self.__uses -= 1
    
    def __str__(self, *args, **kwargs):
        return self.__name
    
    def print(self):
        return self.__name  
    
class Kisses(Weapon):
    '''
    docs
    '''
    
    def __init__(self):
        atk = 1.0
        name = "Hershey's Kisses"
        uses = -1
        super().__init__(name,atk,uses)
        
        
class Straws(Weapon):
    '''
    docs
    '''
    
    def __init__(self):
        atk = random.uniform(1.0,1.75)
        name = "Sour Straws"
        uses = 2
        super().__init__(name,atk,uses)
        
        
class Bars(Weapon):
    '''
    docs
    '''
    
    def __init__(self):
        atk = random.uniform(2.0,2.4)
        name = "Chocolate Bars"
        uses = 4
        super().__init__(name,atk,uses)
        
        
class Bombs(Weapon):
    '''
    docs
    '''
    
    def __init__(self):
        atk = random.uniform(3.5,5.0)
        name = "Nerd Bombs"
        uses = 1
        super().__init__(name,atk,uses)
        
        
        
         
    
        
    
        
        
    