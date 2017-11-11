'''
Created on Nov 8, 2017

@author: Cody
'''
from Tile import *
from Player import *
from pip._vendor.distlib.compat import raw_input
from builtins import str
class Game:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__map = Neighborhood()
        self.__player = Player()
        print("Welcome to the Neighborhood")
        self.__currSpot = self.__map.getGrid()[0][0]
        self.__currX = 0
        self.__currY = 0
        self.__currMsg = self.__map.getGrid()[0][0].getDesc() + "|[" + str(self.__currX) + "][" + str(self.__currY) + "]"
        

    def getInput(self):
        print("Type in a Command")
        msg = raw_input()
        return msg
    
    
    def playerMove(self, dirT):
        x=0
        y=0
        if dirT == "North":
            x = -1
        elif dirT == "South":
            x = 1
        elif dirT == "West":
            y = -1
        elif dirT == "East":
            y= 1
        else:
            self.__currMsg = "Invalid Direction"
        if isinstance(self.__currSpot, House):
            if(self.__currSpot.clear()):
                if(self.__currX+x>=0 and self.__currX+x<=len(self.__map.getGrid())):
                    try:
                        if (self.__currY+y>=0 and self.__currY+y<len(self.__map.getGrid()[self.__currX+x])):
                            self.__currX += x
                            self.__currY += y
                            self.__currSpot = self.__map.getGrid()[self.__currX][self.__currY]
                            self.__currMsg = self.__currSpot.getDesc() + "|[" + str(self.__currX) + "][" + str(self.__currY) + "]"
                        else:
                            self.__currMsg="Can't go that way"
                    except IndexError:
                        self.__currMsg = "Can't go that way"
                else:
                    self.__currMsg = "Can't go that way"
            else:
                self.__currMsg = "Kill the monsters first"
                
        else:
            if(self.__currX+x>=0 and self.__currX+x<=len(self.__map.getGrid())):
                try:
                    if (self.__currY+y>=0 and self.__currY+y<len(self.__map.getGrid()[self.__currX+x])):
                        self.__currX += x
                        self.__currY += y
                        self.__currSpot = self.__map.getGrid()[self.__currX][self.__currY]
                        self.__currMsg = self.__currSpot.getDesc() + "|[" + str(self.__currX) + "][" + str(self.__currY) + "]"
                    else:
                        self.__currMsg="Can't go that way"
                except IndexError:
                    self.__currMsg = "Can't go that way" 
            else:
                self.__currMsg = "Can't go that way"
                
                
            
            
    def getMsg(self):
        print (self.__currMsg)
        
        
    def command(self, msg):
        words = []
        words = msg.split()
        if len(words) == 0:
            self.__currMsg = "Type A Command, An Actual One"
            return
        if words[0] == "Move" or words[0] == "Go":
            if len(words)>1:
                if words[1] == "North" or words[1] == "South" or words[1] == "East" or words[1] == "West":
                    self.playerMove(words[1])
                else:
                    self.__currMsg = "Bad Command"
            else:
                self.__currMsg = "Bad Command"
        
        elif words[0] == "Attack":
            if len(words)>1:
                if words[1] == "Chocolate":
                    self.playerAttack("Chocolate Bars")
                elif words[1] == "Nerd":
                    self.playerAttack("Nerd Bombs")
                elif words[1] == "Sour":
                    self.playerAttack("Sour Straws")
                elif words[1] == "Kisses":
                    self.playerAttack("Hershey's Kisses")
                else:
                    self.__currMsg = "No Such Item"
            else:
                self.__currMsg = "Bad Command"
  
        elif words[0] == "Bag":
            invBag = ""
            for x in self.__player.getBag():
                invBag = invBag + x.getName() + ": " + str(x.getUses()) + "|"
                
            self.__currMsg = invBag
            
        elif words[0] == "List":
            listM = ""
            if isinstance(self.__currSpot, House):
                for x in self.__currSpot.getList():
                    listM = listM + x.getName() + ": " + str(x.getHP()) + "|"
                self.__currMsg = listM
            else:
                self.__currMsg = "There are no monsters here"
            
        elif words[0] == "Stats":
            self.__currMsg = "__player Health; " + str(self.__player.getHP()) + "|Attack: " + str(self.__player.getATK())
            
            
        else:
            self.__currMsg = "Bad Command"
        words = []
                
    def monsterAttack(self):
        if isinstance(self.__currSpot, House):
            if(self.__currSpot.clear()):
                return
            else:
                for x in self.__currSpot.getList():
                    x.attack(self.__player)
                    print (x.getName() + " attacks you for " + str(x.getAtk()))
        
                
    def playerAttack(self,weapon):
        if self.__player.checkItems(weapon):
            wep = self.__player.getItem(weapon)
            if isinstance(self.__currSpot, House):
                if(self.__currSpot.clear()):
                    self.__currMsg = "Everything is dead already"
                    return
                for x in self.__currSpot.getList():
                    x.hurt(wep,self.__player)
                wep.setUse()
                if(wep.getUses() == 0):
                    self.__player.getBag().remove(wep)
                self.__currMsg = "You Attack the Monster(s)"
                self.monsterAttack()
            else:
                self.__currMsg = "There's Nothing Here"
        else:
            self.__currMsg = "You don't have that"
            
    def gameOver(self):
        for x in self.__map.getGrid():
            for y in x:
                if isinstance(y, House):
                    if not y.clear():
                        return False
        
        return True  
    
    def deadGuy(self):
        if(self.__player.getHP() <= 0):
            return True
        return False