'''
Created on Nov 8, 2017

@author: Cody
'''
import random
from Weapon import *
class Player(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__health = random.randint(300,350)
        self.__inventory = [Kisses()]
        self.__attack = 100#random.randint(10,20)
        for i in range(0,9):
            num = random.randint(0,2)
            if num==0:
                self.__inventory.append(Straws())
            if num==2:
                self.__inventory.append(Bars())
            if num==1:
                self.__inventory.append(Bombs())
                
    
    
    def hit(self, val):
        self.__health -= val
        
    def getBag(self):
        return self.__inventory
        
    def checkItems(self, weapon):
        for x in self.__inventory:
            if(x.getName() == weapon):
                return True
        return False
    
    def getItem(self, weapon):
        for x in self.__inventory:
            if(x.getName() == weapon):
                return x
            
    def getHP(self):
        return self.__health
    
    def getATK (self):
        critDesc = []
        critDesc.append("The weaponized candy fills you with determination, and you strike")
        critDesc.append("You feel your body surge with heat, and you throw your fist forward with a shout, \"FALCON PUNCH\"")
        critDesc.append("You foolishly drink a beer while working, but its a homebrew, so you get +2 attack")
        critDesc.append("Tired of halloween, you muster the spirit of Thanksgiving and attack")
        critDesc.append("You draw in newfound strength and shout \"This is my ultimate technique!\", however it takes half a season to charge up")
        val = random.randint(0,4)
        val2 = random.randint(0,9)
        if(val2>=8):
            print(critDesc[val])
            return self.__attack+20
            
        return self.__attack